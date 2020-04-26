import unittest
from tasks import deep_find, deep_find_all, deep_update, deep_compare


class TestDeepFind(unittest.TestCase):

    def test_deep_find_single_level(self):
        graph = {'a': 1, 'b': 2}
        self.assertEqual(deep_find(graph, 'a'), 1)

    def test_deep_find_second_level(self):
        graph = {'a': 1, 'b': {'aa': 11, 'bb': 2}, 'c': 3}
        self.assertEqual(deep_find(graph, 'aa'), 11)

    def test_deep_find_third_level(self):
        graph = {'a': 1, 'b': {'aa': 11, 'bb': {'aaa', 111}}, 'c': 3, 'd': {'dd': {'ddd': 22}}}
        self.assertEqual(deep_find(graph, 'ddd'), 22)


# class TestDeepFindAll(unittest.TestCase):

#     def test_deep_find_all_second_level(self):
#         graph = {'a': 1, 'b': {'a': 11, 'bb': 2}, 'c': 3}
#         self.assertEqual(deep_find_all(graph, 'a'), [1, 11])

#     def test_deep_find_all_third_level(self):
#         graph = {'a': 1, 'b': {'a': 11, 'bb': {'a', 111}}, 'c': 3, 'd': {'dd': {'ddd': 22}}}
#         self.assertEqual(deep_find_all(graph, 'a'), [1, 11, 111])


class TestDeepUpdate(unittest.TestCase):

    def test_deep_updatw_single_level(self):
        graph = {'a': 1, 'b': 2}
        deep_update(graph, 'a', 5)
        self.assertEqual(deep_find(graph, 'a'), 5)

    def test_deep_updatw_second_level(self):
        graph = {'a': 1, 'b': {'aa': 55, 'bb': 2}, 'c': 3}
        deep_update(graph, 'aa', 55)
        self.assertEqual(deep_find(graph, 'aa'), 55)

    def test_deep_update_third_level(self):
        graph = {'a': 1, 'b': {'aa': 11, 'bb': {'aaa', 111}}, 'c': 3, 'd': {'dd': {'ddd': 55}}}
        deep_update(graph, 'ddd', 55)
        self.assertEqual(deep_find(graph, 'ddd'), 55)


class TestDeepCompare(unittest.TestCase):

    def test_deep_compare_single_level(self):
        graph = {'a': 1, 'b': 2}
        graph2 = {'a': 1, 'b': 2}
        self.assertTrue(deep_compare(graph, graph2))

    def test_deep_compare_second_level(self):
        graph = {'a': 1, 'b': {'aa': 11, 'bb': 2}, 'c': 3}
        graph2 = {'a': 1, 'b': {'aa': 11, 'bb': 2}, 'c': 3}
        self.assertTrue(deep_compare(graph, graph2))

    def test_deep_copmare_third_level(self):
        graph = {'a': 1, 'b': {'aa': 11, 'bb': {'aaa', 111}}, 'c': 3, 'd': {'dd': {'ddd': 22}}}
        graph2 = {'a': 1, 'b': {'aa': 11, 'bb': {'aaa', 111}}, 'c': 3, 'd': {'dd': {'ddd': 22}}}
        self.assertTrue(deep_compare(graph, graph2))

    def test_deep_compare_single_level_false(self):
        graph = {'a': 1, 'b': 2}
        graph2 = {'a': 3, 'b': 2}
        self.assertFalse(deep_compare(graph, graph2))

    def test_deep_compare_second_level_false(self):
        graph = {'a': 1, 'b': {'aa': 11, 'bb': 2}, 'c': 3}
        graph2 = {'a': 1, 'b': {'aa': 1, 'bb': 2}, 'c': 3}
        self.assertFalse(deep_compare(graph, graph2))

    def test_deep_copmare_third_level_false(self):
        graph = {'a': 1, 'b': {'aa': 11, 'bb': {'aaa', 111}}, 'c': 3, 'd': {'dd': {'ddd': 22}}}
        graph2 = {'a': 1, 'b': {'aa': 11, 'bb': {'aaa', 11}}, 'c': 3, 'd': {'dd': {'ddd': 22}}}
        self.assertFalse(deep_compare(graph, graph2))


if __name__ == '__main__':
    unittest.main()
