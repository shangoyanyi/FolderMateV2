import sys
import os
from pathlib import Path
from datetime import datetime
import pyperclip
import locale

# 從 log4py 模組中匯入 logger_factory 和其常數
from utils.log4py import logger_factory

# 設定使用 file logger，並指定 log 檔案名稱為 "foldermate.log"
logger = logger_factory(logger_factory.FILE_LOGGER, "foldermate.log")

# 為了避免在 Windows 上出現亂碼，手動設定編碼
# 這行確保 Python 使用與系統一致的編碼
locale.setlocale(locale.LC_ALL, 'C')

def copy_to_clipboard(text: str):
    """將文字複製到剪貼簿並記錄結果"""
    try:
        pyperclip.copy(text) # 使用 pyperclip 函式
        logger.info(f'✅ 成功複製 "{text}" 到剪貼簿。')
    except Exception as e:
        logger.error(f'⚠️ 複製到剪貼簿時發生錯誤: {e}')

def main():
    """從命令列參數取得資料夾路徑，並將其名稱複製到剪貼簿"""
    if len(sys.argv) < 2:
        # 如果沒有提供參數，直接印出錯誤並退出
        logger.error("錯誤：請提供資料夾路徑作為參數。")
        sys.exit(1)

    folder_path_str = sys.argv[1]
    folder_path = Path(folder_path_str)
    
    # 檢查路徑是否存在且為資料夾
    if not folder_path.is_dir():
        logger.error(f"❌ 錯誤：'{folder_path_str}' 不是一個有效的資料夾路徑。")
        sys.exit(1)
        
    # 提取資料夾名稱
    folder_name = os.path.basename(folder_path_str)
    
    # 複製資料夾名稱到剪貼簿並記錄
    copy_to_clipboard(folder_name)

if __name__ == "__main__":
    main()
