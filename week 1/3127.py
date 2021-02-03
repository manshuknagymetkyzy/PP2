s = input()
a = s[s.find('h')+1:s.rfind('h')]
print(s[:s.find('h')+1] + a.replace('h', 'H') + s[s.rfind('h'):])