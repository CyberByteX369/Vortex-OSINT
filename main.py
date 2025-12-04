import typer
import asyncio
import re
import os
import httpx
import dns.resolver
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.prompt import Prompt
from typing import Optional

# Initialize App and Console
app = typer.Typer(help="Vortex-OSINT: Modern Security Tool")
console = Console()

# --- MODULE 1: IP INTELLIGENCE ---
async def fetch_ip_data(ip: str):
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,city,zip,isp,org,as,query"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return response.json()
        except Exception as e:
            return {"status": "fail", "message": str(e)}

@app.command()
def ip(target: str = typer.Option(..., help="The IP address to scan")):
    """Scan an IP address for geolocation and ISP info."""
    console.print(Panel(f"[bold cyan]Scanning IP Target:[/bold cyan] {target}", border_style="cyan"))
    
    with console.status("[bold green]Fetching data...[/bold green]", spinner="dots"):
        data = asyncio.run(fetch_ip_data(target))

    if data.get("status") == "success":
        table = Table(title="IP Intelligence Results", show_header=True, header_style="bold magenta")
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="white")
        
        table.add_row("IP", data.get("query"))
        table.add_row("Country", data.get("country"))
        table.add_row("City", data.get("city"))
        table.add_row("ISP", data.get("isp"))
        table.add_row("Organization", data.get("org"))
        table.add_row("ASN", data.get("as"))
        
        console.print(table)
    else:
        console.print(f"[bold red]Error:[/bold red] {data.get('message', 'Unknown error')}")

# --- MODULE 2: USERNAME RECON ---
SITES = {
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Facebook": "https://www.facebook.com/{}",
    "Medium": "https://medium.com/@{}"
}

async def check_site(client, site, url, username):
    formatted_url = url.format(username)
    try:
        response = await client.get(formatted_url, timeout=10.0)
        if response.status_code == 200:
            return site, formatted_url, True
    except:
        pass
    return site, formatted_url, False

async def scan_usernames(username: str):
    async with httpx.AsyncClient() as client:
        tasks = [check_site(client, site, url, username) for site, url in SITES.items()]
        results = await asyncio.gather(*tasks)
        return results

@app.command()
def user(name: str = typer.Option(..., help="The username to search across social media")):
    """Search for a username across popular social networks."""
    console.print(Panel(f"[bold yellow]Hunting Username:[/bold yellow] {name}", border_style="yellow"))
    
    results = asyncio.run(scan_usernames(name))
    
    table = Table(show_header=True, header_style="bold green")
    table.add_column("Platform", style="cyan")
    table.add_column("Status", style="bold")
    table.add_column("URL", style="dim")

    found_count = 0
    for site, url, found in results:
        if found:
            table.add_row(site, "[green]FOUND[/green]", url)
            found_count += 1
        else:
            table.add_row(site, "[red]NOT FOUND[/red]", "-")

    console.print(table)
    console.print(f"\n[bold green]Total Found:[/bold green] {found_count}")

# --- MODULE 3: EMAIL & BREACH SEARCH (The "Grep" Replacement) ---
@app.command()
def breach(
    pattern: str = typer.Option(..., help="Regex pattern to search (e.g. 'm.*4@gmail.com')"),
    file: str = typer.Option(..., help="Path to your local database file (txt/sql)")
):
    """
    Search a local database file using Regex patterns (Solves the 'Wildcard' problem).
    """
    console.print(Panel(f"[bold red]Breach Hunter[/bold red]\nTarget Pattern: {pattern}\nDatabase: {file}", border_style="red"))

    if not os.path.exists(file):
        console.print(f"[bold red]Error:[/bold red] File '{file}' not found.")
        return

    regex = re.compile(pattern)
    matches = []
    
    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            progress.add_task(description="Scanning file...", total=None)
            
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                for line_num, line in enumerate(f, 1):
                    if regex.search(line):
                        matches.append((line_num, line.strip()))
                        # Limit to first 20 matches to prevent flooding
                        if len(matches) >= 20:
                            break
                            
        if matches:
            console.print(f"\n[bold green]Found {len(matches)}+ Matches:[/bold green]")
            for num, content in matches:
                console.print(f"[cyan]Line {num}:[/cyan] [white]{content}[/white]")
            if len(matches) >= 20:
                console.print("\n[yellow]Limit reached (20). Refine your pattern for specific results.[/yellow]")
        else:
            console.print("[bold yellow]No matches found.[/bold yellow]")

    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

@app.command()
def check_mx(email: str):
    """Check if an email domain has valid MX records."""
    domain = email.split('@')[-1]
    try:
        records = dns.resolver.resolve(domain, 'MX')
        console.print(f"[bold green]Valid MX Records found for {domain}:[/bold green]")
        for mx in records:
            console.print(f"  - {mx.exchange}")
    except Exception:
        console.print(f"[bold red]No valid MX records found for {domain}. Email likely invalid.[/bold red]")

if __name__ == "__main__":
    app()
