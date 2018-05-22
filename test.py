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
       qweqwe

        :param node - ewrwer
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
        sdfswerwe
    """

    # @staticmethod
    def type_ordinate(node):
        """
            kdfgljdfgdsggfsdfg

        :param node:wer  wer
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
