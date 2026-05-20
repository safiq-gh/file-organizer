# File Organizer

A modular, extensible Python CLI tool for organizing files in a directory based on file type. Designed with a strategy-based architecture, strict startup validation, and invariant tests to ensure long-term stability.

## 📋 Project Status

- **Version:** v2.0.0
- **Stage:** Stable
- **Phase:** Phase 2 complete (architecture locked)

Phase 2 introduced:
- Strategy-based grouping
- A centralized strategy registry
- Strict invariants validated at startup
- Invariant tests that lock architectural guarantees

## ✨ Key Features

- 📁 Scan directories for files
- 🔄 Optional recursive traversal
- 🙈 Ignore hidden files and organizer output directories
- 🎯 Group files by type using pluggable strategies
- 🚚 Safely move files into categorized directories
- 👀 Dry-run mode to preview actions
- 💻 Command-line interface (CLI)
- ✅ Unit tests and invariant tests using `pytest`

## 🚀 Entry Point

The application is executed via the Python module entry point:

```bash
python -m fsort --path /path/to/directory
```

The entry point is implemented in:

```
fsort/__main__.py
```

## 🎨 Grouping Model (Strategy-Based)

File grouping is handled via strategies.

**Each strategy:**
- Declares a `group_name`
- Decides whether it accepts a file via `accepts(file)`

**The grouper:**
- Iterates through strategies in order
- Assigns a file to the first accepting strategy
- Requires exactly one fallback strategy

### Built-in Groups

- 🖼️ **Images**
- 📄 **Docs**
- 🎵 **Audio**
- 🎬 **Video**
- 📦 **Archive**
- 📋 **Others** (fallback)

> Adding a new category requires only adding a new strategy—no changes to the grouper logic.

## 🏗️ Architecture Overview

```
fsort/
├── __init__.py
├── __main__.py        # Entry point
├── args.py            # CLI argument definitions
├── cli.py             # CLI orchestration
├── scanner.py         # Directory traversal logic
├── grouper.py         # Strategy-based grouping logic
├── mover.py           # File relocation logic
├── preview.py         # Dry-run preview logic
├── strategies/
│   ├── __init__.py
│   ├── registry.py    # Central strategy registry
│   ├── images.py
│   ├── docs.py
│   ├── audio.py
│   ├── video.py
│   ├── archive.py
│   └── fallback.py
└── tests/
    ├── test_scanner.py
    ├── test_grouper.py
    ├── test_mover.py
    └── test_invariants.py
```

## 📚 Strategy Registry

All grouping strategies are registered centrally in:

```
fsort/strategies/registry.py
```

The grouper dynamically instantiates strategies from this registry at startup.

## 🔒 Enforced Invariants

At startup, the system validates that:
- ✓ Every strategy defines `group_name`
- ✓ `group_name` is a non-empty string
- ✓ Group names are unique
- ✓ Exactly one fallback strategy exists
- ✓ The fallback strategy is last
- ✓ `accepts()` returns a boolean

**Violations cause immediate failure before any file operations occur.**

## 💡 Usage

### Basic Usage

```bash
python -m fsort --path /path/to/directory
```

### Optional Flags

| Flag | Description |
|------|-------------|
| `--recursive` | Scan subdirectories |
| `--dry-run` | Preview changes without moving files |

### Example

```bash
# Organize files in the current directory
python -m fsort --path .

# Recursively organize files with dry-run
python -m fsort --path /downloads --recursive --dry-run

# Actually organize files recursively
python -m fsort --path /downloads --recursive
```

## 🧪 Testing

Run the full test suite:

```bash
pytest
```

The test suite includes:
- Unit tests for scanner, grouper, and mover
- Invariant tests that enforce architectural guarantees

**Invariant tests ensure the system fails fast when misconfigured.**

## 🎯 Design Philosophy

This project prioritizes:
- **Explicit over implicit** behavior
- **Fail-fast validation** at startup
- **Extensibility** without modifying core logic
- **Invariants enforced by tests**, not convention

> The goal is a system that is hard to misuse and safe to extend.

## 📄 License

MIT License

---
