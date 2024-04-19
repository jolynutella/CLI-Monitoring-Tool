# CLI System/Server Monitoring Tool

This is a command-line interface (CLI) tool designed for system administrators and developers to monitor and gather snapshots of system information. The tool captures key metrics such as CPU usage, memory usage, and process statistics at specified intervals.

## Overview

The CLI System/Server Monitoring Tool captures system information and outputs it in a JSON format. It provides flexibility in setting snapshot intervals and defining output file destinations.

## Features

- Collects system information and outputs it in a JSON format.
- Allows customization of snapshot intervals and output file destinations.

## Installation and Usage

### Installation

1. Clone the repository to your local system:
   ```bash
   git clone https://github.com/jolynutella/CLI-Monitoring-Tool.git
2. Navigate to the project directory:
    ```bash
   cd snapshot
3. Install the package using pip:
    ```bash
   pip install .
Alternatively, you can build and install the package from a distribution archive:
```bash
pip install dist/snapshot-0.1.tar.gz
```

### Usage

To capture and save a snapshot of system information, use the following command:
```bash
snapshot -i 30 -f /path/to/output.json
```
Command Options:
- -i, --interval: Specifies the interval (in seconds) between snapshots. Default is 30 seconds.
- -f, --file: Specifies the output file path for the JSON snapshot. The file will contain collected logs and system information.

Example:
```bash
snapshot -i 60 -f /path/to/output.json
```
This command will capture system information every 60 seconds and save it to /path/to/output.json.

## Project Structure
- snapshot/: Main package directory.
- monitor/: Source code for the snapshot tool.
- README.md: Project overview and usage guide.
- setup.py: Configuration for setuptools.

## License
This project is licensed under the MIT License.