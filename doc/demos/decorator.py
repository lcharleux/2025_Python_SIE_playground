def printmyargs(func):
    def newfunc(*args, **kwargs):
        print("args=", args)
        print("kwargs=", kwargs)
        return func(*args, **kwargs)
    return newfunc

@printmyargs
def dummyfunc(x):
    return x**2

dummyfunc(33)
dummyfunc(x=666)