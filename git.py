import subprocess
import os
import base64

class GitAPI:
    TOKEN = os.getenv("TOKEN")

    @staticmethod
    def get_auth_env():
        # トークンをURL・.git/config・コマンドライン引数に残さないよう、環境変数でヘッダーを渡す
        credential = base64.b64encode(f"x-access-token:{GitAPI.TOKEN}".encode()).decode()
        env = os.environ.copy()
        env["GIT_CONFIG_COUNT"] = "1"
        env["GIT_CONFIG_KEY_0"] = "http.extraHeader"
        env["GIT_CONFIG_VALUE_0"] = f"Authorization: Basic {credential}"
        return env

    @staticmethod
    def git_clone_or_pull(repo_url, local_dir):
        git_dir = os.path.join(local_dir,".git")
        isClone = False
        if not os.path.exists(git_dir):
            # 存在しなければクローン
            isClone = True
            print(f"Cloning {repo_url} ...")
            result = subprocess.run(["git", "clone", repo_url, local_dir], capture_output=True, text=True, env=GitAPI.get_auth_env())
        else:
            # 存在すれば pull
            print(f"Pulling updates in {local_dir} ...")
            result = subprocess.run(["git", "-C", local_dir, "pull"], capture_output=True, text=True, env=GitAPI.get_auth_env())

        if result.returncode == 0:
            if isClone:
                print("✅ Git Clone operation successful")
            else:
                print("✅ Git Pull update operation successful")
        else:
            print(f"⚠️ Git operation failed:\n{result.stdout}\n{result.stderr}")
            raise RuntimeError(f"{local_dir}\n{result.stdout}\n{result.stderr}")
