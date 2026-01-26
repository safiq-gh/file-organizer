from pathlib import Path
from fsort import scanner, grouper, mover, preview, cli
def main():

    # ask user for directory path
    args = cli.parse_args()
    path = Path(args.path)
    try:
        # scan directory
        files = scanner.scan_directory(path, args.recursive) 
        #print(files)
    except FileNotFoundError:
        print("Invalid path!")
        return
    except PermissionError:
        print("Access denied!")
        return

    # group files
    groups = grouper.group_files(files)
    #print(groups)

    # preview planned moves
    if args.dry_run:
        pc = 0
        for directory in groups:
            if len(groups[directory]) == 0:
                pc += 1
        if pc < len(groups):
            print(">>> DRY RUN MODE: No files will be moved.")
            preview.preview_moves(groups)
        else:
            print("No preveiw to show!. Files are already in correct order.")
            return
    else:
        # apply moves if confirmed
        mover.apply_moves(groups, path)

if __name__ == "__main__":
    main()
