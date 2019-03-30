

def equalize(str1,str2):

    if len(str1) > len(str2):

        for i in range(len(str1) - len(str2)):
            str2 = '0' + str2
            return str1, str2

    elif len(str1) < len(str2):
        for i in range(len(str2)- len(str1)):
            str1 = '0' + str1
            return str1, str2
    else:
        return str1, str2

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
    c1 = karatsuba_mult(a+b, c+d) - c0 - c2
    return c0 * 10 ** (2 * split) + (c1 * 10 ** split) + c2


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