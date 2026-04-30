"""
- File is a container in which we can store data permanently. It is used to store data in a non-volatile memory.
- Extension of file is used to identify the type of file.
- Types of file:
    - Text file: It is a file that contains only text data. It is used to store data in a human-readable format. It has .txt extension.
    - Binary file: It is a file that contains binary data. It is used to store data in a machine-readable format. It has .bin extension.
    - PDF file: It is a file that contains portable document format. It is used to store data in a portable format. It has .pdf extension.
    - CSV file: It is a file that contains comma-separated values. It is used to store data in a tabular format. It has .csv extension.
    - JSON file: It is a file that contains JavaScript Object Notation. It is used to store data in a structured format. It has .json extension.
    - XML file: It is a file that contains Extensible Markup Language. It is used to store data in a hierarchical format. It has .xml extension.

! File handling in python:
    - It is a phenomenon of reading and writing the data in a file. 
    - It is used to store data permanently. 
    - It is used to create, open, close, read, write, append, delete, rename, copy, move, etc. files.
    - It is used to perform various operations on files.

    - To perform file handling we need the access of the file.
    - To access the file we need to open the file.
    - To open the file we need to use the open() function.    
    *- Syntax of open() function:
        f = open(r'file_path', 'mode')
        f.close()

        ? or

        with open(r'file_path', 'mode') as f:
            # SB

    - Modes of file handling:
        - 'r' --> To read the file. (Default mode)
        - 'w' --> To write the file. It will overwrite the existing data in the file.
        - 'a' --> To append the file. It will add the new data at the end of the file.
        - 'x' --> To create a new file. It will raise an error if the file already exists.
        - 'b' --> To open the file in binary mode. It is used to read and write binary files.
        - 't' --> To open the file in text mode. It is used to read and write text files. (Default mode)
        - '+' --> To open the file in read and write mode. It is used to read and write files.

"""