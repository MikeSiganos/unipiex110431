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
            if pos >= pos2+3 or pos >= pos3+3:
                newfile.write(line)  # Keeps comments inside print & input commands
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
