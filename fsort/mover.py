import os

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

