import webbrowser
import urllib.parse

def search_linkedin():
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    
    if not first_name or not last_name:
        print("❌ First and last name are required!")
        return
    
    keywords = input("Enter up to 3 keywords (separated by spaces, optional): ").strip()
    keyword_list = keywords.split()[:3]  
    
    query_parts = [f'"{first_name} {last_name}"']
    if keyword_list:
        query_parts.append(" ".join(keyword_list))
    
    search_query = f'site:linkedin.com/in { " ".join(query_parts) }'
    encoded_query = urllib.parse.quote(search_query)
    
    url = f"https://www.google.com/search?q={encoded_query}"
    
    print(f"\n🔍 Searching LinkedIn profiles for: {first_name} {last_name} {' '.join(keyword_list)}\n")
    webbrowser.open(url)

if __name__ == "__main__":
    search_linkedin()
