# Regular Expressions

(1) Disjunction Construction:  Assign to the variable regexp a regular expression that matches either the exact string ab or one or more digits.

(2) Hyphenation:  Assign to the variable regexp a Python regular expression that matches lowercase words (a-z) or singly-hyphenated lowercase words.  Hint: It may not be possible to get correctly - do your best!

(3) Re Challenges:  Assign to the variable regexp a Python regular expression that matches single-argument mathematical functions. The function name is a lowercase word (a-z), the function argument must be a number (0-9), and there may optionally be spaces before and/or after the argument.  Hint: You may need to escape the ( and ).

(4) Escaping The Escape:  Assign to regexp a regular expression for double-quoted string literals that allows for escaped double quotes. Hint: Escape " and \.     Hint: (?: (?: ) ).

(5) Phone It In:  Suppose we want to recognize phone numbers with or without hyphens. The regular expression you give should work for any number of groups of any (non-empty) size, separated by 1 hyphen. Each group is [0-9]+.  Hint: Accept "5" but not "-6"

(6) Summing Numbers:  Write a procedure called sumnums(). Your procedure must accept as input a single string. Your procedure must output an integer equal to the sum of all integer numbers (one or more digits in sequence) within that string. If there are no decimal numbers in the input string, your procedure must return the integer 0. The input string will not contain any negative integers. Example Input: "hello 2 all of you 44". Example Output: 46. Hint: int("44") == 44.
