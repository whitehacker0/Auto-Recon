import os
import whois_recon
import github_recon
import linkedin_recon
import phone_recon
import subdomain_recon 
def main():
    print("\n🔍 OSINT Toolkit - Automated Reconnaissance\n")
    print("1. GitHub Recon")
    print("2. Phone Number OSINT")
    print("3. WHOIS Domain Lookup")
    print("4. Subdomain Reconnaissance")
    print("5. LinkedIn Recon") 
    print("6. Run All")

    choice = input("\nSelect an option: ").strip()

    if choice == "1":
        username = input("Enter GitHub username: ").strip()
        if username:
            github_recon.save_github_data(username)
        else:
            print("❌ GitHub username is required.")

    elif choice == "2":
        phone = input("Enter phone number to lookup: ").strip()
        if phone:
            result = phone_recon.lookup_phone(phone)
            print("\n🔍 Phone Lookup Results:")
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print("❌ Phone number is required.")

    elif choice == "3":
        domain = input("Enter domain (e.g., example.com): ").strip()
        if domain:
            whois_recon.whois_lookup(domain)
        else:
            print("❌ Domain name is required.")

    elif choice == "4":
        domain = input("Enter domain (e.g., example.com): ").strip()
        if domain:
            subdomain_recon.find_subdomains(domain)
        else:
            print("❌ Domain name is required.")

    elif choice == "5":
        linkedin_recon.search_linkedin()  # No argument needed

    elif choice == "6":
        username = input("Enter GitHub username: ").strip()
        phone = input("Enter phone number to lookup: ").strip()
        domain = input("Enter domain (e.g., example.com): ").strip()

        if username:
            github_recon.save_github_data(username)
        if phone:
            result = phone_recon.lookup_phone(phone)
            print("\n🔍 Phone Lookup Results:")
            for key, value in result.items():
                print(f"{key}: {value}")
        if domain:
            whois_recon.whois_lookup(domain)
            subdomain_recon.find_subdomains(domain)

        linkedin_choice = input("\nWould you like to run LinkedIn Recon? (y/n): ").strip().lower()
        if linkedin_choice == "y":
            linkedin_recon.search_linkedin()  

    else:
        print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
