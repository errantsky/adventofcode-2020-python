import unittest
from twentieth import extract_four_vectors

class MyTestCase(unittest.TestCase):
    def test_to_vec(self):

        with open('input/in20-test.txt') as f:
            lines = f.readlines()[1:11]
            lines = [list(line.rstrip()) for line in lines]

        print("")

        res = extract_four_vectors(lines)

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
