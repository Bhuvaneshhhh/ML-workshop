try:
    file = open("example.txt", "r")
    content=file.read()
except FileNotFoundError:
    print("The file was not found")
finally:
    if 'file' in locals():
        file.close()
        print("File closed")
