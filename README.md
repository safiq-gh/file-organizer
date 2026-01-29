# File Organizer

A modular Python CLI tool for organizing files in a directory based on file type.

## Current Status

**Version:** v2.1  
**Stage:** Stable refactor with tests  
**Development Phase:** Phase 2 Completed!

## Features Implemented

- Scan directories for files
- Optional recursive scanning
- Excludes hidden files and organizer output directories
- Group files into:
  - Images
  - Docs
  - Others
- Move files into target directories safely
- Dry-run mode
- Command-line interface (argparse)
- Unit tests using pytest

## Project Structure

- `scanner` — directory traversal logic (class-based, recursive-safe)
- `grouper` — file grouping logic
- `mover` — file relocation logic
- `cli` — command-line argument parsing
- `fsort.py` — entry point
- `tests/` — pytest-based test suite

## Usage

```bash
python fsort.py --path /path/to/directory
```
## Optional Flags

``` bash
--recursive   Scan subdirectories
--dry-run     Preview changes without moving files
```
