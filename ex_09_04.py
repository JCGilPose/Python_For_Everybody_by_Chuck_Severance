name = input("Enter file:")

if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)

senders = dict()
count = 0

for line in handle:
    streamlined = line.rstrip()
    words = streamlined.split()
    if len(words) == 0 or words[0] == "From:" :
        continue
    else:
        if words[0] == "From":
            senders[words[1]] = senders.get(words[1], 0) + 1

big_sender = None
big_count = None

for sender,count in senders.items() :
    if big_count is None or count > big_count:
        big_sender = sender
        big_count = count

print(big_sender, big_count)
