import os
import requests
from config import GITHUB_TOKEN

def get_github_info(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            "👤 Username": data.get("login", "N/A"),
            "📝 Name": data.get("name", "N/A"),
            "📖 Bio": data.get("bio", "N/A"),
            "🌎 Location": data.get("location", "Unknown"),
            "🏢 Company": data.get("company", "N/A"),
            "📧 Email": data.get("email", "N/A"),
            "🐦 Twitter": data.get("twitter_username", "N/A"),
            "📅 Account Created": data.get("created_at", "N/A"),
            "🔄 Last Updated": data.get("updated_at", "N/A"),
            "📂 Public Repos": data.get("public_repos", 0),
            "⭐ Starred Repos": get_starred_count(username, headers),
            "👥 Followers": data.get("followers", 0),
            "🔗 Profile URL": data.get("html_url"),
            "🛠️ Organizations": get_user_orgs(username, headers)
        }
    else:
        return {"❌ Error": "User not found or API limit exceeded."}

def get_starred_count(username, headers):
    url = f"https://api.github.com/users/{username}/starred"
    response = requests.get(url, headers=headers)
    return len(response.json()) if response.status_code == 200 else "N/A"

def get_user_orgs(username, headers):
    url = f"https://api.github.com/users/{username}/orgs"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        orgs = [org["login"] for org in response.json()]
        return ", ".join(orgs) if orgs else "None"
    return "N/A"

def save_github_data(username):
    profile_info = get_github_info(username)

    with open("githubdata.txt", "w", encoding="utf-8") as file:
        file.write("🐙 GitHub OSINT Report\n")
        file.write("=====================\n\n")
        for key, value in profile_info.items():
            file.write(f"{key}: {value}\n")

    print("\n✅ GitHub data saved to 'githubdata.txt'")

if __name__ == "__main__":
    username = input("Enter GitHub username: ").strip()
    save_github_data(username)
