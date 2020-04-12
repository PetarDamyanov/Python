from pprint import pprint
import unittest
import json
from xml.etree.ElementTree import tostring

from mixin import Jsonable, WithSetAttributes, WithEqualAttributes,XMlAble


class Panda(Jsonable, WithSetAttributes, WithEqualAttributes,XMlAble):
    pass


class Car(Jsonable, WithSetAttributes, WithEqualAttributes):
    pass

class TestJsonable(unittest.TestCase):
    def test_to_json_returns_empty_json_for_objects_with_no_arguments(self):
        panda = Panda()

        result = panda.to_json(indent=4)
        expexted = {
            'type': Panda.__name__,
            'dict': {}
        }

        self.assertEqual(result, json.dumps(expexted, indent=4))

    def test_to_json_returns_correct_json_with_arguments(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            food=['bamboo', 'grass'],
            skills={'eat': 100, 'sleep': 200}
        )

        panda_result = panda.to_json(indent=4)
        panda_expexted = {
            'type': Panda.__name__,
            'dict': {
                'name': 'Marto',
                'age': 20,
                'weight': 100.10,
                'food': ['bamboo', 'grass'],
                'skills': {'eat': 100, 'sleep': 200}
            }
        }

        self.assertEqual(panda_result, json.dumps(panda_expexted, indent=4))

    # def test_to_json_returns_correct_json_with_arguments_of_jsonable_type(self):
    #     panda = Panda(name='Marto', friend=Panda(name='Ivo'))

    #     panda_result = panda.to_json(indent=4)
    #     panda_expexted = {
    #         'type': Panda.__name__,
    #         'dict': {
    #             'name': 'Marto',
    #             'friend': {
    #                 'type': Panda.__name__,
    #                 'dict': {
    #                     'name': 'Ivo'
    #                 }
    #             }
    #         }
    #     }
    #     # print(json.dumps(panda, default=lambda o: o.__dict__,indent=4))
    #     self.assertEqual(panda_result, json.dumps(panda_expexted, indent=4))

    def test_from_json_with_wrong_class_type(self):
        car = Car()
        car_json = car.to_json()

        with self.assertRaises(ValueError):
            Panda.from_json(car_json)

    def test_from_json_with_no_arguments(self):
        car = Car()
        car_json = car.to_json()

        result = Car.from_json(car_json)

        self.assertEqual(car, result)

    def test_from_json_with_arguments(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            food=['bamboo', 'grass'],
            skills={'eat': 100, 'sleep': 200}
        )
        panda_json = panda.to_json()

        result = Panda.from_json(panda_json)

        self.assertEqual(panda, result)


class TestXmlable(unittest.TestCase):
    def test_xmlable_with_empty_class(self):
        panda = Panda()

        result = panda.to_xml()
        expexted = b"<Panda />"

        self.assertEqual(tostring(result), expexted)

    def test_xmlable_with_class(self):
        panda = Panda(name="Pesho")

        result = panda.to_xml()
        expexted = b"<Panda><name>Pesho</name></Panda>"

        self.assertEqual(tostring(result), expexted)

    def test_to_xml_returns_correct_xml_with_arguments(self):
        panda = Panda(
            name='Marto',
            age=20,
            weight=100.10,
            food=['bamboo', 'grass'],
            skills={'eat': 100, 'sleep': 200}
        )

        panda_result = panda.to_xml()
        pprint(tostring(panda_result))
        panda_expexted = "<Panda><name>Marto</name><age>20</age><weight>100.10</age><food>bamboo"

        self.assertEqual(tostring(panda_result), panda_expexted)

    def test_xmlable_with_empty_class_from_xml(self):
        panda = Panda()
        panda_expexted = panda.to_xml()
        expexted = Panda.from_xml(tostring(panda_expexted))

        self.assertEqual(panda, expexted)

    def test_xmlable_with_class_from_xml(self):
        panda = Panda(name="Pesho")
        panda_expexted = panda.to_xml()
        # print(tostring(panda_expexted))
        expexted = Panda.from_xml(tostring(panda_expexted))
        self.assertEqual(panda, expexted)


if __name__ == '__main__':
    unittest.main()
