import sys
import os
from pathlib import Path
from datetime import datetime
import pyperclip # 新增這行
import locale
# 為了避免在 Windows 上出現亂碼，手動設定編碼
# 這行確保 Python 使用與系統一致的編碼
locale.setlocale(locale.LC_ALL, 'C') 

def log_message(log_folder: Path, message: str):
    """將訊息寫入 log 檔（儲存在指定資料夾內）"""
    log_path = log_folder / "foldermate.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # 使用 'utf-8-sig' 編碼以確保 BOM 標記，避免某些編輯器讀取亂碼
        with open(log_path, "a", encoding="utf-8-sig") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception as e:
        # 如果寫入日誌失敗，則退回到 print
        print(f"寫入日誌時發生錯誤: {e}")
        print(f"[{timestamp}] {message}")

def copy_to_clipboard(text: str, log_folder: Path):
    """將文字複製到剪貼簿並記錄結果"""
    try:
        pyperclip.copy(text) # 使用 pyperclip 函式
        log_message(log_folder, f'✅ 成功複製 "{text}" 到剪貼簿。')
    except Exception as e:
        log_message(log_folder, f'⚠️ 複製到剪貼簿時發生錯誤: {e}')

def main():
    """從命令列參數取得資料夾路徑，並將其名稱複製到剪貼簿"""
    if len(sys.argv) < 2:
        # 如果沒有提供參數，沒有資料夾路徑可以確定 log 存放位置，直接印出錯誤並退出
        print("錯誤：請提供資料夾路徑作為參數。")
        sys.exit(1)

    folder_path_str = sys.argv[1]
    folder_path = Path(folder_path_str)
    
    # 檢查路徑是否存在且為資料夾
    if not folder_path.is_dir():
        # 在無法取得父目錄的情況下，將日誌寫入當前目錄
        log_folder = Path.cwd()
        log_message(log_folder, f"❌ 錯誤：'{folder_path_str}' 不是一個有效的資料夾路徑。")
        sys.exit(1)
        
    log_folder = folder_path.parent

    # 提取資料夾名稱
    folder_name = os.path.basename(folder_path_str)
    
    # 複製資料夾名稱到剪貼簿並記錄
    copy_to_clipboard(folder_name, log_folder)

if __name__ == "__main__":
    main()