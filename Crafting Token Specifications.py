import re

regexp = "[0-9]+.?[0-9]*"


tests = [("123", True), ("1.2", True), ("1.", True), (".5", False), (".5.6", False), ("1..2", False)]

for r, ans in tests:
    
    print ((re.findall(regexp, r) == [r]) == ans)
