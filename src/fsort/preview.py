def preview_moves(groups):
    for keys in groups:
        if len(groups[keys]) == 0:
            continue
        print(f"{keys}/")
        for values in groups[keys]:
            print(f"  {values.name}")
        print(" ")

