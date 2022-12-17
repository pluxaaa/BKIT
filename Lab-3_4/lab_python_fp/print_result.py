def print_result(func):
    def wrapper(*args, **kwargs):
        funcInn = func(*args, **kwargs)
        print()
        print(func.__name__)
        if type(funcInn) == list:
            for i in funcInn:
                print(i)

        if type(funcInn) == dict:
            for k, v in funcInn.items():
                print(k, ' = ', v)

        else:
            print(funcInn)

        return funcInn

    return wrapper


# @print_result
# def test_1():
#     return 1
#
#
# @print_result
# def test_2():
#     return 'iu5'
#
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
#
# @print_result
# def test_4():
#     return [1, 2]
#
#
# if __name__ == '__main__':
#     print('!!!!!!!!')
#     test_1()
#     test_2()
#     test_3()
#     test_4()