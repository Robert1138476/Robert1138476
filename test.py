import tkinter as tk

def exit():
    root.quit()
    quit()

root = tk.Tk()

button = tk.Button(root, text="hey", command=exit)
button.pack(expand=True, fill="both")

root.mainloop()