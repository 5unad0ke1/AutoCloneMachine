import requests

class GitHubAPI:

    USER_NAME = "5unad0ke1"
    TOKEN = "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"
    
    @staticmethod
    def get_github_repos():
        TOKEN = GitHubAPI.TOKEN
        headers = {"Authorization": f"token {TOKEN}"}

        repos = []
        page = 1
        while True:
            url = f"https://api.github.com/user/repos?per_page=100&page={page}"
            r = requests.get(url, headers=headers)
            r.raise_for_status() 
            data = r.json()
            if not data:
                break
                
            for repo in data:
                    if repo["owner"]["login"] == GitHubAPI.USER_NAME:
                        repos.append(repo)
            page += 1

            print("Repositories")
            for repo in repos:
                print(repo["name"])
            print()
        return repos
    