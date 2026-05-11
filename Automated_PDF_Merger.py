#Auto PDF Merger

from pypdf import PdfWriter
import os

pdf_folder = "C:/Users/Priyanshi.dwivedi.BLR/Downloads/PDF files"
merged_pdf = "output_merged.pdf"

merger = PdfWriter()

for file in (os.listdir(pdf_folder)):
    if file.endswith(".pdf"):
        merger.append(os.path.join(pdf_folder,file))


merger.write(merged_pdf)
merger.close()

print("PDFs successfully merged!")