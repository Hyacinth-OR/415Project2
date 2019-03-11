def karatsuba_mult2(x,y):
    if x < 10 or y < 10:
        return x * y
    else:
        # Calculate the number of digits of the numbers
        sx, sy = str(x), str(y)
        m2 = max(len(sx), len(sy)) // 2
        # Split the digit sequences about the middle

        ix = len(sx) - m2
        iy = len(sy) - m2
        a, b = int(sx[:ix]), int(sx[ix:])
        c, d = int(sy[:iy]), int(sy[iy:])

        # 3 products of numbers with half the size
        c0 = karatsuba_mult2(a, c)
        c2 = karatsuba_mult2(b, d)
        c1 = karatsuba_mult2(a + b, c + d) - c0 - c2
        return c0 * 10 ** (2 * m2) + (c1 * 10 ** m2) + c2


def karatsuba_mult(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2

        a = x // 10 ** nby2
        b = x % 10 ** nby2
        c = y // 10 ** nby2
        d = y % 10 ** nby2

        ac = karatsuba_mult(a, c)
        bd = karatsuba_mult(b, d)
        ad_plus_bc = karatsuba_mult(a + b, c + d) - ac - bd

        prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd

        return prod

def exponentiation(a,n):
   if n == 0:
       return 1
   elif n % 2 == 0:
       temp = exponentiation(a,n//2)
       return karatsuba_mult(temp,temp)
   else:
       temp = exponentiation(a, (n - 1) // 2)
       print("doing",temp,"and",a)
       return karatsuba_mult2(karatsuba_mult2(temp,temp),a)

def main():
    task = input("Select task:\n1. Karatsuba Multiplication.\n2. Exponentiation Utilizing Karatsuba Multiplication.")
    if task == "2":
        x = int(input("Input A:"))
        y = int(input("Input N:"))
        sol = exponentiation(x, y)
        print(x, "**", y, "=", sol)
    else:
        x = int(input("Input X:"))
        y = int(input("Input Y:"))
        sol = karatsuba_mult2(x, y)
        print(x, "*", y, "=", sol)

main()