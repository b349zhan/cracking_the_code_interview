def assertions(func):
    assert func("", "")==True
    assert func("", "a")==False
    assert func("a", "a")==True
    assert func("abce", "ebca")==True
    assert func("abchehdhajda", "hajdaabchehd")==True
    assert func("adjisadm", "sjiadona")==False
    assert func("adjisadm", "a")==False

def check_permutations(s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False
    d1, d2 = {}, {}
    for i in range(len(s1)):
        d1[s1[i]] = d1.get(s1[i], 0) + 1
        d2[s2[i]] = d2.get(s2[i], 0) + 1
    if d1 == d2: return True
    return False


if __name__=="__main__":
    assertions(check_permutations)