
from xmlrpc.client import boolean


def assertions(func):
    assert func("")==True
    assert func("a")==True
    assert func("ab")==True
    assert func("aab")==False
    assert func("aabbbcbsbd")==False
    assert func("abcdefghkp")==True

def isEqual(s: str)-> boolean:
    if len(s) < 2: return True
    table = {}
    for i in s:
        table[i] = 1 + table.get(i, 0)
        if table[i] == 2: return False
    return True

if __name__=="__main__":
    assertions(isEqual)
