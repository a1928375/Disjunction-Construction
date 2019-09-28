import re

#regexp = r"[0-9]+(?:-[0-9]+)*"
regexp = r"(?:[0-9]+-)*[0-9]+"

print (re.findall(regexp,"123-4567") == ["123-4567"])
print (re.findall(regexp,"1234567") == ["1234567"])
print (re.findall(regexp,"08-78-88-88-88") == ["08-78-88-88-88"])
print (re.findall(regexp,"0878888888") == ["0878888888"])
print (re.findall(regexp,"-6") != ["-6"])
