@echo off
setlocal

echo Removing FolderMate context menu entries...

for %%S in (todo doing done) do (
    reg delete "HKCU\Software\Classes\Directory\shell\FolderMate_%%S" /f >nul 2>&1
    if errorlevel 1 (
        echo [INFO] Entry not found or already removed: %%S
    ) else (
        echo [OK] Removed context menu entry: %%S
    )
)

echo.
echo [DONE] FolderMate uninstallation complete.
pause
