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

## How to Use?

1. **Clone the Repository**
2. **Write a .bat file to run it on startup**:
```
python "<directory of LiTE.py"
```
Save it in- C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

Now everytime on startup, the script will read the `.env` file preferences set by you automatically log you into LAN
- **Packaging Issues**: Ensure the `--add-data` option is correctly specified when running `pyinstaller`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
