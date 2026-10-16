import os
import sys
from dotenv import load_dotenv
load_dotenv()
from github import GitHubAPI
from git import GitAPI
from webhook import WebhookAPI
from directory import DirectoryAPI


LOCAL_DIR = os.getenv("LOCAL_DIR")

print("Start")
try:
    repos = GitHubAPI.get_github_repos()
except Exception as e:
    WebhookAPI.send_message(f"01 GitHubAPIに問題が発生しました。Tokenの有効期限が切れてませんか？\n{e}")
    sys.exit(1)
try:
    path = DirectoryAPI.get_directory_today(LOCAL_DIR)
except Exception as e:
    WebhookAPI.send_message(f"02 ディレクトリ操作に問題が発生しました。権限に異常が出ているかもしれません\n{e}")
    sys.exit(1)

failed = []
for repo in repos:
    URL = repo["clone_url"]

    DIR = os.path.join(path, repo["name"])

    try:
        GitAPI.git_clone_or_pull(URL, DIR)
    except Exception as e:
        failed.append(f"{repo['name']}: {e}")
print()

DirectoryAPI.delete_old_directory(LOCAL_DIR)

if failed:
    WebhookAPI.send_message("03 Gitに異常が出ました。いったい何が？\n" + "\n".join(failed))
    sys.exit(1)

WebhookAPI.send_message("Clone & Pull & Clear 完了")