

def equalize(str1,str2): # pads with leading 0's
    length = max(len(str1), len(str2))
    str1 = [0 for i in range(len(str1), length)] + str1
    str2 = [0 for i in range(len(str2), length)] + str2

    return str1, str2


def stradd(str1, str2):  # List addition algorithm applied to strings
    str1,str2 = equalize(str1,str2)
    c = 0
    result = []

    for i in range(1, len(str1) + 1):
        col = str1[-i] + str2[-i] + c

        result.append(col % 10)

        c = col / 10
        
    if c != 0:
        result.append(c)

    return result.reverse()


def strsub(str1, str2):
    str1,str2 = equalize(str1,str2)
    result = []

    for i in range(1, len(str1) + 1):
        diff = str1[-i] - str2[-i]
        
        if diff >= 0:
            result.append(diff)
            
        else:
            j = i + 1
            while j <= len(str1):
                str1[-j] = (str1[-j] + 9) % 10
                
                if str1[-j] != 9:
                    break
                    
                else:
                    j = j + 1
                    
            result.append(diff + 10)

    return result.reverse


def karatsuba_mult(s1, s2):
    s1, s2 = str(s1), str(s2)

    if len(s1) or len(s2) == 1:
        return int(s1) * int(s2)

    else:  # len(s1) and len(s2) != 1:
        s1,s2 = equalize(s1,s2)

    n = len(s1)
    split = n // 2 # we split at about the middle of the string

    subdiv = n - split  # create subdivision amount

    a ,b = int(s1[:subdiv]), int(s1[subdiv:])  # subdivide s1 into a and b
    c, d = int(s2[:subdiv]), int(s2[subdiv:])  # subdivide s2 into c and d


    c0 = karatsuba_mult(a, c)
    c2 = karatsuba_mult(b, d)
    a, b, c, d = str(a),str(b),str(c),str(d) #

    c1 = strsub(strsub(karatsuba_mult(stradd(a,b), stradd(c,d)),c0),c2)

    c1chunk = str(c1)
    c1chunk = zeros(c1chunk,split)

    c0chunk = str(c0)
    c0chunk = zeros(c0chunk,2*split)
    return int(c0chunk) + int(c1chunk) + c2


def zeros(s2,n):
    for i in range(n):
        s2 = s2 + "0"
    return s2


def exponentiate(a,n):  # evaluates a ** b using the karatsuba method
    if n == 0:
        return 1

    elif n % 2 == 0:
        temp = exponentiate(a, n / 2)  # this one will only get us to a ^ 1
        # print("Temp finalized in sec 1 at", temp)
        # print("Doing Karatsuba on",temp,temp)
        return karatsuba_mult(temp, temp)

    else:

        temp = exponentiate(a, (n - 1) / 2) # once we get to a ^ 1, we finally return 0 and work our way up.
        # print("Temp finalized in sec 2 at",temp)
        # print("Doing karatsuba on temp * temp and", a)
        return karatsuba_mult(karatsuba_mult(temp, temp), a)


def main():
    task = input("Select task:\n1. Karatsuba Multiplication.\n2. Exponentiation Utilizing Karatsuba Multiplication.")
    if task == "2":
        x = int(input("Input A:"))
        y = int(input("Input N:"))
        sol = exponentiate(x, y)
        print(x, "**", y, "=", sol)

    else:
        x = int(input("Input X:"))
        y = int(input("Input Y:"))
        sol = karatsuba_mult(x, y)
        print(x, "*", y, "=", sol)




main()