text=open('en-ru.txt')
Words={}
for line in text:
    line=line.replace(' ','').replace(',',' ').replace('   ','').replace('.','').replace('\t','').replace('\n','').split('-')



    Words[line[0]]=line[1]
text.close()

EnglishText=open('input.txt')
TranslatedText=open('output.txt','w')
translate=[]
for line in  EnglishText.read().split():
     line=line.replace('.','').replace(',',' ')
     line=line.lower()
     if line.lower() in Words:
         translate.append(Words[line])
     else:
         translate.append(line)

for elem in translate:
    print(elem, end=' ')
    TranslatedText.write(elem)
    TranslatedText.write(' ')
TranslatedText.close()
