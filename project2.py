import tkinter as tk
from tkinter import filedialog
import PyPDF2

class EbookReaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ebook Reader")
        
        self.text_widget = tk.Text(root, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)
        
        open_button = tk.Button(root, text="Open Ebook", command=self.open_ebook)
        open_button.pack()
    
    def open_ebook(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            with open(file_path, "rb") as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                self.text_widget.delete('1.0', tk.END)
                self.text_widget.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = EbookReaderApp(root)
    root.mainloop()