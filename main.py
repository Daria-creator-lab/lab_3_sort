# 	выборкой + yaml
import json
from operator import attrgetter

class to_write_from:
    '''
    Объект класса to_write_from читает данные с файла.

    Он нужен для того, чтобы считать и записать данные с файла.

    Attributes
    ----------
        _data : list
            Список словарей, в котором будут хранится записи из файла
    '''
    _data: list

    def __init__(self, path: str) -> None:
        '''
        Инициализирует экземпляр класса to_write_from.

        Parameters
        ----------
            path : str
                Строковый параметр: путь до открываемого файла
        '''
        self._data = json.load(open(path, encoding='utf-8'))
    # def my_min(self, left, right) -> dict:
    #     '''
    #             Выполняет сортировку выбором валидных записей.
    #
    #             Если запись валидна,то записывается в __valid.
    #
    #             Parameters
    #             ----------
    #                 left : str
    #                     Строка с видом парметра (рост/серия паспорта/СНИЛС/возраст).
    #                 right
    #             Returns
    #             -------
    #                 None:
    #                     Ничего не возвращает
    #             '''
    def selection_sort(self, flag: str) -> None:
        '''
        Выполняет сортировку выбором валидных записей.

        Если запись валидна,то записывается в __valid.

        Parameters
        ----------
            flag : str
                Строка с видом парметра (рост/серия паспорта/СНИЛС/возраст).
        Returns
        -------
            None:
                Ничего не возвращает
        '''
        for i in range(len(self._data) - 1):
            current_elem = self._data[i]
            min_index = i
            for j in range(i + 1, len(self._data)):

                # if self._data[j][flag] < self._data[min_index][flag]:
                #     min_index = j
                if min(self._data[j], self._data[min_index],
                       key=attrgetter(flag)) != self._data[min_index]:
                    min_index = j
            self._data[i] = self._data[min_index]
            self._data[min_index] = current_elem
        # for i in self._data:
        #     current_elem = i
        #     mn = min(self._data[i].values())
        #     # mn = min(range(i, len(self._data)), key=i[flag])
        #     self._data[i] = self._data[mn]
        #     self._data[mn] = current_elem
        # return self._data


B = to_write_from(r'/Users/dary/PycharmProjects/прикладное_программирование_лаба2/new_28.txt')
# print(B._data[0:2])
B.selection_sort('age')
print(B._data[0])