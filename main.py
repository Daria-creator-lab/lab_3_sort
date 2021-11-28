# 	выборкой + yaml
# This Python file uses the following encoding: utf-8
import json
import yaml
from pprint import pprint


class to_write_from:
    '''
    Объект класса to_write_from читает данные с файла.

    Он нужен для того, чтобы считать данные с файла.

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


def selection_sort(data: list, flag: str) -> list:
    '''
    Выполняет сортировку выбором.

    Сортируются наборы данных по заданному параметру.

    Parameters
    ----------
        data : list
             Список словарей, которые будем сортировать.
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

def de_serialization(sort_data: list) -> None:
    '''
    Выполняет сериализацию и десериализацию отсортированного набора данных.

    Parameters
    ----------
        sort_data : list
             Список словарей, которые нужно записать в файл.
    Returns
    -------
        None:
            Ничего не возвращает.
    '''
    with open('sort.yaml', mode='w', encoding='utf8') as f:
        yaml.dump(sort_data, f, default_flow_style=False)
    with open('sort.yaml', encoding='utf8') as f:
        templates = yaml.safe_load(f)
    pprint(templates)



valid_data = to_write_from(r'/Users/dary/PycharmProjects/прикладное_программирование_лаба2/new_28.txt')
sort_data = selection_sort(valid_data._data[0:5], 'height')
de_serialization(sort_data)


