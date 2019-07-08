fname = input("Enter file name: ")

fh = open(fname)

lst = list()

for line in fh:
    if line == "":
        continue
    else:
        streamlined = line.rstrip()
        words = streamlined.split()
        for word in words:
            if word in lst:
                continue
            else:
                lst.append(word)
                
lst.sort()

print(lst)