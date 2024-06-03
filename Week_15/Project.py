#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into
# a single PDF.

import PyPDF2, os

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    try:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # Loop through all the pages (except the first) and add them.
        for pageNum in range(1, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

        pdfFileObj.close()

    except (IOError, PyPDF2.utils.PdfReadError):
        print(f"Error reading {filename}. Skipping.")

# Save the resulting PDF to a file.
output_path = '/path/to/output/directory/allminutes.pdf'
with open(output_path, 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)
