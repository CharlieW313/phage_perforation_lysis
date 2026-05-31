import os
import zipfile

DIRS_TO_ZIP = ['analysis']

def zip_directories(DIRS_TO_ZIP, root_folder='.'):
    for dir_name in DIRS_TO_ZIP:
        dir_path = os.path.join(root_folder, dir_name)

        if not os.path.isdir(dir_path):
            print(f"Skipping: {dir_name} (not found)")
            continue

        zip_path = os.path.join(root_folder, dir_name + '.zip')
        print(f"Zipping: {dir_name}")

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for walk_root, walk_dirs, files in os.walk(dir_path):
                for file in files:
                    full_path = os.path.join(walk_root, file)
                    arcname = os.path.relpath(full_path, root_folder)
                    zipf.write(full_path, arcname)

        print(f"Created: {zip_path}")

    print("\nDone!")

zip_directories(DIRS_TO_ZIP, root_folder='.')