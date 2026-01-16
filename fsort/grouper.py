import os

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

