@echo off
chcp 65001 >nul
setlocal

echo Removing FolderMate context menu entries...

@REM =========================================================
@REM 移除 "變更狀態前綴標籤" 右鍵選單 (HKCU = current user)
@REM =========================================================
for %%S in (todo doing done) do (
    reg delete "HKCU\Software\Classes\Directory\shell\FolderMate_%%S" /f >nul 2>&1
    if errorlevel 1 (
        echo [INFO] Entry not found or already removed: %%S
    ) else (
        echo [OK] Removed context menu entry: %%S
    )
)

@REM =========================================================
@REM 移除 "複製資料夾名稱" 右鍵選單 (HKCU = current user)
@REM =========================================================
reg delete "HKCU\Software\Classes\Directory\shell\FolderMate_CopyFolderName" /f >nul 2>&1
if errorlevel 1 (
    echo [INFO] Entry not found or already removed: FolderMate_CopyFolderName
) else (
    echo [OK] Removed context menu entry: FolderMate_CopyFolderName
)

echo.
echo [DONE] FolderMate uninstallation complete.
pause
