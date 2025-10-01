"""
 *  author: realpratz [Pratyush Priyadarshi]
"""

import time
import datetime
import requests
import os
import tkinter as tk
from dotenv import load_dotenv
import xml.etree.ElementTree as ET
import requests

# ---------- Load ENV File ----------
load_dotenv()
version = "0.2"

username = os.getenv("id")
password = os.getenv("password")
timeout = int(os.getenv("timeout"))
save_xml = bool(int(os.getenv("save_xml")))
on_start = bool(int(os.getenv("on_start")))

# ---------- Utilities ----------
def save_env(data):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, ".env")

    with open(filename, "w") as f:
        for k, v in data.items():
            f.write(f"{k}={v}\n")

def parse_status(xml_text):
    try:
        root = ET.fromstring(xml_text)
        st = root.findtext("status")
        msg = root.findtext("message")
        tree = ET.ElementTree(root)

        if save_xml_var.get():
            script_dir = os.path.dirname(os.path.abspath(__file__))
            xml_dir = os.path.join(script_dir, "XML")
            os.makedirs(xml_dir, exist_ok=True)
            time_str = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
            filename = os.path.join(xml_dir, f"LiTE-{time_str}.xml")
            tree.write(filename, encoding="utf-8", xml_declaration=True)

        return st, msg
    except ET.ParseError:
        return None, None

# ---------- Login/Logout ----------
def login(username, password, timeout=10):
    url = "http://172.16.0.30:8090/login.xml"

    data = {
        "mode": "191",
        "username": username,
        "password": password,
        "a": str(int(time.time() * 1000)),
        "producttype": 0
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "LiTE/auto_login"
    }

    s = requests.Session()
    r = s.post(url, data=data, headers=headers, timeout=timeout)

    if not on_start:
        status, message = parse_status(r.text)
        message = message.replace("{username}", username)
        return status, message

def logout(username, timeout=10):
    url = "http://172.16.0.30:8090/logout.xml"

    data = {
        "mode": "193",
        "username": username,
        "a": str(int(time.time() * 1000)),
        "producttype": 0
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "LiTE/auto_logout"
    }

    s = requests.Session()
    r = s.post(url, data=data, headers=headers, timeout=timeout)

    status, message = parse_status(r.text)
    return status, message

# ---------- Button Logic ----------
def pressLogin():
    try:
        status, msg = login(username_entry.get(), password_entry.get(), int(timeout_entry.get()))

        st_textbox.delete(1.0, tk.END)
        st_textbox.insert(tk.END, status)

        msg_textbox.delete(1.0, tk.END)
        msg_textbox.insert(tk.END, msg)

    except requests.exceptions.RequestException as e:
        st_textbox.delete(1.0, tk.END)
        st_textbox.insert(tk.END, "requests.exceptions.RequestException")

        msg_textbox.delete(1.0, tk.END)
        msg_textbox.insert(tk.END, str(e))

def pressLogout():
    status, msg = logout(username_entry.get(), int(timeout_entry.get()))

    st_textbox.delete(1.0, tk.END)
    st_textbox.insert(tk.END, status)

    msg_textbox.delete(1.0, tk.END)
    msg_textbox.insert(tk.END, msg)

def pressSave():
    save_env({
        "id": username_entry.get(),
        "password": password_entry.get(),
        "timeout": timeout_entry.get(),
        "save_xml": 1 if save_xml_var.get() else 0,
        "on_start": 1 if run_startup_var.get() else 0
    })

# ---------- GUI Setup ----------
if not on_start:
    root = tk.Tk()
    root.title(f"LiTE- LAN integration & Tracking Easer v{version}")
    root.geometry("500x400")
    root.resizable(False, False)

    cred_frame = tk.Frame(root)
    cred_frame.pack(pady=10)

    username_label = tk.Label(cred_frame, text="Username:")
    username_label.grid(row=0, column=0, padx=5, sticky="e")
    username_entry = tk.Entry(cred_frame)
    username_entry.grid(row=0, column=1, padx=5)
    username_entry.insert(0, username)

    password_label = tk.Label(cred_frame, text="Password:")
    password_label.grid(row=0, column=2, padx=5, sticky="e")
    password_entry = tk.Entry(cred_frame, show="*")
    password_entry.grid(row=0, column=3, padx=5)
    password_entry.insert(0, password)

    checkbox_frame = tk.Frame(root)
    checkbox_frame.pack(pady=10)

    save_xml_var = tk.BooleanVar(value=save_xml)
    save_xml_checkbox = tk.Checkbutton(checkbox_frame, text="Save XML file", variable=save_xml_var)
    save_xml_checkbox.grid(row=0, column=0, padx=10)

    run_startup_var = tk.BooleanVar(value=on_start)
    run_startup_checkbox = tk.Checkbutton(checkbox_frame, text="Login on Startup/Background Login", variable=run_startup_var)
    run_startup_checkbox.grid(row=0, column=1, padx=10)

    timeout_label = tk.Label(root, text="Timeout (seconds):")
    timeout_label.pack(pady=(10, 0))
    timeout_entry = tk.Entry(root)
    timeout_entry.pack(pady=5)
    timeout_entry.insert(0, timeout)

    st_label = tk.Label(root, text="Status:")
    st_label.pack(pady=(10, 0))
    st_textbox = tk.Text(root, height=1, width=60)
    st_textbox.pack(pady=5)

    msg_label = tk.Label(root, text="Message:")
    msg_label.pack(pady=(10, 0))
    msg_textbox = tk.Text(root, height=3, width=60)
    msg_textbox.pack(pady=5)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=15)

    login_button = tk.Button(button_frame, text="Login", width=10, command=pressLogin)
    login_button.pack(side=tk.LEFT, padx=5)

    logout_button = tk.Button(button_frame, text="Logout", width=10, command=pressLogout)
    logout_button.pack(side=tk.LEFT, padx=5)

    save_button = tk.Button(button_frame, text="Save", width=10, command=pressSave)
    save_button.pack(side=tk.LEFT, padx=5)

    credits_label = tk.Label(root, text="by Pratyush Priyadarshi (f20250270H)", font=("Arial", 8), fg="gray")
    credits_label.pack(side=tk.BOTTOM, pady=5)

# ---------- Switching Modes ----------
if on_start:
    login(username, password, timeout=10)
else:
    root.mainloop()