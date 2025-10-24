# LiTE

Automating LAN related utilities one step at a time. (**It's still WIP, it's not just for LAN autologin**)

## Requirements

- **Python**: Ensure Python is installed on your system.
- **Libraries**: Install python packages that might not be installed bydefault (install requirements.txt)
## How to Use? (Windows)

1. **Clone the Repository**
2. **Navigate to the directory and install Dependencies**
```
pip install -r requirements.txt
```
3. **Create a `.env` file in the same directory as the `LiTE.py` file**:
```
id=f2025XXXX
password=Bits$XXXXX
timeout=10
save_xml=1
on_start=1
```
4. **Write a .bat file to run it on startup**:
```
python "<path of LiTE.py>"
```
Save it in- ```C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```
## How to Use? (Linux)

1. **Clone the Repository**
2. **Navigate to the directory and create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install Dependencies in the virtual environment**
```bash
pip install -r requirements.txt
```

Depending on your linux distribution, you might have to seperately install Tkinter.
```bash
sudo pacman -Syu tk #Arch / Manjaro
sudo apt install python3-tk #Ubuntu / Debian
sudo dnf install python3-tkinter #Fedora / RedHat
```
4. **Create a `.env` file in the same directory as the `LiTE.py` file**:
```
id=f2025XXXX
password=Bits$XXXXX
timeout=10
save_xml=1
on_start=1
```
5. **Setup an autostart `.desktop` file to launch at login**:
```bash
mkdir -p ~/.config/autostart
nano ~/.config/autostart/LiTE.desktop
```

Write this into the `.desktop` file:
```
[Desktop Entry]
Type=Application
Name=LiTE
Comment=Launch LiTE
Exec=.../LiTE/venv/bin/python .../LiTE/LiTE.py
X-GNOME-Autostart-enabled=true
Terminal=false
```
Replace ```.../``` with your actual path and reboot.

Now everytime on startup, the script will read the `.env` file preferences set by you automatically log you into LAN
---
