import tkinter as tk

m = tk.Tk(className="merge")

button = tk.Button(m, text='Stop', width=25, command=m.destroy)
button.pack()

m.mainloop()