import unittest
from bot.telegram_photo_bot import PhotoBot
from unittest.mock import Mock, MagicMock
from test_util import dict2obj


class TestPhotoBot(unittest.TestCase):

    def test_receive_update_single_file(self):
        # GIVEN

        root_dir = "/tmp/photo"
        file_name = 'IMG_20211003_133744.jpg'
        update = dict2obj({
            'message': {
                'delete_chat_photo': False,
                'document': {
                    'file_name': file_name,
                    'file_id': 'AJSHDFJASHGDFJASHGDFJASHGBFD',
                    'thumb': {
                        'height': 320,
                        'file_id': 'JASDFAKJSHDFKHASKDHFAKSJHFDKAHSD',
                        'file_size': 12327,
                        'width': 240,
                        'file_unique_id': 'AJSDGFJASHDGFJASHGDFJA'
                    },
                    'mime_type': 'image/jpeg',
                    'file_size': 10474747,
                    'file_unique_id': 'AEYGFAJWHGEFJASGD'
                }
            },
            'caption': 'Зарядье',
            'update_id': 462499639
        })
        context = {}
        photo_bot = PhotoBot()
        photo_bot.downloadFile = MagicMock()

        # WHEN
        photo_bot.receiveUpdate(update, context)

        # THEN
        photo_bot.downloadFile.assert_called_once_with(context, "AJSHDFJASHGDFJASHGDFJASHGBFD", "/tmp/photo/2021.10.03 Зарядье/IMG_20211003_133744.jpg")
