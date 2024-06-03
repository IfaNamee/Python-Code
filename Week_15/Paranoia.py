import os
import PyPDF2
import sys


def decrypt_pdfs(folder, password):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith('_encrypted.pdf'):
                encrypted_pdf_path = os.path.join(foldername, filename)
                decrypted_pdf_path = os.path.join(foldername, f"{filename[:-14]}_decrypted.pdf")

                # Decrypt the PDF
                with open(encrypted_pdf_path, 'rb') as encrypted_pdf:
                    pdf_reader = PyPDF2.PdfFileReader(encrypted_pdf)
                    pdf_reader.decrypt(password)

                    with open(decrypted_pdf_path, 'wb') as decrypted_pdf:
                        pdf_writer = PyPDF2.PdfFileWriter()

                        for page_num in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))

                        pdf_writer.write(decrypted_pdf)

                print(f"{encrypted_pdf_path} decrypted successfully to {decrypted_pdf_path}.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decrypt_pdfs.py <folder> <password>")
    else:
        folder = sys.argv[1]
        password = sys.argv[2]
        decrypt_pdfs(folder, password)
