import os
def file_operations():
    original_name = "new file.txt"
    new_name = "renamed file.txt"
    try:
        with open(original_name, "w", encoding = "utf-8") as f:
            f.write("test file")
        print(f"file{original name}creat")
    except IOError as e:
        print(f"error in creat file:{e}")
        return
    try:
        os.rename(original_name, new_name)
        print(f"file{new_name} renamed")
    except OSError as e:
        print(f"error in rename file:{e}")
    try:
        os.remove(new_name)
        print(f"file{new_name} deleted")
    except OSError as e:
        print(f"error in delete file:{e}")
if __name__ == "__main__":
    file_operations()