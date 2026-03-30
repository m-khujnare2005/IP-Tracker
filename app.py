import requests
import tkinter as tk
from tkinter import messagebox
import webbrowser

map_url = ""

def track_ip():
    api_key = api_entry.get()   # take API key from user
    ip = ip_entry.get()        # take IP from user

    if api_key == "" or ip == "":
        messagebox.showerror("Error", "Enter API Key and IP Address")
        return

    url = f"https://ipinfo.io/{ip}?token={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()

        city = data.get("city", "N/A")
        country = data.get("country", "N/A")
        org = data.get("org", "N/A")
        loc = data.get("loc", "N/A")

        result.set(f"City: {city}\nCountry: {country}\nISP: {org}\nLocation: {loc}")

        global map_url
        map_url = f"https://www.google.com/maps?q={loc}"

    except:
        messagebox.showerror("Error", "Something went wrong")


def open_map():
    if map_url:
        webbrowser.open(map_url)
    else:
        messagebox.showerror("Error", "First track IP")


# GUI
root = tk.Tk()
root.title("IP Tracker")
root.geometry("800x700")

tk.Label(root, text="IP Tracker", font=("Arial", 16)).pack(pady=10)

# API Key input
tk.Label(root, text="Enter API Key").pack()
api_entry = tk.Entry(root, width=30)
api_entry.pack(pady=5)

# IP input
tk.Label(root, text="Enter IP Address").pack()
ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

# Button
tk.Button(root, text="Track IP", command=track_ip).pack(pady=10)

# Result
result = tk.StringVar()
tk.Label(root, textvariable=result).pack(pady=10)

# Map button
tk.Button(root, text="Open Map", command=open_map).pack(pady=10)

root.mainloop()