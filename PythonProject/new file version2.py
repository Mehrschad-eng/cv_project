from pathlib import path
def file_operations():
    original = path("new_file.txt")
    renamed = path("renamed file.txt")
    try:
        original.write_text("test file", encoding="utf-8")
        print(f"new file creat: {original}")
    except IOError as e:
        print(f"error in creat: {e}")
    try:
        original.rename(renamed)
        print(f"renamed file creat: {renamed}")
    except FileNotFoundError:
        print("no file found")
    except PermissionError as e:
        print(f"access error{e}")
    try:
        renamed.unlink()
        print(f"file deleted: {renamed}")
    except FileNotFoundError:
        print("there are no files to delete")
    except PermissionError as e:
        print(f"access error{e}")
if __name__ == "__main__":
    file_operations()