# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
text = fh.read()
up_text = text.upper()
print(up_text.rstrip())
fh.close()