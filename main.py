readr=open("C:/Users/HP/Desktop/VS Code/file handling/file handling.txt","r")
print(readr.read())
readr.close()

writer=open("C:/Users/HP/Desktop/VS Code/file handling/file handling.txt","w")
print(writer.write("hello"))
writer.close()

appendr=open("C:/Users/HP/Desktop/VS Code/file handling/file handling.txt","a")
print(appendr.write("bye"))
appendr.close()
