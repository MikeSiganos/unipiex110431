path = "TestAppBlackJackV1.py"

newpath = path+"NoCommentsFile.py"
file = open(path, "r")
print("Opening file...\n")
newfile = open(newpath, "w")
print("Creating new file without comments...\n")

for line in file:
    if "#" in line:
        if line.find("print") > 0 or line.find("input") > 0:
            pos = line.find("#")
            pos2 = line.find("print")
            pos3 = line.find("input")
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
            print(pos)
            if pos >= pos2+3 or pos >= pos3+3:
                print(tmp1, "4-->", pos4, "6-->", pos6)
                print(tmp2, "5-->", pos5, "7-->", pos7)
                if pos4 % 2 == 0 and 0 < pos6 <= pos:
                    newfile.write(line[:pos]+"\n")  # Keeps comments inside print & input commands
                elif pos5 % 2 == 0 and 0 < pos7 <= pos:
                    newfile.write(line[:pos]+"\n")  # Keeps comments inside print & input commands
                else:
                    newfile.write(line)
        elif line.find("#") > 0:
            pos = line.find("#")
            newfile.write(line[:pos]+"\n")  # Removes comments in the end of commands
        else:
            pass  # Removes the lines containing only comments
    else:
        newfile.write(line)

file.close()
newfile.close()
print("Done!\n")

exit(0)
