# Source Code File Analyzer

## Description

This project is a Python program that recursively scans a directory containing source code files, identifies the purpose of each file, and generates a brief description of its functionality.

The descriptions are saved in a single text file named **`file_descriptions.txt`**.

## Features

* Accepts a source code directory as input.
* Recursively scans all subdirectories.
* Supports common source code file formats (`.py`, `.c`, `.cpp`, `.java`, `.js`, etc.).
* Generates concise descriptions for each source file.
* Saves the output in the format:

  ```
  Filename: Description
  ```

## Requirements

* Python 3.x

## How to Run

1. Save the program as `source_code_analyzer.py`.
2. Open a terminal in the project directory.
3. Run the program:

```bash
python source_code_analyzer.py
```

4. Enter the path to the source code directory when prompted.
