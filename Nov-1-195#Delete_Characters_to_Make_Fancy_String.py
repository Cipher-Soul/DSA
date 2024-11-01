# 1957. Delete Characters to Make Fancy String

def fancyString(stri):
    final  = ""
    i=0
    for s in stri:
        i+=1
        # print('=>',i)
        if len(final)>=2 and final[-1] ==s and final[-2] == s:
            pass           
        else:
            final += s
            # print(final)
        
    return final 
    
print(fancyString("aaaabaaaa"))