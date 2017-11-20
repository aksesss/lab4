def print_result(func_to_decorate):
    def decorated_func(*args):
        result = func_to_decorate(*args)
        print(func_to_decorate.__name__)
        if type(result) in (str, int):
            print(result)
        if type(result) is list:
            print(*result,sep=' \n')
        if type(result) is dict:
            for x, y in result.items():
                print('{} = {}'.format(x, y))
        return result

    return decorated_func
