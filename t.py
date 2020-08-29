def mul_2(v):
    return v*2


def func(a,b):
    if a+b == 10:
        return 42
    else:
        return 13

def mygen(a,b,c):
    yield "111"

if __name__ == '__main__':
    gen = mygen(1,2,3)
    assert next(gen) == '111'
    assert next(gen) == 'aaaa'
    assert next(gen) == 'cCccc'

