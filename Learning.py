import re 

regexp = "a[b-z]+|a+"


tests = [("aaa", True), ("abb", True), ("acc", True), ("aabbb", False), ("aaccc", False), ("bc", False)]

for r, ans in tests:
    print ((re.findall(regexp, r) == [r]) == ans)
