#File Handling ===========================================

file = open('text.txt', 'w') #w for write that means it will write the text to the file
text1 = "Hello World!\n"
file.write(text1)
text2 = "This is my first file handling program.\n"
file.write(text2)
text3 = input("Import the file name: ")
file.write(text3)
file.close()
