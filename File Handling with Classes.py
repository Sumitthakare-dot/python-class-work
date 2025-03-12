class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, content):
        with open(self.file_name, 'w') as file:
            file.write(content)

    def read(self):
        with open(self.file_name, 'r') as file:
            return 

handler = FileHandler("example.txt")
handler.write("Hello, world!")
print(handler.read())       
