def isogram_test(string:str)->bool:

    string = string.lower()
    return len(set(string))==len(string)


