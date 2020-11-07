def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
