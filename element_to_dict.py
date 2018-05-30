"""
  Сериализция основных блоков мп - xmk\n
  Основные блоки:\n
  Титульный лист,\n
  Исходные данные,\n
  Средства об измерениях,\n
  Сведения об обрузуемых зу и их частях,\n
  Сведения об уточняемом учатске и частях,\n
  Сведения об измененных учасках и их частях,\n
  Единое землепользование,\n
  Сведения о земельных участках, посредством которых обеспечивается доступ,\n
  Заключение кадастрового инженера \n
  
"""
from serialization.basic import *
from utils.xsd import value_from_xsd
from datetime import datetime
# import logging
# from logging.config import fileConfig
# fileConfig('loggers/logging_config.ini')
# logger = logging.getLogger()

def test():
	"""
	test
	
	"""
	print("sdfasdf")



class XmlTitleDict:
    """
		Формированяи словаря для титульника

    """
    def __init__(self, node):
        """
		
        :param node: GeneralCadastralWorks
        """
        self.node = node
        self.contractor = None

    def __children_dict(self, node, *args):
        """

        :param node: Contractor/child
        :return: dict (node.tag : node.text)
        """
        res = dict()
        for el in node:
            res[el.tag] = el.text
        return res

    def __contractor(self):
        if not self.contractor:
            return self.__children_dict(self.node.xpath('Contractor/child::*'))
        return self.contractor

    def __xml_reason_to_text(self):
        return ''.join(self.node.xpath('Reason/text()'))

    def __xml_purpose_to_text(self):
        return ''.join(self.node.xpath('Purpose/text()'))

    def __xml_client_to_text(self):
        return ' '.join(self.node.xpath('Clients/*[1]/child::*/node()/text()'))

    def __xml_contrsactor_fio_to_text(self):
        _ = self.__contractor()
        if _:
            return f"{_.get('FamilyName', '')} " \
                   f"{_.get('FirstName', '')} " \
                   f"{_.get('Patronymic', '')}"
        return ''

    def __xml_ncertificate_to_text(self):
        _ = self.__contractor()
        if _:
            return _.get('NCertificate', '')
        return ''

    def __xml_telefon_to_text(self):
        _ = self.__contractor()
        if _:
            return _.get('Telephone', '')
        return ''

    def __xml_email_to_text(self):
        _ = self.__contractor()
        if _:
            return _.get('Email', '')
        return ''

    def __xml_address_to_text(self):
        _ = self.__contractor()
        if _:
            return _.get('Address', '')
        return ''

    def __xml_organization_to_text(self):
        return ' '.join(self.node.xpath('Contractor/Organization/node()/text()'))

    def __xml_data_to_text(self):
        _dt = datetime.strptime(dict(self.node.attrib).get('DateCadastral'), "%Y-%m-%d")
        if _dt:
            # return  f"""{_dt:%d.%m.%Y}"""
            pass
        return ''

    def to_dict(self):
        """
		Данный  метод  возвращает словарь значения для  заполнения  шаблона title.docx

		:return: dict->cnfg.Title
        """
        result = None
        try:
            value_title = [self.__xml_reason_to_text(), self.__xml_purpose_to_text(),
                           self.__xml_client_to_text(), self.__xml_contrsactor_fio_to_text(),
                           self.__xml_ncertificate_to_text(), self.__xml_telefon_to_text(), self.__xml_address_to_text(),
                           self.__xml_email_to_text(), self.__xml_organization_to_text(), self.__xml_data_to_text()]
            result = dict(zip(cnfg.TITLE.attr, value_title))
        except Exception as e:
            # logger.error(f""" Ошибки при формировании титульника {e} """)
            pass
        else:
            # logger.info(f"""Словарь титульного {result}""")
            pass
        return result

