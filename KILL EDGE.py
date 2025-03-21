import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Function to run the KILL EDGE batch script
def kill_edge():
    try:
        # Assuming the .bat script is included and named 'kill_edge.bat'
        subprocess.run(['kill_edge.bat'], check=True, shell=True)
        messagebox.showinfo("Success", "Edge has been removed successfully.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "An error occurred while removing Edge.")

# Function to reinstall Edge
def reinstall_edge():
    # You can include code here to download and reinstall Edge
    messagebox.showinfo("Reinstall", "Reinstalling Edge... (This feature can be enhanced)")

# Function to exit the app
def exit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("KILL ECS - Edge Remover")
root.geometry("400x300")
root.config(bg="#2f4f4f")

# Label for the app
label = tk.Label(root, text="Welcome to KILL ECS!", font=("Arial", 14), bg="#2f4f4f", fg="white")
label.pack(pady=20)

# Button to Kill Edge
kill_edge_button = tk.Button(root, text="KILL EDGE", font=("Arial", 12), fg="white", bg="red", width=15, command=kill_edge)
kill_edge_button.pack(pady=10)

# Button to Reinstall Edge
reinstall_edge_button = tk.Button(root, text="Reinstall Edge", font=("Arial", 12), fg="white", bg="green", width=15, command=reinstall_edge)
reinstall_edge_button.pack(pady=10)

# Button to Exit
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), fg="white", bg="gray", width=15, command=exit_app)
exit_button.pack(pady=20)

# Run the app
root.mainloop()
