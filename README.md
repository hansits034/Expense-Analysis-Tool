# 💰 MyExpenses - Lightweight Local Expense Tracker

> A minimal, fast, and privacy-first personal finance tracker. Built with Python (Flask) for the backend and pure HTML/JS + Tailwind CSS for the frontend. Runs completely offline like a native desktop app!

## ✨ Features
* **100% Offline & Private:** All your data is saved locally in a `data.json` file. No databases, no cloud tracking.
* **Ultra Lightweight:** Uses less than 5MB of storage compared to heavy Node.js/Electron alternatives.
* **Interactive Dashboard:** Beautiful charts powered by **Chart.js** (Line trend & Donut category).
* **Smart History:** Auto-sorting, search functionality, and specific date filtering.
* **Custom Baseline:** Set your own daily spending limit with visual indicators on the chart.
* **Native App Feel:** Runs in "App Mode" via a VBScript shortcut, hiding the messy terminal window completely.

---

## 📸 Preview
<img width="2559" height="1365" alt="image" src="https://github.com/user-attachments/assets/2db7c13f-a6e0-4f09-9e24-59b65a2adf0d" />

---

## 🛠️ Prerequisites
Before running the application, make sure you have installed:
1. [Python](https://www.python.org/downloads/) (Make sure to check "Add Python to PATH" during installation).
2. **Flask** library. Open your Command Prompt (CMD) and run:
   ```bash
   pip install flask
   ```

## 🚀 Windows Installation & Setup Tutorial

Follow these steps to set up the tracker as a native-looking desktop app on Windows:

### 1. Download the Project

1. Download this repository as a `.zip` file.

2. Extract the `.zip` file to a permanent location on your computer (e.g., `D:\MyProjects\MySpendings`).

### 2. Create the Stealth Launch Script

To run the app without a black CMD window popping up, we will use a VBScript.

1. Open **Notepad**.

2. Copy and paste the code below:

   ```vbscript
   Set WshShell = CreateObject("WScript.Shell")
   
   ' 1. Point to your extracted project folder
   ' CHANGE THIS PATH to where you extracted the project!
   WshShell.CurrentDirectory = "D:\008_ExpenseTracker\python-tracker"
   
   ' 2. Run Python Flask server hidden in the background (0 means Hide)
   WshShell.Run "cmd /c python app.py", 0, False
   
   ' 3. Wait 2.5 seconds for the server to load
   WScript.Sleep 2500
   
   ' 4. Open Microsoft Edge in borderless "App Mode" to localhost
   ' (You can change "msedge.exe" to "chrome.exe" if you prefer Google Chrome)
   WshShell.Run "msedge.exe --app=http://localhost:3000", 1, False
   ```
3. **IMPORTANT:** Change the `WshShell.CurrentDirectory` path in the script above to match the exact folder location where you extracted this project.

4. Click **File > Save As**.

5. Choose your **Desktop** as the save location.

6. Set "Save as type" to **All Files (*.*)**.

7. Name the file **`MyExpenses.vbs`** and click Save.

### 3. Make it Look Professional (Optional)

Let's change the default script icon to a real app icon:

1. Go to your Desktop and **Right-Click** the `MyExpenses.vbs` file.

2. Select **Show more options > Send to > Desktop (create shortcut)**.

3. **Right-Click** the newly created shortcut and select **Properties**.

4. Go to the **Shortcut** tab, click **Change Icon...**, and browse for the `.ico` file inside the `/static` folder of this project.

5. Rename the shortcut to "My Spendings" and hide the original `.vbs` file somewhere safe.

### 4. How to Use

* **To Start:** Simply Double-Click your new Desktop Shortcut. The app will open cleanly without any browser tabs or URL bars.

* **To Exit:** Always click the **Red Power Button** ⏻ on the top right corner of the application to safely kill the local server before closing the window.

## 📂 Data Storage

Your financial records are automatically stored inside the `data.json` file located in the root directory. You can easily back up this file by copying it to your Google Drive or Flash Drive.

