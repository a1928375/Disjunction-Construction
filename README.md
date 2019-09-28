# Regular Expressions

(1) Disjunction Construction:  Assign to the variable regexp a regular expression that matches either the exact string ab or one or more digits.

(2) Hyphenation:  Assign to the variable regexp a Python regular expression that matches lowercase words (a-z) or singly-hyphenated lowercase words.  Hint: It may not be possible to get correctly - do your best!

(3) Re Challenges:  Assign to the variable regexp a Python regular expression that matches single-argument mathematical functions. The function name is a lowercase word (a-z), the function argument must be a number (0-9), and there may optionally be spaces before and/or after the argument.  Hint: You may need to escape the ( and ).

(4) Escaping The Escape:  Assign to regexp a regular expression for double-quoted string literals that allows for escaped double quotes. Hint: Escape " and \.     Hint: (?: (?: ) ).

(5) Phone It In:  Suppose we want to recognize phone numbers with or without hyphens. The regular expression you give should work for any number of groups of any (non-empty) size, separated by 1 hyphen. Each group is [0-9]+.  Hint: Accept "5" but not "-6"

(6) Summing Numbers:  Write a procedure called sumnums(). Your procedure must accept as input a single string. Your procedure must output an integer equal to the sum of all integer numbers (one or more digits in sequence) within that string. If there are no decimal numbers in the input string, your procedure must return the integer 0. The input string will not contain any negative integers. Example Input: "hello 2 all of you 44". Example Output: 46. Hint: int("44") == 44.

(7) Single Hyphenated Words:  We examined hyphenated words in a quiz in class. In this problem you will get a chance to handle them correctly. Assign to the variable regexp a Python regular expression that matches both words (with letters a-z) and also singly-hyphenated words. If you use grouping, you must use (?: and ) as your regular expression parentheses. Examples: 

    regexp exactly matches "astronomy"  
    regexp exactly matches "near-infrared"  
    regexp exactly matches "x-ray"  
    regexp does not exactly match "-tricky" 
    regexp does not exactly match "tricky-" 
    regexp does not exactly match "large - scale" 
    regexp does not exactly match "gamma-ray-burst" 
    regexp does not exactly match "" 

Your regular expression only needs to handle lowercase strings. In Python regular expressions, r"A|B" checks A first and then B - it does not follow the maximal munch rule. Thus, you may want to check for doubly-hyphenated words first and then non-hyphenated words.

(8) Email Addresses And Spam:  In this assignment you will write Python code to to extract email addresses from a string of text. To avoid unsolicited commercial email (commonly known as "spam"), users sometimes add the text NOSPAM to an other-wise legal email address, trusting that humans will be smart enough to remove it but that machines will not. As we shall see, this provides only relatively weak protection. For the purposes of this exercise, an email address consists of a word, an '@', and a domain name. A word is a non-empty sequence of upper- or lower-case letters. A domain name is a sequence of two or more words, separated by periods. 

    Example: wes@udacity.com
    Example: username@domain.name
    Example: me@this.is.a.very.long.domain.name

If an email address has the text NOSPAM (uppercase only) anywhere in it, you should remove all such text. Example: 
    
    'wes@NOSPAMudacity.com' -> 'wes@udacity.com' 
    'wesNOSPAM@udacity.com' -> 'wes@udacity.com' 

You should write a procedure addresses() that accepts as input a string. Your procedure should return a list of valid email addresses found within that string -- each of which should have NOSPAM removed, if applicable. 

Hint 1: Just as we can FIND a regular expression in a string using re.findall(), we can also REPLACE or SUBSTITUTE a regular expression in a string using re.sub(regexp, new_text, haystack). Example: 

    print re.sub(r"[0-9]+", "NUMBER", "22 + 33 = 55") 
    "NUMBER + NUMBER = NUMBER" 

Hint 2: Don't forget to escape special characters. 

Hint 3: You don't have to write very much code to complete this exercise: you just have to put together a few concepts. It is possible to complete this exercise without using a lexer at all. You may use any approach that works. 

(9) Crafting Token Specifications:  Define a variable regexp that matches numbers with 1 or more leading digits and an optional . followed by 0 or more digits.
