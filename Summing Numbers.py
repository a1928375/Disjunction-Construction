import re

def sumnums(sentence): 
    
    result  = re.findall(r"[0-9]+" ,sentence)
    
    j = 0
    
    for i in result:
        
        j = j+int(i)
    
    return j
    
    
def sumnums2(sentence):
    
    result = []
    
    i = 0
    k = 0
    
    while i < len(sentence):
            
        if sentence[i] in ("0123456789"):
            
            a = sentence.find(" ",i)
            
            b = sentence.find(",", i)
            
            if a == -1:
                
                a = float('inf')
            
            elif b == -1:
                
                b = float('inf')
                    
            num = min(a,b)
            
            result.append(sentence[i:num])
            
            i = num
        
        else:
            
            i = i+1
    
    for j in result:
        
        k = k+int(j)
    
    return k
        
test_case_input = """The Act of Independence of Lithuania was signed on February 16, 1918, by 20 council members."""

test_case_output = 1954

if sumnums(test_case_input) == test_case_output:
    
  print ("Test case passed.")
  
else:
    
  print ("Test case failed:")
  
  print (sumnums(test_case_input))
