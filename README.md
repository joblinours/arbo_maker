# Test Directory Tree Generator

This Python script generates a file and folder tree for testing, with customizable parameters to control depth, number of files, number of subfolders, and more.

## Description

The script creates a directory structure with files within these directories, according to specifications defined by the user. Templates for file names, folder names, and file content can be defined. The script also supports constraints on the total number of files and folders created.

### Features

- Creates a directory tree with files at different depth levels.
- Customizable parameters for the number of files, subfolders, and depth.
- Option to set constraints on the total number of files and folders.
- Displays the generated tree in text form similar to the `tree` command.

## Prerequisites

The script requires Python 3.6 or a later version.

## Installation

Clone the repository and install the necessary dependencies (if needed):

```bash
git clone https://github.com/joblinours/arbo_maker.git
cd arbo_maker
```

No external dependencies are required.

## Usage

### Command syntax

```bash
python arbo_maker.py <root_folder_path> [options]
```

### Options

- `base_path`: The root folder path where the tree will be created. (Required)
- `--min_depth`: Minimum depth of the tree (default is `1`).
- `--max_depth`: Maximum depth of the tree (default is `5`).
- `--min_files`: Minimum number of files per folder (default is `1`).
- `--max_files`: Maximum number of files per folder (default is `5`).
- `--min_dirs`: Minimum number of subfolders per folder (default is `1`).
- `--max_dirs`: Maximum number of subfolders per folder (default is `3`).
- `--file_name`: Template for file names (default is `file_{index}.txt`).
- `--subdir_name`: Template for subfolder names (default is `subdir_{index}`).
- `--file_content`: Template for file content (default is `This is the content of {file_name}.`).
- `--min_files_total`: Minimum total number of files.
- `--max_files_total`: Maximum total number of files.
- `--exact_files_total`: Exact total number of files.
- `--min_dirs_total`: Minimum total number of folders.
- `--max_dirs_total`: Maximum total number of folders.
- `--exact_dirs_total`: Exact total number of folders.
- `--tree`: Displays the full tree after creation.

### Example Usage

```bash
python generate_tree.py /path/to/directory --max_depth 3 --min_files 2 --max_files 5 --tree
```

This will generate a tree with a maximum depth of 3, between 2 and 5 files per folder, and display the tree at the end.

### In Progress

The script did not integrate correctly with the `--exact_files_total` and `--exact_dirs_total` options, fixes are underway.

### Result

The script generates a directory structure and creates files within it. Once the tree is completed, the script displays a summary with the total number of files and folders created, and if the `--tree` option is enabled, it shows the tree similarly to the `tree` command.

---

### License

This project is licensed under the [MIT](LICENSE) license.
