# 	выборкой + yaml
# This Python file uses the following encoding: utf-8
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

    # def selection_sort(self, flag: str) -> None:
    #     '''
    #     Выполняет сортировку выбором валидных записей.
    #
    #     Если запись валидна,то записывается в __valid.
    #
    #     Parameters
    #     ----------
    #         flag : str
    #             Строка с видом парметра (рост/серия паспорта/СНИЛС/возраст).
    #     Returns
    #     -------
    #         None:
    #             Ничего не возвращает
    #     '''
        # for i in range(len(self._data) - 1):
        #     current_elem = self._data[i]
        #     min_index = i
        #     for j in range(i + 1, len(self._data)):
        #         if min(self._data[j][flag], self._data[min_index][flag]) != self._data[min_index][flag]:
        #             min_index = j
        #     self._data[i] = self._data[min_index]
        #     self._data[min_index] = current_elem

def selection_sort(data, flag: str) -> list:
    '''
    Выполняет сортировку выбором валидных записей.

    Parameters
    ----------
        flag : str
            Строка с видом парметра (рост/серия паспорта/СНИЛС/возраст).
    Returns
    -------
        list:
            Возвращает список отсортированных словарей.
    '''
    for i in range(len(data) - 1):
        current_elem = data[i]
        min_index = i
        for j in range(i + 1, len(data)):
            if min(data[j][flag], data[min_index][flag]) != data[min_index][flag]:
                min_index = j
        data[i] = data[min_index]
        data[min_index] = current_elem
    return data


B = to_write_from(r'/Users/dary/PycharmProjects/прикладное_программирование_лаба2/new_28.txt')
# print(B._data[0:5])
# B.selection_sort('age')
# print(B._data[0])

# A = [{'telephone': '+7-(968)-048-23-86', 'height': '1.70', 'snils': '20800731719', 'passport_number': 717278, 'occupation': 'Ассистент менеджера по продажам', 'age': 40, 'academic_degree': 'Бакалавр', 'worldview': 'Буддизм', 'address': 'Аллея Яуза Платформа 1010'}, {'telephone': '+7-(909)-551-92-23', 'height': '1.67', 'snils': '69023345894', 'passport_number': 292027, 'occupation': 'Энергетик', 'age': 19, 'academic_degree': 'Магистр', 'worldview': 'Агностицизм', 'address': 'Аллея Генерала Кузнецова 99'}, {'telephone': '+7-(901)-152-03-79', 'height': '1.66', 'snils': '07363492276', 'passport_number': 388912, 'occupation': 'Машинистка', 'age': 22, 'academic_degree': 'Кандидат наук', 'worldview': 'Атеизм', 'address': 'Аллея Землянская 652'}, {'telephone': '+7-(926)-351-52-30', 'height': '1.87', 'snils': '86837825479', 'passport_number': 310302, 'occupation': 'Стоматолог', 'age': 47, 'academic_degree': 'Бакалавр', 'worldview': 'Деизм', 'address': 'Аллея Серпуховская Застава 788'}, {'telephone': '+7-(968)-784-67-63', 'height': '1.56', 'snils': '10125951914', 'passport_number': 757433, 'occupation': 'Оценщик', 'age': 32, 'academic_degree': 'Доктор наук', 'worldview': 'Деизм', 'address': 'Аллея Изумрудная 737'}]
print(selection_sort(B._data[0:5], 'age'))
