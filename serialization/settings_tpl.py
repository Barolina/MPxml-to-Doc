"""
    Настройка для генерации результирующего файла.
    Все блоки(разделы) печатного варианта мп, должны следовать в определенном порядке
    Для кадого раздела указываться \n
     tpl: шаблон для рендеринга \n
     pos_doc: позиция блока в результирующе печатном варианте \n
     class: класс для получения источника данных \n
     clear: удалять узлы, после прохождения по xml, данный атрибут на дынный момент важен, пока  не придумано обхода, \n
        к примеру элемент ProvidingPassCadastralNumbers  - скажем таки размазан по всему файлу xml  \n
"""
from serialization.element_to_dict import *

BINDER_FILE = {
    'GeneralCadastralWorks': {
        'tpl': 'title.docx',
        'pos_doc': '1.',
        'class': XmlTitleDict,
        'clear': True,
    },
    'InputData': {
        'tpl': "inputdata.docx",
        'pos_doc': '2.',
        'class': XmlInputDataDict,
        'clear': True,
    },
    'Survey': {
        'tpl': "survey.docx",
        'pos_doc': '3.',
        'class': XmlSurveyDict,
        'clear': True,
    },
    'NewParcel': {
        'tpl': "newparcel.docx",
        'pos_doc': '4.',
        'class': XmlNewParcel,
        'clear': False, #есть присутствие ProvidingPassCadastralNumbers
    },
    'ExistParcel': {
        'tpl': "existparcel.docx",
        'pos_doc': '4.',
        'class': XmlExistParcel,
        'clear': False, #есть присутствие ProvidingPassCadastralNumbers
    },
    'SubParcels': {
        'tpl': "subparcels.docx",
        'pos_doc': '6.',
        'class': XmlSubParcels,
        'clear': False, #есть присутствие ProvidingPassCadastralNumbers
    },
    'ChangeParcel': {
        'tpl': "changeparcel.docx",
        'pos_doc': '5.',
        'class': XmlChangeParcel,
        'clear': False, #есть присутствие ProvidingPassCadastralNumbers
    },
    'SpecifyRelatedParcel': {
        'tpl': 'existparcel.docx',
        'pos_doc': '6.',
        'class': XmlExistParcel,
        'clear': False, #есть присутствие ProvidingPassCadastralNumbers
    },
    'FormParcels': {
        'tpl': 'providing.docx',
        'pos_doc': '9.',
        'class': XmlNewParcelProviding,
        'clear': True,
    },
    'ExistEZParcels': {
        'tpl': 'existparcel.docx',
        'pos_doc': '7.',
        'class': XmlExistParcel,
        'clear': True,
    },
    'ExistEZEntryParcel': {
        'tpl': 'existparcel.docx',
        'pos_doc': '8.',
        'class': XmlExistParcel,
        'clear': True,
    },
    'Conclusion': {
        'tpl': 'conclusion.docx',
        'pos_doc': '99.',
        'class': XmlConclusion,
        'clear': True,
    }
}
