def lambdaSort(lst):
    return sorted(lst, key=lambda x: abs(x), reverse=True)


def no_lambdaSort(lst):
    return sorted(lst, key=abs, reverse=True)
