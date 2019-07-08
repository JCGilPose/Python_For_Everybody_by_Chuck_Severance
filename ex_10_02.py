name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times = dict()

for line in handle:
    streamlined = line.rstrip()
    words = streamlined.split()
    if len(words) == 0 or words[0] != 'From':
        continue
    else:
        time = words[5]
        pos = time.find(':')
        hour = time[0: pos]
        times[hour] = times.get(hour, 0) + 1

hours = list()

for k, v in times.items():
    records = k, v
    hours.append(records)
    hours.sort()

for k, v in hours:
    print(k, v)