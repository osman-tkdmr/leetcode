def romanToInt(roman):
    l1 = []
    total = 0
    for i in roman:
        if   i == "I":l1.append(1)            
        elif i == "V":l1.append(5)            
        elif i == "X":l1.append(10)           
        elif i == "L":l1.append(50)         
        elif i == "C":l1.append(100)        
        elif i == "D":l1.append(500)        
        elif i == "M":l1.append(1000)      
        else:return "This isn't a roman number"
            
    for i in range(len(l1)-1):
        if l1[i]<l1[i+1]:
            l1[i] = 0 - l1[i]
    for i in l1:
        total+=i
    return total

print(romanToInt(input("please enter a roman number:")))
