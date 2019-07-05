text = "X-DSPAM-Confidence:    0.8475"

colon_pos = text.find(':')

value_string = text[colon_pos + 1:]

value = float(value_string)

print(value)
