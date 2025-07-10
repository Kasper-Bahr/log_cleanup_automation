import os
import argparse
import datetime
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Log File Cleanup Script")
    parser.add_argument("directory", help="Folder to scan")
    parser.add_argument("--days", type=int, default=30, help="Delete logs older than this many days")
    parser.add_argument("--archive", action="store_true", help="Archive important files instead of deleting")
    parser.add_argument("--report", action="store_true", help="Generate cleanup report")
    return parser.parse_args()

def find_old_logs(folder, days):
    now = datetime.datetime.now()
    threshold = now - datetime.timedelta(days=days)
    old_logs = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".log"):
                path = os.path.join(root, file)
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
                if mtime < threshold:
                    old_logs.append((path, mtime))
    return old_logs

def archive_file(path):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    archive_dir = os.path.join(os.path.dirname(path), "archive", date_str)
    os.makedirs(archive_dir, exist_ok=True)
    shutil.move(path, os.path.join(archive_dir, os.path.basename(path)))

def delete_file(path):
    os.remove(path)

def generate_report(deleted, archived):
    now = datetime.datetime.now()
    report_lines = []
    report_lines.append(f"--- Cleanup Report ({now.strftime('%Y-%m-%d %H:%M:%S')}) ---")
    report_lines.append(f"Deleted: {len(deleted)} files")
    report_lines.append(f"Archived: {len(archived)} files")
    for f in deleted:
        report_lines.append(f"[DELETED] {f}")
    for f in archived:
        report_lines.append(f"[ARCHIVED] {f}")
    report_lines.append("----------------------\n")

    for line in report_lines:
        print(line)

    report_filename = f"cleanup_report_{now.strftime('%Y-%m-%d')}.txt"
    with open(report_filename, "a", encoding="utf-8") as report_file:
        for line in report_lines:
            report_file.write(line + "\n")

def main():
    args = parse_args()
    logs = find_old_logs(args.directory, args.days)
    deleted = []
    archived = []

    for path, _ in logs:
        if args.archive:
            archive_file(path)
            archived.append(path)
        else:
            delete_file(path)
            deleted.append(path)

    if args.report:
        generate_report(deleted, archived)

if __name__ == "__main__":
    main()
