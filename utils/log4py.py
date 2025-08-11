import logging
from logging.handlers import RotatingFileHandler
import os
from pathlib import Path
import sys

# 定義日誌存放路徑
LOG_FOLDER = Path(os.getenv('LOCALAPPDATA')) / 'Programs' / 'Logs'
LOG_FOLDER.mkdir(parents=True, exist_ok=True)

def _create_formatter():
    """建立日誌格式化器"""
    return logging.Formatter(
        '[%(asctime)s] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def logger_factory(handler_type: str, log_file_name: str = "log4py_default.log"):
    """
    建立並回傳一個已經設定好的日誌記錄器。

    Args:
        handler_type (str): 日誌輸出類型。可以是 logger_factory.FILE_LOGGER 或 logger_factory.CONSOLE_LOGGER。
        log_file_name (str, optional): 日誌檔案名稱，只對 FILE_LOGGER 有效。預設為 "log4py_default.log"。

    Returns:
        logging.Logger: 設定好的日誌記錄器物件。
    """
    if handler_type == logger_factory.FILE_LOGGER:
        logger_name = 'FileLogger'
        log_file_path = LOG_FOLDER / log_file_name
        handler = RotatingFileHandler(
            log_file_path,
            maxBytes=1048576,  # 檔案大小限制為 1MB
            backupCount=5,     # 備份檔案數量
            encoding='utf-8'
        )
    elif handler_type == logger_factory.CONSOLE_LOGGER:
        logger_name = 'ConsoleLogger'
        handler = logging.StreamHandler(sys.stdout)
    else:
        raise ValueError("Invalid handler type specified.")

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 確保 logger 只附加一次 handler
    if not logger.hasHandlers():
        formatter = _create_formatter()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger

# 將常數屬性附加到 factory 函式上，以便於呼叫
logger_factory.FILE_LOGGER = "file"
logger_factory.CONSOLE_LOGGER = "console"