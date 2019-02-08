from urllib.request import urlopen

url = input("Type a valid URL (Example--> https://github.com): ")
html = urlopen(url).read()
print("\nIn this code: \n", html, "\n")

hl = html.count('href='.encode())  # links -->href="..."
br = html.count('<br>'.encode())  # change line from <br>
p = html.count('</p>'.encode())  # change line from </p>
nl = br + p
print("System found...\nTotal links (href=...): ", hl, "\nTotal line changes (<br> | </p>): ", nl, "\n")

exit(0)
