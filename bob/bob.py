def deleteWhiteSpace(text):
    textNew=""
    for t in text:
        if t!=" " and t!= "\n" and t!= "\r" and t != "\t":
            textNew+=t
    return textNew

def response(hey_bob=""):
    hey_bob=deleteWhiteSpace(hey_bob)
    if hey_bob=="":
        return "Fine. Be that way!"
    elif hey_bob.isupper():
        if hey_bob[-1]=='?':
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    elif hey_bob[-1]=='?':
        return "Sure."
    else:
        return "Whatever."