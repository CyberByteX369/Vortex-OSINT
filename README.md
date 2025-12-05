cat <<EOF > README.md
# 🌪️ Vortex-OSINT

> **A Modern, Async-Powered Security Intelligence Tool.**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Kali](https://img.shields.io/badge/Kali_Linux-Supported-dragon?style=for-the-badge&logo=kalilinux)
![Termux](https://img.shields.io/badge/Termux-Ready-green?style=for-the-badge&logo=android)

Vortex is an all-in-one OSINT CLI tool designed for security researchers. It aggregates email validation, IP geolocation, username reconnaissance, and local breach database searching into a single, high-performance interface.

## 🚀 Features

* **📧 Email Intel:** Validates email format, checks MX records, and detects disposable domains.
* **🕵️ Username Recon:** Asynchronously scans 20+ social media sites (Instagram, GitHub, Reddit, etc.) for user presence.
* **🌍 IP Geolocation:** Detailed ISP, City, and ASN mapping using high-speed APIs.
* **🔓 Breach Hunter:** A built-in Regex search engine to find patterns (like \`m*4@gmail.com\`) inside your local text databases without using complex grep commands.
* **⚡ Async Performance:** Uses \`httpx\` and \`asyncio\` for blazing fast results.
* **📱 Cross-Platform:** Auto-detects and installs dependencies for **Kali Linux** and **Termux**.

## 📦 Installation

**1. Clone the repository**
```bash
git clone https://github.com/CyberByteX369/Vortex-OSINT.git
cd Vortex-OSINT
```

**2. Run the Universal Auto-Fix Script**
This script automatically detects your OS (Kali, Ubuntu, or Termux) and installs the correct dependencies to prevent errors.
```bash
chmod +x fix_environment.sh
./fix_environment.sh
```

**3. Activate the Virtual Environment**
```bash
source venv/bin/activate
```

## 💻 Usage

### Main Menu
```bash
python main.py --help
```

### 🔍 Search a Pattern in a Database
Find emails matching a pattern (e.g., starts with 'm', ends with '4', gmail.com) in your local file.
```bash
python main.py breach --pattern "m.*4@gmail.com" --file /path/to/database.txt
```

### 👤 Scan a Username
```bash
python main.py user --name "cyberadmin"
```

### 🌐 Analyze an IP Address
```bash
python main.py ip --target "1.1.1.1"
```

## ⚠️ Disclaimer
This tool is for educational purposes and security research only. The author is not responsible for misuse.
EOF
