import sys
import os
from enum import Enum
from pathlib import Path
import re
from datetime import datetime

class FolderStatus(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

def clean_folder_name(name: str) -> str:
    """移除任何 [todo] / [doing] / [done] 前綴"""
    return re.sub(r"^\[(todo|doing|done)\]\s*", "", name, flags=re.IGNORECASE)

def log_message(log_folder: Path, message: str):
    """將訊息寫入 log 檔（儲存在指定資料夾內）"""
    log_path = log_folder / "foldermate.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def apply_status(folder_path: Path, status: FolderStatus):
    parent = folder_path.parent
    if not folder_path.exists() or not folder_path.is_dir():
        log_message(parent, f"❌ 無效路徑：{folder_path}")
        return

    original_name = folder_path.name
    cleaned_name = clean_folder_name(original_name)
    new_name = f"[{status.value}] {cleaned_name}"
    new_path = parent / new_name

    if folder_path == new_path:
        log_message(parent, f"✅ 已是目標狀態：{folder_path.name}")
        return

    try:
        folder_path.rename(new_path)
        log_message(parent, f"✅ 成功：{original_name} → {new_name}")
    except Exception as e:
        log_message(parent, f"⚠️ 失敗：{original_name} → {e}")

def main():
    if len(sys.argv) < 3:
        print("用法：python set_folder_status.py 狀態 路徑1 路徑2 ...")
        print("例如：python set_folder_status.py todo \"C:\\folder1\" \"C:\\folder2\"")
        sys.exit(1)

    status_arg = sys.argv[1].lower()
    try:
        status = FolderStatus(status_arg)
    except ValueError:
        print(f"❌ 無效狀態：{status_arg}，可用值為 {[s.value for s in FolderStatus]}")
        sys.exit(1)

    for path_str in sys.argv[2:]:
        folder = Path(path_str)
        apply_status(folder, status)

if __name__ == "__main__":
    main()
