import unittest
import pdf_parser
import datetime


class TestStringMethods(unittest.TestCase):

    test_str = '02 Nov - 07 Dec 12 4 6 23:55 05:25+2 AR7450* 772 13H30M'

    def test_convert_time(self):
        self.assertEqual(pdf_parser.convert_time(
            self.test_str), 48600)
        self.assertNotEqual(pdf_parser.convert_time(
            self.test_str), 56700)

    def test_date_parse(self):
        self.assertTupleEqual(pdf_parser.date_parse(
            self.test_str), (datetime.date(2018, 11, 2), datetime.date(2018, 12, 7)))

    def test_check_time(self):
        self.assertTupleEqual(pdf_parser.check_time(
            self.test_str), (datetime.time(23, 55), datetime.time(5, 25)))

    def test_check_week(self):
        self.assertEqual(pdf_parser.check_week(
            self.test_str), '12 4 6')

    def test_get_flight_aircraft(self):
        self.assertTupleEqual(pdf_parser.get_flight_aircraft(
            self.test_str), ('AR7450*', '772'))

    # def test_check_airport(self):
    #     self.assertTupleEqual(pdf_parser.check_airport(
    #         self.test_str), ('TO', 'Basel/Mulhouse', 'France', 'BSL'))


if __name__ == '__main__':
    unittest.main()
