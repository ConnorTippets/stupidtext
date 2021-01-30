from functions import stupidifier

ip = str(input('Input: '))
co = 'Output: '

output = stupidifier(ip)
co += output
print(co)
