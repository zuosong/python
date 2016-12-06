f = open('E:\Private Doc\code\links.txt','r')
longest = 0
while True:
    linelen = len(f.readline().strip())
    if not linelen:
        break
    if linelen > longest:
        longest = linelen
f.close()
return longest
