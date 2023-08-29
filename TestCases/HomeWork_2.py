#Task №2

text = "Hello"
seen = set()
for ch in text:
    if ch in seen:
        print(ch)
        break
    else:
        seen.add(ch)