# LiTE

Automating LAN related utilities one step at a time

## Requirements

- **Python**: Ensure Python is installed on your system.
- **Libraries**: Install python packages that might not be installed bydefault:
```
pip install requests
pip install python-dotenv
pip install tk
```

## How to Use? (Windows)

1. **Clone the Repository**
2. **Create a `.env` file in the same directory as the `.py` file**:
```
id=f2025XXXX
password=Bits$XXXXX
timeout=10
save_xml=1
on_start=1
```
3. **Write a .bat file to run it on startup**:
```
python "<directory of LiTE.py>"
```
Save it in- ```C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```

Now everytime on startup, the script will read the `.env` file preferences set by you automatically log you into LAN
---
