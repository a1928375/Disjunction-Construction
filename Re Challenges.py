import re

regexp = r"[a-z]+[(][ ]*[0-9][ ]*[)]"

print (re.findall(regexp,"cos(0)") == ["cos(0)"])

print (re.findall(regexp,"sqrt(   2     )") == ["sqrt(   2     )"])

print (re.findall(regexp,"cos     (0)") != ["cos     (0)"])

print (re.findall(regexp,"sqrt(x)") != ["sqrt(x)"])
