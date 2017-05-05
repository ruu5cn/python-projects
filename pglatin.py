"""Translates words from pig latin to english"""
def fromPG():
    text = input("What is the pig latin?").lower()
    copyL = text.split(" ")
    through = len(copyL); now = 0
    while now < through:
        current = list(copyL[now])
        current.reverse()
        current.append(current[2])
        del(current[0:3])
        current.reverse()
        current = "".join(current)
        copyL[now] = current
        now += 1
    copyL = " ".join(copyL)
    return copyL
def toPG():
    text = input("What is the text?")
    copyL = text.split(" ")
    through = len(copyL); now = 0
    while now < through:
        current = list(copyL[now])
        current.append(current[0])
        del(current[0])
        current = "".join(current)
        current = current + 'ay'
        copyL[now] = current
        now += 1
    copyL = " ".join(copyL)
    return copyL
