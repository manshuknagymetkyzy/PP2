s = input()
a = s[s.find('h')+1 : s.rfind('h')]
print(s[:s.rfind('h')] + a + s[s.rfind('h'):])