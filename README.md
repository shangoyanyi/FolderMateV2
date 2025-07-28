# FolderMateV2

**FolderMate** is a lightweight Windows utility that lets you manage folder statuses (`[todo]`, `[doing]`, `[done]`) directly from the right-click context menu.

This tool is ideal for users who manually organize folders (e.g. for tasks, projects, monthly files) and want a simple way to track status visually without using external tools or spreadsheets.

---

## 🔧 Features

- Right-click any folder to label it with a status: `[todo]`, `[doing]`, or `[done]`
- Automatically removes any previous status label before applying the new one
- Supports multiple selected folders at once
- Logs all operations to `foldermate.log` (stored in the folder’s **parent directory**)
- No admin rights required (uses per-user registry via `HKCU`)

---

## 📁 Files in this project

| File name              | Purpose                                      |
|------------------------|----------------------------------------------|
| `set_folder_status.py` | The Python script that renames folders and logs operations |
| `install.bat`          | Installs the tool: copies files and registers right-click menu |
| `uninstall.bat`        | Removes the registered context menu entries  |
| `README.md`            | Documentation you're reading now             |

---

## 🛠 Installation

1. Make sure Python is installed at: %LOCALAPPDATA%\Programs\Python\Python312\python.exe


If your Python is installed elsewhere, update the path in `install.bat`.

2. Run `install.bat`.

3. Right-click on any folder → choose `FolderMate` → select a status (`[todo]`, `[doing]`, or `[done]`).

---

## 🧼 Uninstallation

1. Run `uninstall.bat`  
2. (Optional) Delete the installation folder at: %LOCALAPPDATA%\Programs\FolderMate\


---

## 🧠 Notes

- Each folder's parent directory will contain a `foldermate.log` file recording all status changes.
- Status is applied by renaming the folder (e.g. `ProjectX` → `[doing] ProjectX`)
- The script safely handles folder names already containing status prefixes

---

## 🔍 Example (optional CLI usage)

```bash
python set_folder_status.py done "D:\Tasks\March" "D:\Tasks\April"
```

Will rename the folders to:

[done] March

[done] April

And log to:

D:\Tasks\foldermate.log


---
## 📎 License
MIT — free for personal and commercial use.