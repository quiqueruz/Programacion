"""
Test de la relación de ejercicios de Github de Rafa
"""
import unittest
from unittest import TestCase
from duration import Duration


class TestDuration(TestCase):
    def setUp(self):
        self.duration1 = Duration(10, 20, 30)
        self.duration2 = Duration(20, 0, 0)
        self.duration3 = Duration(30, 59, 50)

    def test_add_seconds(self):
        self.duration1.add_seconds(20)
        self.assertEqual(self.duration1, Duration(10, 20, 50))

        self.duration2.add_seconds(60)
        self.assertEqual(self.duration2, Duration(20, 1, 0))

        self.duration3.add_seconds(10)
        self.assertEqual(self.duration3, Duration(31, 0, 0))

    def test_sub_seconds(self):
        self.duration1.sub_seconds(90)
        self.assertEqual(self.duration1, Duration(10, 19, 0))

        self.duration2.sub_seconds(3600)
        self.assertEqual(self.duration2, Duration(19, 0, 0))
        with self.assertRaises(ValueError):
            self.duration2.sub_hours(68401)

        self.duration3.sub_seconds(50)
        self.assertEqual(self.duration3, Duration(30, 59, 0))

    def test_add_minutes(self):
        self.duration1.add_minutes(100)
        self.assertEqual(self.duration1, Duration(12, 0, 30))

        self.duration2.add_minutes(3600)
        self.assertEqual(self.duration2, Duration(80, 0, 0))

        self.duration3.add_minutes(1)
        self.assertEqual(self.duration3, Duration(31, 0, 50))

    def test_sub_minutes(self):
        self.duration1.sub_minutes(620)
        self.assertEqual(self.duration1, Duration(0, 0, 30))
        with self.assertRaises(ValueError):
            self.duration1.sub_minutes(10)

        self.duration2.sub_minutes(1200)
        self.assertEqual(self.duration2, Duration(0, 0, 0))

        self.duration3.sub_minutes(60)
        self.assertEqual(self.duration3, Duration(29, 59, 50))

    def test_add_hours(self):
        self.duration1.add_hours(5)
        self.assertEqual(self.duration1, Duration(15, 20, 30))

        self.duration2.add_hours(30)
        self.assertEqual(self.duration2, Duration(50, 0, 0))

        self.duration3.add_hours(1)
        self.assertEqual(self.duration3, Duration(31, 59, 50))

    def test_sub_hours(self):
        self.duration1.sub_hours(10)
        self.assertEqual(self.duration1, Duration(0, 20, 30))
        with self.assertRaises(ValueError):
            self.duration1.sub_hours(10)

        self.duration2.sub_hours(19)
        self.assertEqual(self.duration2, Duration(1, 0, 0))
        with self.assertRaises(ValueError):
            self.duration2.sub_hours(2)

        self.duration3.sub_hours(1)
        self.assertEqual(self.duration3, Duration(29, 59, 50))
        with self.assertRaises(ValueError):
            self.duration3.sub_hours(30)

    def tearDown(self):
        del self.duration1  # Borrado de memoria
        del self.duration2
        del self.duration3


if __name__ == '__main__':
    unittest.main()
