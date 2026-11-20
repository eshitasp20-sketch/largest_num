import sys
def largest_num(num1,num2,num3):
    if((num1 > num2) and (num1 > num3)):
        return num1
    elif((num2 > num1) and (num2 > num3)):
        return num2
    else:
        
        return num3

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])

    print("Largest number is ", largest_num(num1, num2, num3))