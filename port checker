import socket
import tkinter as tk
from tkinter import messagebox

def check_port():
    try:
        ip = ip_entry.get()
        socket.inet_aton(ip)

        port = int(port_entry.get())
        if not (0 <= port <= 65535):
            raise ValueError("Port number must be between 0 and 65535")

        result = sock.connect_ex((ip, port))

        if result == 0:
            messagebox.showinfo("Port Status", "Port is --> OPEN <--")
        else:
            messagebox.showinfo("Port Status", "Port is --> NOT OPEN <--")

    except socket.error as e:
        messagebox.showerror("Error", f"Socket error: {e}")
    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid input: {ve}")

# Create the socket outside the GUI
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# GUI setup
root = tk.Tk()
root.title("Port Checker")
root.geometry("200x110")
# IP Entry
tk.Label(root, text="Enter IP:").pack()
ip_entry = tk.Entry(root)
ip_entry.pack()

# Port Entry
tk.Label(root, text="Enter Port:").pack()
port_entry = tk.Entry(root)
port_entry.pack()

# Check Button
check_button = tk.Button(root, text="Check Port", command=check_port)
check_button.pack()

# Start the GUI
root.mainloop()

# Close the socket outside the GUI
sock.close()
