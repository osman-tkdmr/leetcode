def concatenatedBinary(n):
    binaryes = []
    """
    def decimalToBinary(dec):
        
        a = 0
        i = 1
        while dec > 0: 
            a += (dec % 2) * i      my code :(
            i *= 10
            dec //= 2
        return a 
    """
    #decimal to binary : binary = bin(decimal)[2:]  python code :)
    for i in range(1, n+1):
        binaryes.append(bin(i)[2:])
    

        """
        def binaryToDecimal(dec):    
            dec = 0
            j = 0
            for i in bin[::-1]:             my code :(
                if i == '1':
                    dec += (2 ** j)
                j += 1
            return dec 
        """
     #binary to decimal :  decimal = int(binary, 2)   I love python :)
    return int(("".join(binaryes)),2)


print(concatenatedBinary(3))