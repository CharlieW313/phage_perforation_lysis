import os
import zipfile

ZIPS_TO_EXTRACT = ['analysis.zip']

def extract_zips(ZIPS_TO_EXTRACT, root_folder='.'):
    for zip_name in ZIPS_TO_EXTRACT:
        zip_path = os.path.join(root_folder, zip_name)

        if not os.path.exists(zip_path):
            print(f"Skipping: {zip_name} (not found)")
            continue
        
        print(f"Extracting: {zip_name}")
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            extract_dir = os.path.splitext(zip_path)[0]
            os.makedirs(extract_dir, exist_ok=True)
            zipf.extractall(extract_dir)

        print(f"Extracted: {zip_name}")

    print("\nDone!")

extract_zips(ZIPS_TO_EXTRACT, root_folder='.')