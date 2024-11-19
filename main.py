readr=open("C:/Users/HP/Desktop/VS Code/file handling/file handling.txt","r")
print(readr.read())
readr.close()

writer=open("C:/Users/HP/Desktop/VS Code/file handling/file handling.txt","w")
print(writer.write("hello\n"))
print(writer.write("good evening"))
writer.close()

appendr=open("C:/Users/HP/Desktop/VS Code/file handling/file handling.txt","a")
print(appendr.write("bye\n"))
print(appendr.write("hi"))
appendr.close()

