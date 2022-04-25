f = open("Test.txt", 'r', -1, 'utf-8')
text = f.readline()
f.close()

count = 0
for i in text:
    a = i.split()
    count += len(a)
    print(count)
f = open("Test.txt", 'a', -1, 'utf-8')
f.write('В тексте'+ str(count) +'слов.')
f.close()

f = open("Test.txt", 'r', -1, 'utf-8')
f.read()
f.close()