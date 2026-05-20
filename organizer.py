import os

def main():

    # ask user for directory path
    path = input("Enter path: ")
    try:
        # scan directory
        files = scan_directory(path)
        #print(files)
    except FileNotFoundError:
        print("Invalid path!")
        return
    except PermissionError:
        print("Access denied!")
        return

    # group files
    groups = group_files(files)
    #print(groups)

    # preview planned moves
    pc = 0
    for directory in groups:
        if len(groups[directory]) == 0:
            pc += 1
    if pc < len(groups):
        preview_moves(groups)
    else:
        print("No preveiw to show!. Files are already in correct order.")
        return
    # ask for confirmation
    confirmation = input("Confirm to change(y/n): ").lower()
    if confirmation == "y":
        # apply moves if confirmed
        apply_moves(groups, path)
    else:
        return

def scan_directory(path):
    files = []
    for fildir in os.listdir(path):
        full_path = os.path.join(path, fildir)
        if os.path.isfile(full_path) and fildir != "organizer.py" and not fildir.startswith("."):
            files.append(full_path)
    return files

def group_files(files):

    group_rules = {
                "Images": [".jpg", ".png", ".jpeg", ".gif"],
                "Docs": [".pdf", ".docx", ".txt"]
                }

    group = {
            "Images": [],
            "Docs": [],
            "Others": []
            }

    for file in files:
        file_name = os.path.basename(file)
        name, ext = os.path.splitext(file_name)
        ext = ext.lower()
        if ext in group_rules['Images']:
            group['Images'].append(file)
        elif ext in group_rules['Docs']:
            group['Docs'].append(file)
        else:
            group['Others'].append(file)
    return group

def preview_moves(groups):
    for keys in groups:
        if len(groups[keys]) == 0:
            continue
        print(f"{keys}/")
        for values in groups[keys]:
            name = os.path.basename(values)
            print(f"  {name}")
        print(" ")

def apply_moves(groups, base_path):
    for directory in groups:
        full_path = os.path.join(base_path, directory)
        os.makedirs(full_path, exist_ok=True)
        for src in groups[directory]:
                dst = os.path.join(full_path, os.path.basename(src))
                if os.path.exists(dst):
                    continue
                else:
                    os.rename(src, dst)
main()
