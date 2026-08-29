import os

SOURCE_EXTENSIONS = {
    ".py", ".c", ".cpp", ".cc", ".h", ".hpp",
    ".java", ".js", ".ts", ".cs", ".php",
    ".go", ".rs", ".swift", ".kt", ".rb"
}


def summarize_file(filepath):

    filename = os.path.basename(filepath).lower()

    if "main" in filename:
        return "Contains the main entry point of the application and initializes core modules."

    elif "config" in filename:
        return "Defines configuration settings, constants, and application parameters."

    elif "database" in filename or "db" in filename:
        return "Implements database connection and query execution functionality."

    elif "util" in filename or "helper" in filename:
        return "Provides helper and utility functions used throughout the application."

    elif "model" in filename:
        return "Defines data models and related structures."

    elif "controller" in filename:
        return "Implements application control logic and request handling."

    elif "service" in filename:
        return "Contains business logic and service implementations."

    elif "api" in filename:
        return "Implements API endpoints and request processing."

    elif "test" in filename:
        return "Contains unit tests or testing utilities."

    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read(3000)

        if "if __name__ == '__main__':" in code or 'if __name__ == "__main__":' in code:
            return "Contains the main executable program."

        elif "class " in code:
            return "Defines one or more classes and their associated methods."

        elif "def " in code:
            return "Implements functions that provide application functionality."

        elif "#include" in code:
            return "Contains C/C++ source code implementing application logic."

        elif "import " in code:
            return "Implements program functionality using imported modules."

        else:
            return "Contains source code implementing application functionality."

    except Exception as e:
        return f"Unable to analyze file ({e})"


def scan_directory(directory):

    descriptions = []

    for root, dirs, files in os.walk(directory):
        for file in files:

            extension = os.path.splitext(file)[1].lower()

            if extension in SOURCE_EXTENSIONS:

                filepath = os.path.join(root, file)

                description = summarize_file(filepath)

                descriptions.append((file, description))

    return descriptions


def save_output(descriptions, output_file="file_descriptions.txt"):

    with open(output_file, "w", encoding="utf-8") as f:

        for filename, description in descriptions:
            line = f"{filename}: {description}"
            print(line)
            f.write(line + "\n")


def main():

    print("=" * 60)
    print("SOURCE CODE FILE ANALYZER")
    print("=" * 60)

    directory = input("Enter the path of the source code directory: ").strip()

    if not os.path.isdir(directory):
        print("\nError: Invalid directory path.")
        return

    print("\nScanning directory...")
    descriptions = scan_directory(directory)

    if not descriptions:
        print("\nNo supported source code files found.")
        return

    print(f"\nFound {len(descriptions)} source files.\n")

    save_output(descriptions)

    print("\nAnalysis completed successfully!")
    print("Descriptions saved to 'file_descriptions.txt'")


if __name__ == "__main__":
    main()
