"""
    Summa chisel
    Сумма чисел
"""


def sum(a, b):
    """
        sum two nubers

    :param a: numbers
    :param b: numbers
    :return: number
    """
    return a+b



CNST_NEWPARCEL = 'newparcel'
CNST_EXISTPARCEL = 'existparcel'
CNST_UNDEFINE = 'undefine'

META_TPL_ORDINATE = {  # шаблон для пребразвоания в вордовском tpl
    CNST_EXISTPARCEL: ['', ] * 7, # 7-кол-во колонок в таблице на уточнение
    CNST_NEWPARCEL: ['', ] * 5, # 5 кол-во колонок в таблице  на образование
    CNST_UNDEFINE: '',
}


class XMLElemenBase:
    """
        Базовый класс - определяющий структуру наследников

        :param node - на вход узел дерева
        :return  json(object)
    """
    def __init__(self, node):
        self.node = node

    def to_dict(self):
        """
            Return json - object, based on the dictionary in config
            (данные метод реализован у всех наследников, необходимых для render шааболонов)

        :return: json()
        """
        pass
