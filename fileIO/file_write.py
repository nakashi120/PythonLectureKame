with open("writing_file.txt", mode="w") as f:
    f.write("You can write contents here\nuse 'backslash' to break the row")
    f.write("new write() doesn't break row")

    print("You can add a new row using 'file' parameter", file=f)
