🌪️ Vortex-OSINT

A Modern, Async-Powered Security Intelligence Tool for Linux & Windows.

Vortex is an all-in-one OSINT tool designed for security researchers. It aggregates email validation, IP geolocation, username reconnaissance, and local breach database searching into a single, beautiful CLI.

🚀 Features

📧 Email Intel: Validates email format, checks MX records, and detects disposable domains.

🕵️ Username Recon: Asynchronously scans social media sites (Instagram, GitHub, Reddit, etc.) for user presence.

🌍 IP Geolocation: detailed ISP, City, and ASN mapping.

🔓 Breach Hunter: A built-in Regex search engine to find patterns (like m*4@gmail.com) inside your local text databases without using complex grep commands.

⚡ Async Performance: Uses httpx and asyncio for blazing fast results.

📦 Installation

1. Clone the repository

```bash
git clone [https://github.com/yourusername/Vortex-OSINT.git](https://github.com/yourusername/Vortex-OSINT.git)
```
```bash
cd Vortex-OSINT
```


3. Set up Virtual Environment (Fixes Kali/Debian errors)
``` bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies
``` bash
pip install -r requirements.txt
```

💻 Usage

Main Menu
``` bash
python main.py --help
```

1. Search a Pattern in a Local Database
Instead of using grep, use Vortex to find partial emails (e.g., m...4@gmail.com).
``` bash
python main.py breach --pattern "m.*4@gmail.com" --file /path/to/database.txt
```

2. Scan a Username
``` bash
python main.py user --name "cyberadmin"
```

3. Analyze an IP Address
``` bash
python main.py ip --target "1.1.1.1"
```

⚠️ Disclaimer

This tool is for educational purposes and security research only. Using this tool to target systems without permission is illegal. The author is not responsible for misuse.
