import argparse 

def parse_args():
    parser = argparse.ArgumentParser(description="File Organizer")
    parser.add_argument("--path", required=True, type=str, help="Path to the folder you want to organize.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    parser.add_argument("--recursive", action="store_true", help="Scan the directories and sub-directories recursively.")
    return parser.parse_args()
