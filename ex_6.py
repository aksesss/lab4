import json
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = r"data_light_cp1251.json"

with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(unique((field(arg, 'job-name')), ignore_case=True), key=str.lower)


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('Программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом работы Python', arg))


@print_result
def f4(arg):
    return list('{}, зарплата {} руб'.format(x, y) for x, y in zip(arg, list(gen_random(100000, 200000, len(arg)))))


with timer():
    f4(f3(f2(f1(data))))
