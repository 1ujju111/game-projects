import tkinter as tk
from tkinter import filedialog, scrolledtext

class TypingPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Practice Program")
        
    
        self.select_file_button = tk.Button(root, text="Select Text File", command=self.load_file)
        self.select_file_button.pack(pady=10)
        
  
        self.text_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
        self.text_display.pack(pady=10)
        self.text_display.config(state=tk.DISABLED)
        
        self.typing_area = tk.Text(root, wrap=tk.WORD, height=10, width=50)
        self.typing_area.pack(pady=10)
        
       
        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.start_button.pack(pady=10)
       
        self.results_label = tk.Label(root, text="")
        self.results_label.pack(pady=10)
        
        self.original_text = ""
        
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.original_text = file.read()
            self.text_display.config(state=tk.NORMAL)
            self.text_display.delete(1.0, tk.END)
            self.text_display.insert(tk.END, self.original_text)
            self.text_display.config(state=tk.DISABLED)
            
    def start_typing(self):
        self.typing_area.delete(1.0, tk.END)
        self.typing_area.bind('<KeyRelease>', self.check_typing)
        self.results_label.config(text="")
        
    def check_typing(self, event):
        typed_text = self.typing_area.get(1.0, tk.END).strip()
        original_text_trimmed = self.original_text[:len(typed_text)]
        
        if typed_text == original_text_trimmed:
            self.typing_area.config(bg="white")
        else:
            self.typing_area.config(bg="lightcoral")
        
        if typed_text == self.original_text:
            self.typing_area.config(state=tk.DISABLED)
            self.results_label.config(text="Well done! You have typed the text correctly.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingPracticeApp(root)
    root.mainloop()