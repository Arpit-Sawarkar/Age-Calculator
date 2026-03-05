import tkinter as tk
from tkinter import messagebox
from logic import calculate
def start():
    windows = tk.Tk()
    windows.title("Age Calculator")
    windows.geometry("600x500")
    windows.configure(bg="#0f172a")
    windows.resizable(False, False)
    #label
    label = tk.Label(windows,text="Age Calculator",font=("Arial", 25, "bold"),fg="white",bg="#0f172a")
    label.pack(anchor="w",padx=20,pady=20)
    #text
    dob_label=tk.Label(windows,text="Enter your Date of Birth (YYYY/MM/DD)",font=("Arial",13),fg="white",bg="#0f172a")
    dob_label.pack(anchor="w",padx=10,pady=(5,5))
    #input box
    entry_frame = tk.Frame(windows, bg="#1e293b",bd=2,relief="groove")
    entry_frame.pack(anchor="w", padx=12, pady=5)
    dob_entry = tk.Entry(entry_frame,font=("Arial", 13),bg="#1e293b",fg="white",insertbackground="white",width=30,bd=0)
    dob_entry.pack(padx=5, pady=3)
    #function for button
    def show_age():
        dob = dob_entry.get()
        try:
            years, months, days = calculate(dob)
            if not result_frame.winfo_ismapped():
                result_frame.pack(anchor="w", padx=12, pady=(5, 20), fill="x")
            result_label.config(text=f"You are {years} years, {months} months and {days} days old !",fg="#22c55e")
        except Exception:
            tk.messagebox.showerror("Error", "Invalid Date! Use YYYY/MM/DD format.")
    #button
    button=tk.Button(windows,text="Calculate Age",font=("Arial",11,"bold"),bg="#1e293b",fg="white",activebackground="#1d4ed8",activeforeground="white",bd=2,highlightbackground="white",highlightthickness=4,padx=2,pady=2,command=show_age)
    button.pack(anchor="w",padx=10,pady=10)
    #result
    result_frame = tk.Frame(windows, bg="#1e293b")
    result_label = tk.Label(result_frame,text="",font=("Arial", 13, "bold"),fg="#22c55e",bg="#1e293b",padx=10, pady=10,anchor="w",justify="left")
    result_label.pack(fill="both")
    #mainloop
    windows.mainloop()
