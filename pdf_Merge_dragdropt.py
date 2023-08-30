import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import PyPDF2
import os

class PDFManipulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Tools ")

        self.label = tk.Label(root, text="Select an action:", )
        self.label.pack(pady=10)

        self.merge_button = tk.Button(root, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.pack(pady=5)

        self.split_button = tk.Button(root, text="Split PDF", command=self.split_pdf_to_pages)
        self.split_button.pack(pady=5)

    def merge_pdfs(self):
        pdf_files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if pdf_files:
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if output_path:
                pdf_merger = PyPDF2.PdfMerger()
                for pdf_file in pdf_files:
                    pdf_merger.append(pdf_file)
                
                with open(output_path, "wb") as output_file:
                    pdf_merger.write(output_file)
                
                messagebox.showinfo("Success", "PDFs merged successfully.")

    def split_pdf_to_pages(self):
        input_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if input_file:
            output_folder = filedialog.askdirectory()
            if output_folder:
                pdf_reader = PyPDF2.PdfReader(input_file)
                num_pages = len(pdf_reader.pages)
                
                for page_num in range(num_pages):
                    output_path = os.path.join(output_folder, f"page_{page_num + 1}.pdf")
                    pdf_writer = PyPDF2.PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                    with open(output_path, "wb") as output_file:
                        pdf_writer.write(output_file)

                messagebox.showinfo("Success", f"PDF split into pages and saved to {output_folder}")

def main():
    root = tk.Tk()
    app = PDFManipulatorApp(root)
    root.geometry("250x150")
    root.minsize(260, 150)
    root.maxsize(260, 150)
    root['background']='#7cabfc'
    root.mainloop()

if __name__ == "__main__":
    main()
