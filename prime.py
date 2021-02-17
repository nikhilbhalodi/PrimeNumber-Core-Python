


def prime_number():

    in1 = int(input("Enter start range: "))  
    

    output = []  
    
      
    if in1 >= 0:
        
        in2 = int(input("Enter end range: "))
        for i in range(in1,in2 + 1):  
            for j in range(2,i):  
                if (i % j) == 0:
                    break  
            else:
                output.append(i)
        if output[0]==1 or output[1]==1 :
            output.remove(1)
            if output[0]==0:
                output.remove(0)
        
        print(output) 
    else:
        print("Please Enter greterthen 1 input")


    

prime_number()