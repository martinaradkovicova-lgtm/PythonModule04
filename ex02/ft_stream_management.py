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
            print(f"[STDERR] Error opening file '{filename}': "
                  f"{ERROR}", file=sys.stderr)

        if file_obj is not None:
            print("---")
            print()
            content: str = file_obj.read()
            print(content, end="")
            print()
            print("---")
            file_obj.close()
            print(f"File '{filename}' closed.")

            transformed: str = ""
            i: int = 0
            while i < len(content):
                if content[i] == "\n":
                    transformed += "#\n"
                else:
                    transformed += content[i]
                i += 1

            if len(content) > 0 and content[len(content) - 1] != "\n":
                transformed += "#"

            print("Transform data:")
            print("---")
            print()
            print(transformed, end="")
            print()
            print("---")

            print("Enter new file name (or empty): ", end="")
            sys.stdout.flush()

            raw_input: str = sys.stdin.readline()
            new_filename = ""
            if len(raw_input) > 0:
                if raw_input[len(raw_input) - 1] == "\n":
                    new_filename = raw_input[:-1]
                else:
                    new_filename = raw_input
            if new_filename == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_filename}'")
                try:
                    new_file_obj: typing.IO[str] = open(new_filename, "w")
                    new_file_obj.write(transformed)
                    new_file_obj.close()
                    print(f"Data saved in file '{new_filename}'.")
                except Exception as ERROR:
                    print(f"[STDERR] Error opening file '{new_filename}': "
                          f"{ERROR}", file=sys.stderr)
                    print("Data not saved.")
