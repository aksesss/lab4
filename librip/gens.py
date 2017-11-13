import random


def field(items_list, *args):
    if args is None:
        print("Вы не передали назвония полей")
        return

    if len(items_list) == 0:
        print("Вы передали пустой лист")
        return

    b = bool

    if len(args) == 1:
        for item_dict in items_list:
            if item_dict[args[0]] is not None:
                yield item_dict[args[0]]
    else:
        for item_dict in items_list:
            dictionary = {}
            for arg in args:
                if item_dict.get(arg) is not None:
                    b = True
                    dictionary[arg] = item_dict.get(arg)
                else:
                    b = False
            if b:
                yield dictionary
            else:
                continue


def gen_random(begin, end, num_count):
    # На входе int int int на выходе gen ( int )
    for i in range(num_count):
        yield random.randint(begin, end)
