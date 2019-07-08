# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

line_count = 0
average = 0
spam_conf_total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    if line.startswith("X-DSPAM-Confidence:") :
        line_count += 1
        colon_posit = line.find(':')
        string_value = line[colon_posit + 1:]
        spam_conf = float(string_value)
        spam_conf_total += spam_conf

average = spam_conf_total / line_count
        
print("Average spam confidence:", average)
