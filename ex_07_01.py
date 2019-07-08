# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    streamlined = line.rstrip()
    capitalized = streamlined.upper()
    print(capitalized)