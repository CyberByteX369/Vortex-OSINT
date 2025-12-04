🌪️ Vortex-OSINT
> A Modern, Async-Powered Security Intelligence Tool.
> 
Vortex is an all-in-one OSINT CLI tool designed for security researchers. It aggregates email validation, IP geolocation, username reconnaissance, and local breach database searching into a single, high-performance interface.
🚀 Features
 * 📧 Email Intel: Validates email format, checks MX records, and detects disposable domains.
 * 🕵️ Username Recon: Asynchronously scans 20+ social media sites (Instagram, GitHub, Reddit, etc.) for user presence.
 * 🌍 IP Geolocation: Detailed ISP, City, and ASN mapping using high-speed APIs.
 * 🔓 Breach Hunter: A built-in Regex search engine to find patterns (like m*4@gmail.com) inside your local text databases without using complex grep commands.
 * ⚡ Async Performance: Uses httpx and asyncio for blazing fast results.
📦 Installation
1. Clone the repository
``` bash
git clone https://github.com/CyberByteX369/Vortex-OSINT.git
```
``` bash
cd Vortex-OSINT
```

2. Run the Auto-Setup (Fixes Environment Errors)
``` bash
chmod +x setup.sh
```
``` bash
./setup.sh
```

3. Activate the Virtual Environment
``` bash
source venv/bin/activate
```

💻 Usage
Main Menu
``` bash
python main.py --help
```

🔍 Search a Pattern in a Database
Find emails matching a pattern (e.g., starts with 'm', ends with '4', gmail.com) in your local file.
``` bash
python main.py breach --pattern "m.*4@gmail.com" --file /home/kali/Downloads/database.txt
```

👤 Scan a Username
``` bash
python main.py user --name "cyberadmin"
```

🌐 Analyze an IP Address

``` bash
python main.py ip --target "1.1.1.1"
```

⚠️ Disclaimer
This tool is for educational purposes and security research only. The author is not responsible for misuse.
