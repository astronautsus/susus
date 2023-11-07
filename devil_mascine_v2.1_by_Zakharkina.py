print('Hello I am the misterious creatue from hell. I can count almost anything you want.')
f = 'yes'
while f == 'yes':
    print('options:')
    print('summation(+)')
    print('subtraction(-)')
    print('multiplication(*)')
    print('division(/)')
    print('integer division(//)')
    print('remainder(%)')
    print('root(/*)')
    print('exponentiation(**)')
    print('conversion to decimal notation(#)')
    print('analize(@)')
    print('What do you want? Please print "+" or "-" or "*" or "/" or "%" or "//" or "**" or "/*" or "#" or "@"')
    e = input()
    if e == '+':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And the second one')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
        t = float(t)
        g = float(g)
        print(t + g)
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '-':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And the second one')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
        t = float(t)
        g = float(g)
        print(t - g)
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '*':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And the second one')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
        t = float(t)
        g = float(g)
        print(t * g)
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '/':
        print('Add one number')
        t = float(input())
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
            print('And the second one')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
        if g == 0:
            print('Nobody can devide by zero, even me')
            g = float(input())
        t = float(t)
        g = float(g)
        print(t / g)
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '**':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And the exponent for it')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
        t = float(t)
        g = float(g)
        print(t ** g)
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '/*':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And the root for it')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
        t = float(t)
        g = float(g)
        print(t ** (1 / g))
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '//':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And the second one')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
        if g == 0:
            print('Nobody can devide by zero, even me')
            g = float(input())
        t = float(t)
        g = (g)
        print(t // g)
        print('Is it okayfloat? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '%':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And the second one')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
            print('Please do it correctly')
        if g == 0:
            print('Nobody can devide by zero, even me')
            g = float(input())
        t = float(t)
        g = float(g)
        print(t % g)
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '#':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('And it`s number system')
        g = input()
        while '1' not in g and '2' not in g and '3' not in g and '4'not in g and '5' not in g and\
                '6' not in g and '7' not in g and '8' not in g and '9'not in g and '0' not in g:
            print('Please do it correctly')
            g = input()
            print('Please do it correctly')
        t = int(t)
        g = int(g)
        print(int(str(t), g))
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    elif e == '@':
        print('Add one number')
        t = input()
        while '1' not in t and '2' not in t and '3' not in t and '4'not in t and '5' not in t and\
                '6' not in t and '7' not in t and '8' not in t and '9'not in t and '0' not in t:
            print('Please do it correctly')
            t = input()
        print('~ length:', len(t))
        t = int(t)
        tu = t
        if  tu == 0:
            print('~ number of different digits:')
            print('1 :', 0)
            print('2 :', 0)
            print('3 :', 0)
            print('4 :', 0)
            print('5 :', 0)
            print('6 :', 0)
            print('7 :', 0)
            print('8 :', 0)
            print('9 :', 0)
            print('0 :', 1)
        else:
            a = 0
            b = 0
            c = 0
            d = 0
            x = 0
            y = 0
            u = 0
            h = 0
            i = 0
            j = 0
            while tu!= 0:
                if tu % 10 == 1:
                    a = a + 1
                elif tu % 10 == 2:
                    b = b + 1
                elif tu % 10 == 3:
                    c = c + 1
                elif tu % 10 == 4:
                    d = d + 1
                elif tu % 10 == 5:
                    x = x + 1
                elif tu % 10 == 6:
                    y = y + 1
                elif tu % 10 == 7:
                    u = u + 1
                elif tu % 10 == 8:
                    h = h + 1
                elif tu % 10 == 9:
                    i = i + 1
                elif tu % 10 == 0:
                    j = j + 1
                tu = tu // 10
        print('~ number of different digits:')
        print('1 :', a)
        print('2 :', b)
        print('3 :', c)
        print('4 :', d)
        print('5 :', x)
        print('6 :', y)
        print('7 :', u)
        print('8 :', h)
        print('9 :', i)
        print('0 :', j)
        if t % 2 == 0:
            print('~ this is an even number')
        else:
            print('~ this is not an even number')
        tg = t
        if tg == 0:
             print('~ the summ of the digits of the number = 0')
        else:
            z = 0
            while tg != 0:
                z = z + tg % 10
                tg = tg // 10
            print('~ the summ of the digits of the number =', z)
        om = 1
        re = 0
        if t == 0:
            print('~ the divisors of this number:')
            print('all numbers')
        elif t == 1:
            print('~ it is a prime number')
        else:
            while t != om:
                if t % om == 0:
                    re = re + 1
                om = om + 1
            if re == 1:
                  print('~ it is a prime number')
            else:
                om = 1
                print('~ the divisors of this number:')
                while t // om != 1:
                    if t % om == 0:
                        print(om)
                    om = om + 1
                print(t)
        ho = t ** (1 / 2)
        if round(ho) ** 2 == t:
            print('~', t, 'is a square of', ho)
        else:
            print('~', t, 'is not a square of any number')
        ho = t ** (1 / 3)
        if round(ho) ** 2 == t:
             print('`', t, 'is a cube of', ho)
        else:
             print('~', t, 'is not a cube of any number')
        print('Is it okay? Print "yes" or "no"')
        f = input()
        if f == 'yes':
            print(':)')
        elif f == 'no':
            print(':(')
        else:
            print('Please do it correctly')
        print('Wanna continue? print "yes" or "no"')
        f = input()
        while f != 'yes' and f != 'no':
            print('Please do it correctly')
            f = input()
    else:
        print('Please do it correctly')
print('Already leaving? Have a good day, come back soon <3')

    
