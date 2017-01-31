s = 'aaaabbсaa'
s = 'abc'
#s = str(input())
ziped = ''
i = 0
while i < len(s):
    ziped += s[i]
    k = 1
    while i+k < len(s):
        if s[i] == s[i+k]:
            k += 1
        else:
            break
    ziped += str(k)
    i += k

print(ziped)
