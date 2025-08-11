@echo off
chcp 65001 >nul
setlocal

@REM Get the folder where this script is located
set "BASEDIR=%~dp0"
set "TARGETDIR=%LOCALAPPDATA%\Programs\FolderMate"
set "PYEXE=%LOCALAPPDATA%\Programs\Python\Python312\pythonw.exe"

@REM Create target directory if it does not exist
if not exist "%TARGETDIR%" (
    mkdir "%TARGETDIR%"
)

@REM Copy all files to the target directory
xcopy /E /Y "%BASEDIR%*" "%TARGETDIR%" >nul


@REM 安裝python依賴套件
echo [INFO] Installing dependencies...
:: "%PYEXE%" -m pip install --upgrade pip
"%PYEXE%" -m pip install -r "%BASEDIR%\requirements.txt"


@REM =========================================================
@REM 註冊 "變更狀態前綴標籤" 右鍵選單 (HKCU = current user)
@REM =========================================================
echo.
echo 註冊 "FolderMate: [todo/doing/done]" 右鍵選單...

for %%S in (todo doing done) do (
    reg add "HKCU\Software\Classes\Directory\shell\FolderMate_%%S" /ve /d "FolderMate: [%%S]" /f
    reg add "HKCU\Software\Classes\Directory\shell\FolderMate_%%S" /v "Icon" /d "\"%TARGETDIR%\icon3.ico\"" /f
    reg add "HKCU\Software\Classes\Directory\shell\FolderMate_%%S\command" /ve /d "\"%PYEXE%\" \"%TARGETDIR%\set_folder_status.py\" %%S \"%%1\"" /f
)

echo "FolderMate: [todo/doing/done]" 右鍵選單已設定完成。


@REM =========================================================
@REM 註冊 "複製資料夾名稱" 右鍵選單 (HKCU = current user)
@REM =========================================================
echo.
echo 註冊 "FolderMate: 複製資料夾名稱" 右鍵選單...

reg add "HKCU\Software\Classes\Directory\shell\FolderMate_CopyFolderName" /ve /d "FolderMate: 複製資料夾名稱" /f
reg add "HKCU\Software\Classes\Directory\shell\FolderMate_CopyFolderName" /v "Icon" /d "\"%TARGETDIR%\icon3.ico\"" /f
reg add "HKCU\Software\Classes\Directory\shell\FolderMate_CopyFolderName\command" /ve /d "\"%PYEXE%\" \"%TARGETDIR%\copy_folder_name.py\" \"%%1\"" /f

echo "FolderMate: 複製資料夾名稱" 右鍵選單已註冊完成。

echo.
echo [OK] FolderMate installed and context menu registered.
echo [PATH] Script installed to: %TARGETDIR%
echo [PYTHON] Python executable: %PYEXE%
pause
