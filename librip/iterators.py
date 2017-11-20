# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if type(items) is list:
            self.item = iter(items)
        elif str(type(items)) == '<class \'generator\'>':
            self.item = items
        else:
            raise TypeError("Класс Unique принимает на вход list или generator, а не " + str(type(items)))
        self.unique_item_list = []
        self.ignore_case = kwargs.get('ignore_case')

    def _is_unique(self, item):
        if self.ignore_case:
            item = str(item)
            item = item.lower()
        if item in self.unique_item_list:
            return False
        else:
            self.unique_item_list.append(item)
            return True

    def __next__(self):
        value = next(self.item)
        while not self._is_unique(value):
            value = next(self.item)
        return value

    def __iter__(self):
        return self
