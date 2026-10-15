

def decor(x):
    def inner(a,b,c):
        a = a + 5
        b = b + 5
        c = c + 5
        z = x(a,b,c)
        return z
    return inner
@decor
def outer(x, y, z):
    return x + y + z

print(outer(5,5,5))