def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error, you tried to divide by zero')

print(div42by(int(input('type some shit: '))))