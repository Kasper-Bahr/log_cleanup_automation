# Log File Cleanup Automation

A Python automation script for cleaning up old `.log` files.  
Useful for developers, sysadmins, and anyone managing cluttered log directories.

---

## Features

- Recursively scans specified folders
- Detects `.log` files older than N days
- Deletes or archives them (by date)
- Automatically generates a detailed report (terminal + .txt)
- Fully CLI-based via `argparse`
- Ready to integrate with automation tools (cron, Task Scheduler, etc.)

---

## Quick Start

```
python cleanup.py <folder_path> [--days N] [--archive] [--report]
```

### Example

```
python cleanup.py test_logs --days 30 --archive --report
```

This command archives all `.log` files older than 30 days from `test_logs/`  
and generates a report saved as `.txt`.

---

## Report Output

When using `--report`, a file like:

```
cleanup_report_2025-07-10.txt
```

is saved to the root folder with content like:

```
--- Cleanup Report (2025-07-10 13:33:59) ---
Deleted: 0 files
Archived: 1 files
[ARCHIVED] test_logs\example_old.log
----------------------
```

---

## How It Works

1. Scans the given folder (and subfolders)
2. Finds `.log` files older than the specified number of days
3. Archives (or deletes) them
4. Optionally writes a summary report to a timestamped `.txt` file

---

## Tech Stack

- Python 
- argparse
- os
- datetime
- shutil
- Developed in Visual Studio Code

---

## License

This project is licensed under the MIT License.

---

Created by [Kasper-Bahr] Kasperbahr@wp.pl
