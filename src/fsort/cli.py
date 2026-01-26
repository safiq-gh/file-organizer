from pathlib import Path
from fsort import scanner, grouper, mover, preview, args

def main():
    args_ns = args.parse_args()
    path = Path(args_ns.path)

    try:
        files = scanner.scan_directory(path, args_ns.recursive)
    except FileNotFoundError:
        print("Invalid path!")
        return
    except PermissionError:
        print("Access denied!")
        return

    groups = grouper.group_files(files)

    if args_ns.dry_run:
        empty = sum(1 for d in groups if not groups[d])
        if empty < len(groups):
            print(">>> DRY RUN MODE: No files will be moved.")
            preview.preview_moves(groups)
        else:
            print("No preview to show. Files already ordered.")
    else:
        mover.apply_moves(groups, path)

