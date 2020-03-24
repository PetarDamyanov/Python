import json
import xml.etree.ElementTree as ET

# Mixins
class Jsonable(object):
	def to_json(self,inent=4):
		d=self.__dict__
		d["type"]=type(self).__name__
		json_data=json.dumps(d,indent=indent)
		# print(json_data)
		return str(json_data)

	def from_json(json_string):
		json_data=json.dumps(json_string)
		print(json_data)
class Xmlable(object):
	def to_xml(self):
		d=self.__dict__
		d["type"]=type(self).__name__
		s=""
		for x in d:
			s			
		return "<{0}><{1}>{2}</{1}></{0}>".format(type(self).__name__,'name',self.name)



		return 
		# ET.dump(self)
	def from_xml(xml_string):
		ET.fromstring(xml_string)

