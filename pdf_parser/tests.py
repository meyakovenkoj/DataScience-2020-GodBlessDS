import unittest
import pdf_parser
import datetime


class TestStringMethods(unittest.TestCase):

    test_str = '01 Nov - 31 Jan 1234567 12:40 14:00 SV1666 320 1H20M'

    def test_convert_time(self):
        self.assertEqual(pdf_parser.convert_time(
            self.test_str), 4800)
        self.assertNotEqual(pdf_parser.convert_time(
            self.test_str), 56700)

    def test_date_parse(self):
        self.assertTupleEqual(pdf_parser.date_parse(
            self.test_str), (datetime.date(2018, 11, 1), datetime.date(2019, 1, 31)))

    def test_check_time(self):
        self.assertTupleEqual(pdf_parser.check_time(
            self.test_str), (datetime.time(12, 40), datetime.time(14, 0)))

    def test_check_week(self):
        self.assertEqual(pdf_parser.check_week(
            self.test_str), '1234567')

    def test_get_flight_aircraft(self):
        self.assertTupleEqual(pdf_parser.get_flight_aircraft(
            self.test_str), ('SV1666', '320'))


if __name__ == '__main__':
    unittest.main()
