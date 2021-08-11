# from sys import stdin as In

all_num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decitoany(n1, val):
    box = []
    b = 0;
    height = 0
    # numeric part
    num1 = n1 // 1
    while num1 > 0:
        b = int(num1 % val)
        if b > 9:
            b += 55
            b = chr(b)
        box.append(b)
        num1 //= val
        height += 1
    box.reverse()
    # fractional part (after the decimal point--if present)
    f1 = n1 % 1
    if f1 > 0:
        box.append('.')
        for i in range(8):  # 4 decimal points
            f1 *= val
            b = int(f1)
            if b > 9:
                b += 55
                b = chr(b)
            box.append(b)
            if f1 >= 1:
                f1 %= 1
    return box,val
    


def anytodeci(n1, val):
    import string
    if isinstance(n1, str):
        n1, n2 = n1.split('.')
        power = len(n1) - 1
        box = 0
        for i, num in enumerate(n1):
            if num in string.ascii_letters:
                n = ord(num)
                if n > 96:
                    n = n - 97
                else:
                    n = n - 65
                n += 10
                num = n
            box += int(num) * (val ** (power - i))

        for i, num in enumerate(n2, 1):
            if num in string.ascii_letters:
                n = ord(num)
                if n > 96:
                    n = n - 97
                else:
                    n = n - 65
                n += 10
                num = n
            # print('_num:',num)
            box += int(num) / (val ** i)

        # print('_box:', box)
        return box
    else:
        from math import log10
        i = int(log10(n1))
        # print('i=',i)
        box = 0
        while i >= 0:
            num = n1 / (10 ** i)
            num = int(num % 10)
            # print(num)
            box += (num * (val ** i))
            i -= 1

        f1 = n1 % 1
        if f1 > 0:
            j = 1
            f1 *= 10000  # to get 4 digits after decimal
            for i in range(3, -1, -1):
                num = int(f1 / (10 ** i))
                num %= 10
                box += num / (val ** j)
                j += 1
        return box

def isbase(number,x):
    x_base = set(all_num[:x])
    for i in number:
        if i not in x_base and i!='.':
            return False
    return True


if __name__ == '__main__':
    # n1=5637.5340;b1=8;b2=16    #initial decimal number and base
    i = 0
    while i == 0:
        n1 = input('\nnum : ')
        b1 = int(input('base of the value given : '))
        b2 = int(input('base2 be converted to:'))

        # print('\nnum : ', end=""); n1 = str(In.readline())[:-1]         # type of variable
        # print('base1 : ', end=""); b1 = int(In.readline())
        # print("base2 : ", end=""); b2 = int(In.readline())              # type to be converted

        if '.' not in n1:
            n1+='.0'

        if not isbase(n1,b1) :
            print("\n number",n1,"does not belong to base",b1," format :( ")
            continue

        if b1 <= 10:
            n1 = float(n1)


        # breakpoint()
        if b1 == 10:
            decitoany(n1, b2)
            print(" \n({})b{} -->".format(n1, 10), end=" ")
            print("(", "".join(str(i) for i in b), ")b{}".format(v))
        elif b2 == 10:
            box = anytodeci(n1, b1)
            print(" \n({})b{} -->".format(n1, b1), end=" ")
            print("(", "".join(str(box)), ")b{}".format(10))
        else:
            box = anytodeci(n1, b1)
            b,v=decitoany(box, b2)
            print(" \n({})b{} -->".format(n1, b1), end=" ")
            print("(", "".join(str(box)), ")b{}".format(10), "-->", end=" ")
            print("(", "".join(str(i) for i in b), ")b{}".format(v))
