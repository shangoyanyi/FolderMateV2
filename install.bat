@echo off
setlocal

REM Get the folder where this script is located
set "BASEDIR=%~dp0"
set "TARGETDIR=%LOCALAPPDATA%\Programs\FolderMate"
set "PYEXE=%LOCALAPPDATA%\Programs\Python\Python312\pythonw.exe"

REM Create target directory if it does not exist
if not exist "%TARGETDIR%" (
    mkdir "%TARGETDIR%"
)

REM Copy all files to the target directory
xcopy /E /Y "%BASEDIR%*" "%TARGETDIR%" >nul

REM Register right-click context menu items (HKCU = current user)
for %%S in (todo doing done) do (
    reg add "HKCU\Software\Classes\Directory\shell\FolderMate_%%S" /ve /d "FolderMate: [%%S]" /f
    reg add "HKCU\Software\Classes\Directory\shell\FolderMate_%%S" /v "Icon" /d "\"%TARGETDIR%\icon.ico\"" /f
    reg add "HKCU\Software\Classes\Directory\shell\FolderMate_%%S\command" /ve /d "\"%PYEXE%\" \"%TARGETDIR%\set_folder_status.py\" %%S \"%%1\"" /f
)

echo.
echo [OK] FolderMate installed and context menu registered.
echo [PATH] Script installed to: %TARGETDIR%
echo [PYTHON] Python executable: %PYEXE%
pause
