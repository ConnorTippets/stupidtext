def stupidText(text):
    text = list(text)
    x = 0
    while x < len(text):
        text[x] = text[x].upper()
        text[x+1] = text[x+1].lower()
        x += 2
    text = ''.join(text)
    return text

stupidifier = stupidText
