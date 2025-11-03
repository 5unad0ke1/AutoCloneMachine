import subprocess
import os
from webhook import WebhookAPI

class GitAPI:
    def git_clone_or_pull(repo_url, local_dir):
        git_dir = os.path.join(local_dir,".git")
        isClone = False
        if not os.path.exists(git_dir):
            # 存在しなければクローン
            isClone = True
            print(f"Cloning {repo_url} ...")
            result = subprocess.run(["git", "clone", repo_url, local_dir], capture_output=True, text=True)
        else:
            # 存在すれば pull
            print(f"Pulling updates in {local_dir} ...")
            result = subprocess.run(["git", "-C", local_dir, "pull"], capture_output=True, text=True)
        
        if result.returncode == 0:
            if isClone:
                print("✅ Git Clone operation successful")
            else:
                print("✅ Git Pull update operation successful")
        else:   
            print(f"⚠️ Git operation failed:\n{result.stdout}\n{result.stderr}")
            WebhookAPI.send_message(f"⚠️ Git operation failed:\n{result.stdout}\n{result.stderr}")
