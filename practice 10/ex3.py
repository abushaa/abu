file = open('/usr/share/licenses/python/LICENSE')
text = file.read()
text = text.lower()
for symbol in ',.-!?()':
    text=text.replace(symbol,' ')
words=[]
stats={}
for word in text:
    if word in stats:
        stats[word]+=1
    else:
        pass
print()