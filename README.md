# TLDR

## Preview:
<img width="2559" height="1364" alt="image" src="https://github.com/user-attachments/assets/0d17c6c6-f3f9-4bb5-9164-0b0beaea2bcf" />

## Windows Tutorial:
1. Download Zip
2. Extract
3. Make new notepad
```
Set WshShell = CreateObject("WScript.Shell")

' 1. Arahkan ke folder project Python kamu
' Pastikan path ini sesuai dengan lokasi folder app.py kamu disimpan
WshShell.CurrentDirectory = "D:\008_ExpenseTracker\python-tracker"

' 2. Jalankan server Python (Flask) secara tersembunyi (angka 0 artinya Hide)
WshShell.Run "cmd /c python app.py", 0, False

' 3. Beri waktu 3 detik agar server Python loading dan siap menerima koneksi
WScript.Sleep 2500

' 4. Buka browser otomatis ke alamat lokal
WshShell.Run "msedge.exe --app=http://localhost:3000", 1, False
```
Save As, Desktop Directory, Rename "MySpending.vbs", Save as Type "All Files", Right Click, Show More Option, Send to, Dekstop (Create Shortcut), Properties (Custom Icon).
4. Left Click, Wait 3 Secs.
5. Click Shutdown Button on the Top Right Corner.
