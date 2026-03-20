from datetime import datetime
import os
import shutil

class DirectoryAPI:

    max_directory = 5
    
    @staticmethod
    def get_directory_today(from_path):

        today = datetime.today().strftime("%Y%m%d")
        path = os.path.join(from_path,today)

        os.makedirs(path, exist_ok=True)
        return path
    
    @staticmethod
    def delete_old_directory(from_path):
        dirs = [
            name for name in os.listdir(from_path)
                if os.path.isdir(os.path.join(from_path, name))
        ]
        
        print("Current Directries")
        for dir in dirs:
            print(dir)
        
        print()
        
        if len(dirs) > DirectoryAPI.max_directory:
            dirs_sorted = sorted(dirs)
            remove_count = len(dirs_sorted) - DirectoryAPI.max_directory
            to_remove = dirs_sorted[:remove_count]
            for d in to_remove:
                path_to_remove = os.path.join(from_path, d)
                try:
                    shutil.rmtree(path_to_remove)
                    print(f"Removed old directory: {path_to_remove}")
                except Exception as e:
                    print(f"Failed to remove {path_to_remove}: {e}")
            print("Done")
        