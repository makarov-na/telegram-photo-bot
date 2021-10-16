import unittest
from bot.telegram_photo_bot import PhotoBot
from bot.date_utils import DateUtil
from unittest.mock import Mock, MagicMock


class TestDateUtils(unittest.TestCase):

    def test_isStartWithDate_id_valid(self):
        # GIVEN
        file_name = '2021.10.21 '
        # WHEN
        result = DateUtil.isStartWithDate(file_name)
        # THEN
        self.assertTrue(result)

    def test_isStartWithDate_is_invalid(self):
        # GIVEN
        file_name = 'sdf2021.10.21 '
        # WHEN
        result = DateUtil.isStartWithDate(file_name)
        # THEN
        self.assertFalse(result)

    def test_isContainDate_is_valid(self):
        # GIVEN
        file_name = 'IMG_20211003_133744.jpg'
        # WHEN
        result = DateUtil.isContainRawDate(file_name)
        # THEN
        self.assertTrue(result)

    def test_isContainDate_is_invalid(self):
        # GIVEN
        file_name = 'IMG_202103_133744.jpg'
        # WHEN
        result = DateUtil.isContainRawDate(file_name)
        # THEN
        self.assertFalse(result)

    def test_parseDate(self):
        # GIVEN
        file_name = 'IMG_20211003_133744.jpg'
        # WHEN
        result = DateUtil.makeDateString(file_name)
        # THEN
        self.assertEqual("2021.10.03", result)
