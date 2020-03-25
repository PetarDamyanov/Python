import json
from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as et

class ClsEncode(json.JSONEncoder):
        def default(self, o):
            return o.__dict__


class WithSetAttributes:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


class WithEqualAttributes:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Jsonable:
    def to_json(self, indent=4):
        name = self.__class__.__name__

        attributes = self.__dict__
         
        return json.dumps({'type': name, 'dict': attributes}, indent=indent)



    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)

        class_name = data['type']

        if class_name != cls.__name__:
            raise ValueError('Wrong type.')

        attributes = data['dict']

        return cls(**attributes)

class XMlAble:
    def to_xml(self):
        elem = Element(self.__class__.__name__)
        for key, val in self.__dict__.items():
            child = Element(key)
            child.text = str(val)
            elem.append(child)
        return elem

    @classmethod
    def from_xml(cls,xml_string):
        data = et.fromstring(xml_string)

        class_name = data.tag

        if class_name != cls.__name__:
            raise ValueError('Wrong type.')

        attributes = {}
        for x in data:
            attributes[x.tag]=x.text

        return cls(**attributes)
