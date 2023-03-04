import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("메모장")
        self.filename = None
        self.text = tk.Text(master)
        self.text.pack(fill=tk.BOTH, expand=1)

        # 메뉴바 생성
        menu_bar = tk.Menu(master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="열기", command=self.open_file)
        file_menu.add_command(label="저장", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="끝내기", command=master.quit)
        menu_bar.add_cascade(label="파일", menu=file_menu)
        master.config(menu=menu_bar)

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Files", "*.txt"),
                                                              ("All Files", "*.*")])
        if self.filename:
            self.text.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.text.insert(tk.END, f.read())

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                         filetypes=[("Text Files", "*.txt"),
                                                                    ("All Files", "*.*")])
        if self.filename:
            with open(self.filename, "w") as f:
                f.write(self.text.get(1.0, tk.END))

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()