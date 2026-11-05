text = "X-DSPAM-Confidence:    0.8475"
a = text.find('0.8475')
a = float(text[23:])
print(a)
