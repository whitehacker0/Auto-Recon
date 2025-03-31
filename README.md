# OSINT Multi Recon Tool

## 📌 Overview
The **OSINT Multi Recon Tool** is an automated reconnaissance tool designed to help penetration testers, cybersecurity professionals, and ethical hackers gather valuable open-source intelligence (OSINT). This tool provides various reconnaissance modules, including:

- **GitHub Recon** – Extracts information about a user's repositories, followers, and contributions.
- **LinkedIn Recon** – Searches for LinkedIn profiles based on a target's name.
- **Phone Number OSINT** – Looks up phone number details from public sources.
- **WHOIS Domain Lookup** – Retrieves WHOIS information for a given domain.
- **Subdomain Reconnaissance** – Finds subdomains related to a target domain.

## 🔥 Why This Tool is Useful for Penetration Testers
Penetration testers can leverage this tool to:
- Gather preliminary information about a target before an engagement.
- Identify subdomains and potential attack surfaces.
- Conduct WHOIS lookups to discover domain ownership details.
- Perform social engineering reconnaissance using LinkedIn data.
- Investigate GitHub repositories for leaked credentials or sensitive information.

## 🛠 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/WallaceScott240/osint-multi-recon-tool.git
   cd osint-multi-recon-tool
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the main script:
```sh
python osint_tool.py
```

### Menu Options:
1️⃣ **GitHub Recon** – Enter a GitHub username to extract public data.
2️⃣ **LinkedIn Recon** – Search for LinkedIn profiles using a name and optional keywords.
3️⃣ **Phone Number OSINT** – Enter a phone number to gather OSINT data.
4️⃣ **WHOIS Domain Lookup** – Retrieve WHOIS information for a domain.
5️⃣ **Subdomain Reconnaissance** – Find subdomains associated with a domain.
6️⃣ **Run All** – Execute all modules sequentially.

## 📂 Project Structure
```
📁 OSINT Multi Recon Tool
│-- 📜 osint_tool.py           # Main script
│-- 📜 github_recon.py         # GitHub reconnaissance module
│-- 📜 linkedin_recon.py       # LinkedIn reconnaissance module
│-- 📜 phone_recon.py          # Phone number OSINT module
│-- 📜 whois_recon.py          # WHOIS lookup module
│-- 📜 subdomain_recon.py      # Subdomain reconnaissance module
│-- 📜 config.py               # Configuration file (if needed)
│-- 📜 requirements.txt        # Required Python libraries
│-- 📜 whoisdata.txt           # WHOIS lookup results
│-- 📜 subdomains_xxx.txt      # Subdomain reconnaissance results
│-- 📜 githubdata.txt          # GitHub reconnaissance results
```

## ⚠ Disclaimer
This tool is intended for educational and ethical security testing purposes only. Unauthorized use against targets without permission is illegal and punishable by law. Use responsibly.

