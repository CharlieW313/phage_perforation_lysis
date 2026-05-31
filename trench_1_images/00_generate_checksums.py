import hashlib
import os
import csv

def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        return f"ERROR: {str(e)}"

def run_generator(root_folder, output_csv):
    # --- Pass 1: hash all files and write the CSV ---
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Relative Path', 'SHA256'])
        
        EXCLUDED_DIRS = {'.git', '__pycache__', '.ipynb_checkpoints'}
        for root, dirs, files in os.walk(root_folder):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, root_folder)

                if os.path.abspath(full_path) == os.path.abspath(output_csv):
                    continue

                print(f"Hashing: {rel_path}")
                checksum = get_sha256(full_path)
                writer.writerow([rel_path, checksum])

    # --- Pass 2: hash the completed CSV and write to a separate file ---
    csv_checksum = get_sha256(output_csv)
    manifest_path = output_csv + '.sha256'
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write(csv_checksum)

    print(f"\nFinished! Manifest saved to: {output_csv}")
    print(f"Manifest checksum saved to: {manifest_path}")
    
# USAGE: Set your directory and desired output name
run_generator('.', 'checksum_list.csv')