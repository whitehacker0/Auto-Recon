import whois

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        
        details = {
            "🌍 Domain Name": domain_info.domain_name,
            "🏢 Registrar": domain_info.registrar,
            "📅 Creation Date": domain_info.creation_date,
            "⏳ Expiration Date": domain_info.expiration_date,
            "🔄 Updated Date": domain_info.updated_date,
            "🖧 Name Servers": domain_info.name_servers,
            "🔒 Status": domain_info.status,
            "🏢 Registrant": getattr(domain_info, "org", "Private"),
            "📧 Emails": getattr(domain_info, "emails", "Not Available"),
            "🌎 Country": getattr(domain_info, "country", "Unknown")
        }
        
        filename = "whois.txt"  # Fixed filename
        with open(filename, "w", encoding="utf-8") as file:
            file.write("🌍 WHOIS Lookup Report\n")
            file.write("=" * 40 + "\n\n")
            
            for key, value in details.items():
                file.write(f"{key}:\n")
                if isinstance(value, list):
                    for item in value:
                        file.write(f"  - {item}\n")
                else:
                    file.write(f"{value}\n")
                file.write("\n")
        
        print(f"\n✅ WHOIS data saved to '{filename}'")

    except Exception as e:
        print(f"❌ Error retrieving WHOIS data: {e}")

if __name__ == "__main__":
    domain = input("Enter a domain (e.g., example.com): ").strip()
    whois_lookup(domain)
