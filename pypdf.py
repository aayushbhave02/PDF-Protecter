import PyPDF2
from PyPDF2.errors import PdfReadError
import os

def encrypt_pdf_in_place(pdf_path, password):
    try:
        # Read original PDF
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_writer = PyPDF2.PdfWriter()

            # Copy pages to writer
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            # Encrypt with password
            pdf_writer.encrypt(password)

            # Temporary file path
            temp_path = pdf_path + ".temp"

            # Write to temporary file
            with open(temp_path, 'wb') as temp_file:
                pdf_writer.write(temp_file)

        # Replace original file with encrypted version
        os.replace(temp_path, pdf_path)

        print(f"\n✅ Successfully encrypted '{pdf_path}' with password.")

    except FileNotFoundError:
        print(f"\n❌ Error: File '{pdf_path}' not found.")
    except PdfReadError:
        print(f"\n❌ Error: File '{pdf_path}' is not a valid PDF.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

def main():
    print("🔐 In-Place PDF Encryption Tool\n")
    pdf_path = input("Enter the path of the PDF file to encrypt: ")
    password = input("Enter the password to protect the PDF: ")

    encrypt_pdf_in_place(pdf_path, password)

if __name__ == "__main__":
    main()
