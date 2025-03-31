import requests
import json

def get_crtsh_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdomains = set()
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            json_data = response.json()
            subdomains.update(entry['name_value'].strip() for entry in json_data)
    except requests.RequestException as e:
        subdomains.add(f"❌ Error fetching data from crt.sh: {e}")
    return subdomains

def get_threatcrowd_subdomains(domain):
    url = f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
    subdomains = set()
    try:
        response = requests.get(url, timeout=10, verify=False)  # Disable SSL verification
        if response.status_code == 200:
            json_data = response.json()
            if json_data.get("subdomains"):
                subdomains.update(json_data["subdomains"])
    except requests.RequestException as e:
        subdomains.add(f"❌ Error fetching data from ThreatCrowd: {e}")
    return subdomains

def find_subdomains(domain):
    subdomains = set()
    subdomains.update(get_crtsh_subdomains(domain))
    subdomains.update(get_threatcrowd_subdomains(domain))
    save_subdomains(domain, subdomains)

def save_subdomains(domain, subdomains):
    filename = f"subdomains_{domain}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("🔍 Subdomain Enumeration Report\n")
        file.write("====================================\n\n")
        file.write(f"📌 Target Domain: {domain}\n")
        file.write(f"📅 Total Subdomains Found: {len(subdomains)}\n\n")
        file.write("📜 Subdomains List:\n")
        file.write("--------------------\n")
        for sub in sorted(subdomains):
            file.write(f"🔹 {sub}\n")
    print(f"✅ Subdomains saved to {filename}")

if __name__ == "__main__":
    target_domain = input("Enter target domain: ").strip()
    find_subdomains(target_domain)
