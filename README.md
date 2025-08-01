## Project Title: In-Place PDF Encryption Tool using Python ##

# Project Description:

The In-Place PDF Encryption Tool is a lightweight and efficient Python-based utility designed to enhance document security by applying password protection to existing PDF files. This script uses the PyPDF2 library to read the contents of a PDF file, encrypt it with a user-provided password, and replace the original file with the encrypted version—ensuring minimal file clutter and streamlined protection.

# Key Objectives:

- Allow users to secure sensitive PDF documents with encryption.
- Provide a simple command-line interface for selecting the file and setting a password.
- Avoid creating unnecessary duplicate files by overwriting the original file safely.
- Ensure robust error handling for common issues like missing files or invalid formats.

# Features:

- Reads and encrypts any valid PDF file.
- Password protection using PyPDF2's encryption method.
- Temporary file handling to ensure original data is not lost during processing.
- Clear user prompts and console output.
- Exception handling for common errors such as:
                                              > File not found
                                              > Invalid PDF structure
                                              > Unforeseen read/write issues

# Skills Demonstrated:

- Python scripting
- File I/O operations
- Use of external libraries (PyPDF2)
- Exception handling
- Basic command-line interface design
- Safe in-place file modification

# Use Cases:

- Encrypting sensitive reports before sharing via email.
- Protecting personal records such as tax documents or contracts.
- Building into a larger document workflow or security automation tool.
