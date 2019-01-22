from urllib.request import urlopen

url = input("Type a valid URL (Example--> http://www.cs.unipi.gr/): ")
html = urlopen(url).read()
print("\nIn this code: \n", html, "\n")

hl = html.count('href='.encode())
br = html.count('<br>'.encode())
p = html.count('</p>'.encode())
nl = br + p
print("System found...\nTotal links (href=...): ", hl, "\nTotal line changes (<br> | </p>): ", nl, "\n")

exit(0)
