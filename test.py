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

"""
    Serialization xml ordinate
    Сериализация  узлов xmk файла с коорлинатами
"""
# from utils import config as cnfg
# from utils.xsd import value_from_xsd
# import os
# from lxml.etree import _Element
# import logging
#
# # fileConfig('loggers/logging_config.ini')
# logger = logging.getLogger()

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


class StaticMethod:
    """
        Вспомогательный класс для работы  c node xml
    """

    # @staticmethod
    def type_ordinate(node):
        """
            Определени типа  коорлинат - на  образование или на уточнение

        :param node:
        :return: ExistOrdinate ot NewOrdinate
        """
        isExist = CNST_UNDEFINE
        initial_node = None
        if node is not None:
            # may come  Element
            if isinstance(node, _Element):
                initial_node = node
                # may come a List
            elif isinstance(node, list) and node[0] is not None:
                initial_node = node[0]
            # get a type  of ordinates
            if initial_node is not None:
                isOrdinate = initial_node.find('.//Ordinate')
                isExistSubParcel = True if len(initial_node.xpath('ancestor::*[name() = "SpecifyRelatedParcel" or '
                                                                  'name() = "ExistSubParcel"]')) > 0\
                                           or initial_node.tag == 'ExistSubParcel' else False
                isExist = CNST_EXISTPARCEL if ((isOrdinate is None) or isExistSubParcel) else CNST_NEWPARCEL
        return isExist

    # @staticmethod
    def get_empty_tpl(node):
        """
        :param node: node
        :return: Return empty tpl rows  for word, depends on Type Ordinate
        """
        if node is not None:
            name_type_ord = StaticMethod.type_ordinate(node)
            return META_TPL_ORDINATE[name_type_ord]
        return None

    # @staticmethod
    def merge_array_list(key, array_value):
        """
            преобразоание  списков ключей и массива значений в словарь

        :param key: ключи словаря
        :param array_value: массив значений
        :return:  [{ 'id': 1, 'name': 'ЗУ1'}, { 'id': 1, 'name': 'ЗУ1'},]
        """
        res = list()
        if key and array_value:
            for _ in array_value:
                res.append(dict(zip(key, _)))
        return res

    # @staticmethod
    def xml_key_to_text(node, path, name_xsd):
        """
            получение знсачения ноды по ключу из справоника

        :param node:  узел - где ищем
        :param path: парсер - что(как) ищем
        :param name_xsd: наименование сравочнка
        :return: text
        """
        if not name_xsd:
            logging.error(f"""Не передан справочник {name_xsd}""")
            return ''
        _list = node.xpath(path)
        res = ''
        if _list:
            path = os.path.join(cnfg.PATH_XSD, name_xsd)
            res = value_from_xsd(path, _list[0])
            node.clear()
        return res
