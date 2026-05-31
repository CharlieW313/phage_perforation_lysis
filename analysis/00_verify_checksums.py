import hashlib
import os
import csv

def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    if not os.path.exists(file_path):
        return "MISSING"
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return "ERROR_READING"

def run_verification(root_folder, input_csv):
    # --- Step 1: Verify the manifest's own integrity first ---
    manifest_path = input_csv + '.sha256'
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            expected_csv_hash = f.read().strip()
        actual_csv_hash = get_sha256(input_csv)
        if actual_csv_hash == expected_csv_hash:
            print(f"Manifest integrity OK: {input_csv}\n")
        else:
            print(f"WARNING: Manifest checksum FAILED  {input_csv} may have been altered!")
            print("Aborting verification as the manifest cannot be trusted.\n")
            return
    else:
        print(f"WARNING: No .sha256 sidecar file found. Manifest integrity cannot be confirmed.\n")

    # --- Step 2: Verify all files listed in the CSV ---
    mismatches = 0
    total_files = 0
    with open(input_csv, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            total_files += 1
            rel_path = row['Relative Path']
            expected_hash = row['SHA256']
            local_path = os.path.join(root_folder, rel_path)
            actual_hash = get_sha256(local_path)
            if actual_hash == expected_hash:
                print(f"OK: {rel_path}")
            elif actual_hash == "MISSING":
                print(f"MISSING: {rel_path}")
                mismatches += 1
            else:
                print(f"CORRUPT/CHANGED: {rel_path}")
                mismatches += 1

    print(f"\nVerification Complete.")
    print(f"Total checked: {total_files} | Errors found: {mismatches}")

run_verification('.', 'checksum_list.csv')
