import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        for i in range(1, len(sys.argv)):
            filename = sys.argv[i]
            print(f"Accessing file '{filename}'")

            try:
                file_obj = open(filename, "r")
            except Exception as ERROR:
                print(f"Error opening file '{filename}': {ERROR}")
                continue

            print("---\n")
            content = file_obj.read()
            print(content, end="")
            print("\n---")

            file_obj.close()
            print(f"File '{filename}' closed.")
