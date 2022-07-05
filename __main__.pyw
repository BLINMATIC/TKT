import tkinter as tk

try:
    import libaries as ext
except:
    root = tk.Tk()
    tk.Label(root, text="NOTICE: Could not find folder libaries").pack()
    tk.Button(root, text="ok", width=10, height=1, command=lambda: root.destroy()).pack()
    root.mainloop()

class main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        self.root.title("TKT")
        self.out = tk.Text(self.root, width=80, height=15)
        self.inp = tk.Text(self.root, width=80, height=1)
        self.send = tk.Button(self.root, text="SEND ↲", width=90, height=1, command=lambda: self.send1())

        self.out.pack()
        self.inp.pack()
        self.send.pack()

        self.out.config(state=tk.DISABLED)
        self.root.mainloop()
    
    def send1(self):
        txt = self.inp.get("1.0", "end-1c")
        self.out.config(state=tk.NORMAL)
        self.out.insert("1.0", "USR > " + txt + "\n")
        exec("self.out.insert(\"1.0\", \"OUT > \" + " + txt + " + \"\\n\")")
        self.out.config(state=tk.DISABLED)
        self.inp.delete("1.0", "end-1c")

if __name__ == "__main__":
    m = main()
