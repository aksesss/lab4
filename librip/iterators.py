# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if type(items) is list:
            self.item = iter(items)
        elif str(type(items)) == '<class \'generator\'>':
            self.item = items
        else:
            print("Класс Unique принимает на вход list или generator, а не" + str(type(items)))
            raise TypeError
        self.unique_item_list = []
        self.ignore_case = kwargs.get('ignore_case')

    def _IsUnique(self, item):
        if self.ignore_case:
            str(item)
            item = item.lower()
            if item in self.unique_item_list:
                return False
            else:
                self.unique_item_list.append(item)
                return True
        else:
            if item in self.unique_item_list:
                return False
            else:
                self.unique_item_list.append(item)
                return True

    def __next__(self):
        value = next(self.item)
        while not self._IsUnique(value):
            value = next(self.item)
        return value

    def __iter__(self):
        return self
