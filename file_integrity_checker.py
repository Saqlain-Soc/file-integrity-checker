import hashlib
import json
import os
from datetime import datetime
from pathlib import Path

BASELINE_FILE = "file_baseline.json"

def calculate_hashes(file_path):
    """Calculate MD5 and SHA-256 hashes of a file"""
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                md5_hash.update(chunk)
                sha256_hash.update(chunk)
        return {
            "md5": md5_hash.hexdigest(),
            "sha256": sha256_hash.hexdigest()
        }
    except Exception as e:
        return None


def load_baseline():
    """Load existing baseline from JSON file"""
    if os.path.exists(BASELINE_FILE):
        with open(BASELINE_FILE, "r") as f:
            return json.load(f)
    return {}


def save_baseline(baseline):
    """Save baseline to JSON file"""
    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)


def add_files_to_baseline():
    """Add new files to the baseline"""
    baseline = load_baseline()
    
    print("\n=== Add Files to Baseline ===")
    print("Enter file paths one by one. Type 'done' when finished.\n")
    
    while True:
        path = input("File path (or 'done'): ").strip()
        if path.lower() == "done":
            break
        
        if not os.path.isfile(path):
            print(f"[!] File not found: {path}")
            continue
        
        abs_path = str(Path(path).resolve())
        hashes = calculate_hashes(abs_path)
        
        if hashes:
            baseline[abs_path] = {
                "md5": hashes["md5"],
                "sha256": hashes["sha256"],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"[+] Added: {abs_path}")
        else:
            print(f"[!] Failed to hash: {abs_path}")
    
    save_baseline(baseline)
    print(f"\n[✓] Baseline saved to {BASELINE_FILE}")


def check_integrity():
    """Check integrity of all files in baseline"""
    baseline = load_baseline()
    
    if not baseline:
        print("\n[!] No baseline found. Please add files first.")
        return
    
    print("\n=== File Integrity Check ===")
    print(f"Checking {len(baseline)} file(s)...\n")
    
    for file_path, data in baseline.items():
        print(f"File: {file_path}")
        
        if not os.path.exists(file_path):
            print("Status: MISSING")
            print("-" * 60)
            continue
        
        current_hashes = calculate_hashes(file_path)
        
        if current_hashes is None:
            print("Status: ERROR (Could not read file)")
            print("-" * 60)
            continue
        
        md5_match = current_hashes["md5"] == data["md5"]
        sha256_match = current_hashes["sha256"] == data["sha256"]
        
        if md5_match and sha256_match:
            print("Status: UNCHANGED")
        else:
            print("Status: MODIFIED")
            print(f"  Original MD5   : {data['md5']}")
            print(f"  Current  MD5   : {current_hashes['md5']}")
            print(f"  Original SHA256: {data['sha256']}")
            print(f"  Current  SHA256: {current_hashes['sha256']}")
        
        print(f"Baseline Timestamp: {data['timestamp']}")
        print("-" * 60)


def show_baseline():
    """Display current baseline"""
    baseline = load_baseline()
    
    if not baseline:
        print("\n[!] Baseline is empty.")
        return
    
    print("\n=== Current Baseline ===")
    for path, data in baseline.items():
        print(f"\nPath     : {path}")
        print(f"MD5      : {data['md5']}")
        print(f"SHA-256  : {data['sha256']}")
        print(f"Timestamp: {data['timestamp']}")
    print()


def main():
    while True:
        print("\n" + "="*50)
        print("       FILE INTEGRITY CHECKER")
        print("="*50)
        print("1. Add files to baseline")
        print("2. Check file integrity")
        print("3. Show current baseline")
        print("4. Exit")
        print("="*50)
        
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == "1":
            add_files_to_baseline()
        elif choice == "2":
            check_integrity()
        elif choice == "3":
            show_baseline()
        elif choice == "4":
            print("\nExiting... Goodbye!")
            break
        else:
            print("\n[!] Invalid choice. Please try again.")


if __name__ == "__main__":
    main()