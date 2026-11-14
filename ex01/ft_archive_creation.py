import sys
import typing

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        filename: str = sys.argv[1]

        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{filename}'")

        file_obj: typing.IO[str] | None = None
        try:
            file_obj = open(filename, "r")
        except Exception as ERROR:
            print(f"Error opening file '{filename}': {ERROR}")

        if file_obj is not None:
            print("---")
            print()
            content: str = file_obj.read()
            print(content, end="")
            print()
            print("---")
            file_obj.close()
            print(f"File '{filename}' closed.")

            archived: str = ""
            i: int = 0
            while i < len(content):
                if content[i] == "\n":
                    archived += "#\n"
                else:
                    archived += content[i]
                i += 1

            if len(content) > 0 and content[len(content) - 1] != "\n":
                archived += "#"

            print("Transform data:")
            print("---")
            print()
            print(archived, end="")
            print()
            print("---")

            new_filename: str = input("Enter new file name (or empty): ")
            if new_filename == "":
                print("Not saving data.")
            else:
                try:
                    new_file_obj: typing.IO[str] = open(new_filename, "w")
                    new_file_obj.write(archived)
                    new_file_obj.close()
                    print(f"Saving data to '{new_filename}'")
                    print(f"Data saved in file '{new_filename}'.")
                except Exception as ERROR:
                    print(f"Error writing to file '{new_filename}': {ERROR}")
