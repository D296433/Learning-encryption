def reverse(text):
    text = [*text]
    newText = ""
    for i in reversed(text):
        newText += i
    return newText