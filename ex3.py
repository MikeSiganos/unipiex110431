# path = "TestAppBlackJackV1.py"
path = input("Type filename... ")

newpath = path+"NoCommentsFile.py"
file = open(path, "r")
print("Opening file...\n")
newfile = open(newpath, "w")
print("Creating new file without comments...\n")
for line in file:
    if "#" in line:
        pos = line.find("#")
        tmp1 = "'"
        tmp2 = "\""
        pos4 = line.count(tmp1)
        pos5 = line.count(tmp2)
        pos6 = line.find(tmp1)
        pos7 = line.find(tmp2)
        if pos4 >= 2:
            pos6 = line.find(tmp1, pos6 + 1)
        if pos5 >= 2:
            pos7 = line.find(tmp2, pos7 + 1)
        if (pos6 > 0 or pos7 > 0) and pos !=0:
            if pos4 % 2 == 0 and 0 < pos6 <= pos:
                newfile.write(line[:pos]+"\n")  # Keeps comments inside inside "..."
            elif pos5 % 2 == 0 and 0 < pos7 <= pos:
                newfile.write(line[:pos]+"\n")  # Keeps comments inside inside "..."
            else:
                newfile.write(line)
        elif pos > 0:
            newfile.write(line[:pos]+"\n")  # Removes comments in the end of commands
        else:
            pass  # Removes lines containing only comments
    else:
        newfile.write(line)

file.close()
newfile.close()
print("Done!\n")

exit(0)
