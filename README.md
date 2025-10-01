# LiTE

Automating LAN related utilities one step at a time

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

Now everytime on startup, the script will read the `.env` file preferences set by you automatically log you into LAN
---
