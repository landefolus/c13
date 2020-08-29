import unittest
from main import MyIter

class MyTest(unittest.TestCase):

    def test_iterator_09(self):
        for i in MyIter(1,10,1):
            pass
        self.assertEqual(i, 9)

    def test_iterator_90(self):
        for i in MyIter(10,0, 1):
            pass
        self.assertEqual(i, 1)

    def test_indexiter(self):
        gen = MyIter(0,20, 4)
        self.assertEqual(gen[0], 0, 'Ждал 0')
        self.assertEqual(gen[1], 4)
        self.assertEqual(gen[2], 8)
        with self.assertRaises(IndexError, msg="Отрицательный недопустим!"):
            print(gen[-5])

        with self.assertRaises(IndexError):
            a = gen[50]
            print(a)



if __name__ == '__main__':
    unittest.main()