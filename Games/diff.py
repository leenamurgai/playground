from collections import defaultdict

def func(x):
    return x + 1

def diff(arg1, arg2):
    """return first difference between the args if there is one,
    else return None"""

    # check if the types of arg1 and arg2 are the same
    if type(arg1) != type(arg2):
        return arg1, arg2

    # if args aren't a list or a dict just compare
    if type(arg1) != dict and type(arg1) != list:
        if arg1 != arg2:
            return arg1, arg2

    # if type args are lists
    if type(arg1) == list:
        for idx, elt in enumerate(arg1):
            if diff(elt, arg2[idx]) != None:
                return diff(elt, arg2[idx])

    # if type args are dicts
    if type(arg1) == dict:
        print(arg1, arg2)
        if diff(sorted(list(arg1.keys())), sorted(list(arg2.keys()))) != None:
            return diff(sorted(list(arg1.keys())), sorted(list(arg2.keys())))
        for k, v in arg1.items():
            if arg2[k] != v:
                return arg1, arg2
    return None

dict1 = {'a':1, 'b':2}
dict2 = {'c':2, 'd':3}
print('==', dict1 == dict2)
