from fsort import scanner,grouper,mover,preview
def main():

    # ask user for directory path
    path = input("Enter path: ")
    try:
        # scan directory
        files = scanner.scan_directory(path)
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
    pc = 0
    for directory in groups:
        if len(groups[directory]) == 0:
            pc += 1
    if pc < len(groups):
        preview.preview_moves(groups)
    else:
        print("No preveiw to show!. Files are already in correct order.")
        return
    # ask for confirmation
    confirmation = input("Confirm to change(y/n): ").lower()
    if confirmation == "y":
        # apply moves if confirmed
        mover.apply_moves(groups, path)
    else:
        return

if __name__ == "__main__":
    main()
