import sys
import os
from enum import Enum
from pathlib import Path
import re
# 從 log4py 模組中匯入 logger_factory 和其常數
from utils.log4py import logger_factory

# 設定使用 file logger，並指定 log 檔案名稱為 "foldermate.log"
logger = logger_factory(logger_factory.FILE_LOGGER, "foldermate.log")

class FolderStatus(Enum):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"

def clean_folder_name(name: str) -> str:
    """移除任何 [todo] / [doing] / [done] 前綴"""
    return re.sub(r"^\[(todo|doing|done)\]\s*", "", name, flags=re.IGNORECASE)

def apply_status(folder_path: Path, status: FolderStatus):
    """
    對指定的資料夾路徑套用新的狀態前綴。
    """
    parent = folder_path.parent
    if not folder_path.exists() or not folder_path.is_dir():
        logger.error(f"❌ 無效路徑：{folder_path}")
        return

    original_name = folder_path.name
    cleaned_name = clean_folder_name(original_name)
    new_name = f"[{status.value}] {cleaned_name}"
    new_path = parent / new_name

    if folder_path == new_path:
        logger.info(f"✅ 已是目標狀態：{folder_path.name}")
        return

    try:
        folder_path.rename(new_path)
        logger.info(f"✅ 成功：{original_name} → {new_name}")
    except Exception as e:
        logger.error(f"⚠️ 失敗：{original_name} → {e}")

def main():
    """
    從命令列參數取得狀態和資料夾路徑，然後套用狀態。
    """
    if len(sys.argv) < 3:
        logger.error("用法：python set_folder_status.py 狀態 路徑1 路徑2 ...")
        logger.error("例如：python set_folder_status.py todo \"C:\\folder1\" \"C:\\folder2\"")
        sys.exit(1)

    status_arg = sys.argv[1].lower()
    try:
        status = FolderStatus(status_arg)
    except ValueError:
        logger.error(f"❌ 無效狀態：{status_arg}，可用值為 {[s.value for s in FolderStatus]}")
        sys.exit(1)

    for path_str in sys.argv[2:]:
        folder = Path(path_str)
        apply_status(folder, status)

if __name__ == "__main__":
    main()
