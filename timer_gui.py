import tkinter as tk
from tkinter import messagebox
import time
import threading


def start_countdown():
    try:
        start_num = int(entry_number.get())
        final_message = entry_message.get()

        if start_num <= 0:
            messagebox.showerror("Invalid Input", "Please enter a number greater than 0.")
            return

        # Disable the Start button while countdown runs
        button_start.config(state=tk.DISABLED)

        def run_countdown():
            for i in range(start_num, 0, -1):
                label_output.config(text=str(i))
                time.sleep(1)
            label_output.config(text=final_message)
            ask_to_repeat()

        threading.Thread(target=run_countdown).start()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


def ask_to_repeat():
    result = messagebox.askyesno("Repeat", "Do you want to run the timer again?")
    if result:
        reset_fields()
    else:
        root.quit()


def reset_fields():
    entry_number.delete(0, tk.END)
    entry_number.focus_set()
    entry_message.delete(0, tk.END)
    label_output.config(text="")
    button_start.config(state=tk.NORMAL)


# GUI setup
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x250")

# Widgets
tk.Label(root, text="Enter starting number:").pack(pady=5)
entry_number = tk.Entry(root)
entry_number.pack(pady=5)

tk.Label(root, text="Enter final message:").pack(pady=5)
entry_message = tk.Entry(root)
entry_message.pack(pady=5)

button_start = tk.Button(root, text="Start Countdown", command=start_countdown)
button_start.pack(pady=10)

label_output = tk.Label(root, text="", font=("Helvetica", 24))
label_output.pack(pady=20)


if __name__ == "__main__":
    root.mainloop()
