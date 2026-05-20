from pathlib import Path
from fsort import scanner, grouper, mover, preview, args


def show_banner():
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    banner = r"""
███████╗██╗██╗     ███████╗███████╗ ██████╗ ██████╗ ████████╗
██╔════╝██║██║     ██╔════╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝
█████╗  ██║██║     █████╗  ███████╗██║   ██║██████╔╝   ██║
██╔══╝  ██║██║     ██╔══╝  ╚════██║██║   ██║██╔══██╗   ██║
██║     ██║███████╗███████╗███████║╚██████╔╝██║  ██║   ██║
╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝

        FileSort — Organize Your Files
"""
    print(f"{CYAN}{banner}{RESET}")

def main():
    show_banner()  # <-- banner runs immediately

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

