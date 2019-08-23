from unittest import TestCase, main
from symmetrical_number import symmetrical
from isogram import isogram_test


class PracticeTestCases(TestCase):

    def test_is_symmetric(self):

        self.assertEqual(symmetrical(34),False)

        self.assertEqual(symmetrical(444), True)

    def test_is_isogram(self):

        self.assertEqual(isogram_test("Avijatya"),False)

        self.assertEqual(isogram_test("Oracle"), True)

        self.assertEqual(isogram_test("PasSword"), False)


if __name__ ==  "__main__":
    main()