import subprocess
import os
import base64

class GitAPI:
    TOKEN = os.getenv("TOKEN")

    @staticmethod
    def get_auth_args():
        # トークンをURLや.git/configに残さないよう、実行時のみヘッダーで渡す
        credential = base64.b64encode(f"x-access-token:{GitAPI.TOKEN}".encode()).decode()
        return ["-c", f"http.extraHeader=Authorization: Basic {credential}"]

    @staticmethod
    def git_clone_or_pull(repo_url, local_dir):
        git_dir = os.path.join(local_dir,".git")
        isClone = False
        if not os.path.exists(git_dir):
            # 存在しなければクローン
            isClone = True
            print(f"Cloning {repo_url} ...")
            result = subprocess.run(["git", *GitAPI.get_auth_args(), "clone", repo_url, local_dir], capture_output=True, text=True)
        else:
            # 存在すれば pull
            print(f"Pulling updates in {local_dir} ...")
            result = subprocess.run(["git", "-C", local_dir, *GitAPI.get_auth_args(), "pull"], capture_output=True, text=True)

        if result.returncode == 0:
            if isClone:
                print("✅ Git Clone operation successful")
            else:
                print("✅ Git Pull update operation successful")
        else:
            print(f"⚠️ Git operation failed:\n{result.stdout}\n{result.stderr}")
            raise RuntimeError(f"{local_dir}\n{result.stdout}\n{result.stderr}")
