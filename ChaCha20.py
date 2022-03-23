import math, random

#Assumptions 0: Base Assumption: input and outputs off all functions is a string, unless if specified for specialised cases
#Assumption 1: Nounce and Key are values in the Ascii Space, so a nouce value of 000000001 is allowed. Otherwise minimum noucse would be A: 01000001
#Nounce function generates nounce for given number of blocks

#Ascii Space starts from 0XXXXX... so first bit of each 8 bit ascii value is 0
def RandomNounce(n): 
    temp = ''
    for y in range (n):
        for m in range(4):
            temp += "0"    
            for x in range(7):
                temp += str(random.randint(0, 1))

    #This splits string into list of strings of 32 bit each 
    temp = [temp[i:i+32] for i in range(0, len(temp), 32)]
    return temp


def RandomKey(): 
    temp =''
    for x in range(256):
        temp += str(random.randint(0, 1))
    
    #This converts string into list string of 32 bit each
    temp = [temp[i:i+32] for i in range(0, len(temp), 32)]
    return temp

def ConstantGenerator():
    constant_s = "expand 32-byte k"
    #converting to binary, in 1 line loop
    constants = ''.join(format(ord(i), '08b') for i in constant_s)

    #Now splitting into 4 parts, a,b,c,d using anoyher 1 line loop
    #This converts string into list string of 32 bit each
    constants = [constants[i:i+32] for i in range(0, len(constants), 32)]
    return constants
    


def Rotate(text,n):
    HackyShift = (text[n:] + text[:n])
    return HackyShift


def QuarterRound(a,b,c,d):



    
    ###

    a = bin(int(a, 2) + int(b, 2))
    a = a[2:].zfill(32)
    d = int(d,2) ^ int(a,2)  #d ^= a
    d ='{0:b}'.format(d)
    d = str(d).zfill(32)

    d = Rotate(d, 16)



    ###
    c = bin(int(c, 2) + int(d, 2))
    c = c[2:].zfill(32)

    b = int(b,2) ^ int(c,2)  #b ^= c
    b ='{0:b}'.format(b)
    b = str(b).zfill(32)        

    b = Rotate(b, 12)


    ###

    a = bin(int(a, 2) + int(b, 2))
    a = a[2:].zfill(32)
    
    d = int(d,2) ^ int(a,2)  #d ^= a
    d ='{0:b}'.format(d)
    d = str(d).zfill(32)

    d = Rotate(d, 8)



    
    ###
    c = bin(int(c, 2) + int(d, 2))
    c = c[2:].zfill(32)

    b = int(b,2) ^ int(c,2)  #b ^= c
    b ='{0:b}'.format(b)
    b = str(b).zfill(32)  

    b = Rotate(b, 7)
    

 

    if len(a) > 32:
        a = a[len(a) - 32:]
    if len(b) > 32:
        b = b[len(b) - 32:]
    if len(c) > 32:
        c = c[len(c) - 32:]
    if len(d) > 32:
        d = d[len(d) - 32:]


    return (a,b,c,d)
    




def main():
    #Getting list of 4 Constants in binary
    Constants = ConstantGenerator()

    #now generating random key
    Key = RandomKey() #default is 256 bits

    #Now generating 2 nounces sub-blocks
    #Assumption 2, 1 block contains 2 counters and 2 nounces
    Nounces = RandomNounce(2)       #argument 2 means 32*2 bits
    Counter = ["00000000000000000000000000000000","00000000000000000000000000000001"]

    #Now combining to form a block
    
    block = Constants+Key+Counter+Nounces
    
    #now block is ready for deployment
    #Testing Block
    

    #5 test cases for the QuarterRound Function
    #Assumption 3: We're going to apply this, COLUMN BY COLUMN for first 4 test cases, and diaganol for last test case

    

    Case_1 = block[0], block[4], block[ 8], block[12]
    Case_2 = block[1], block[5], block[ 9], block[13]
    Case_3 = block[2], block[6], block[10], block[14]
    Case_4 = block[3], block[7], block[11], block[15]
    Case_5 = block[0], block[5], block[10], block[15]
    print("Case 1: Running QuarterRound(block[0], block[4], block[ 8], block[12]) with values \n ",Case_1)
    print("Output:", QuarterRound(block[0], block[4], block[ 8], block[12])) # column 0
  
    print("\n\nCase 2: Running QuarterRound(block[1], block[5], block[ 9], block[13]) with values\n ", Case_2)# column 1
    print("Output: ", QuarterRound(block[1], block[5], block[ 9], block[13])) # column 1

    print("\n\nCase 3: Running QuarterRound(block[2], block[6], block[10], block[14]) with values\n ", Case_3)# column 2
    print("\n\nOutput: ", QuarterRound(block[2], block[6], block[10], block[14]) )# column 2

    print("Case 4: Running QuarterRound(block[3], block[7], block[11], block[15]) with values\n ",Case_4 )# column 3
    print("\n\nOutput: ", QuarterRound(block[3], block[7], block[11], block[15]) )# column 3
    
    print("Case 5: Running QuarterRound(block[0], block[5], block[10], block[15]) with values\n ",Case_5) # diagonal 1
    print("\n\nOutput: ", QuarterRound(block[0], block[5], block[10], block[15]) )# diagonal 1
  
    #FINALLY APPLYING QUARTER ROUND

    #finding average diffusion

    print("##########\n\nPart 2: CHECKING DIFFUSION\n\n\n")
    total_diffusion = 0
    for cases in Case_1,Case_2,Case_3,Case_4,Case_5:
        Input = ""
        Output = ""
        Input = Input.join(cases)
        print("\n\nInput: ",Input)

        temp = QuarterRound(*Case_1)


        Output= Output.join(temp)
        
        diffusion = int(Input,2) ^ int(Output,2)  
        
        diffusion ='{0:b}'.format(diffusion)
        diffusion = str(diffusion).zfill(128)
        
        diffusion = diffusion.count("1")
        print("Diffusion: ", diffusion)

        total_diffusion += diffusion

    print("\n\nAverage Diffusion = ", total_diffusion/5)
    print("Average Diffusion in % = ",((total_diffusion/5)*100/128),"%")
    #Assumption 
    print("NOTE: Diffusion is checked for 5 test quarter round functions of 1 round only! which has an input and output of 128bits\nIn Rakshit's Lab Testing, Diffusion was found to be around 50% average with multiple tests")



main()
