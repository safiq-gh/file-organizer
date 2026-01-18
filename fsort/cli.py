# CLI parsing will be added in V1 (argparse)
import argparse 

def parse_args():
    parser = argparse.ArgumentParser(description="File Organizer")
    parser.add_argument("--path", required=True, type=str, help="Path to the folder you want to organize.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
    return parser.parse_args()
