from unittest.mock import MagicMock

from tests.bot.test_util import dict2obj
from datetime import timedelta, datetime


def get_test_post_with_document():
    post = dict2obj({
        'message': {
            'date': 1635963509,
            'delete_chat_photo': False,
            'document': {
                'file_name': 'IMG_20211003_133744.jpg',
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
            },
            'chat': {
                'last_name': 'Test',
                'type': 'private',
                'first_name': 'Test',
                'id': 634737640
            },
            'caption': 'folder_name'
        },

        'update_id': 462499639
    })
    post.message.reply_text = MagicMock()
    return post


def get_test_posts_for_multiple_documents_in_one_post():
    result = []
    result.append(
        dict2obj({
            'message': {
                'date': 1635963509,
                'delete_chat_photo': False,
                'media_group_id': '13075151643656746',
                'document': {
                    'file_name': 'IMG_20211003_133744.jpg',
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
                },
                'chat': {
                    'last_name': 'Test',
                    'type': 'private',
                    'first_name': 'Test',
                    'id': 634737640
                },
                'caption': 'folder_name'
            },

            'update_id': 462499639
        }))
    result.append(
        dict2obj({
            'message': {
                'date': 1635963509,
                'delete_chat_photo': False,
                'media_group_id': '13075151643656746',
                'document': {
                    'file_name': 'IMG_20211004_133745.jpg',
                    'file_id': 'sdmcbasjhdSHGDFJASHGBFD',
                    'thumb': {
                        'height': 320,
                        'file_id': 'sdmcbasjhdSHGDFJASHGBFD',
                        'file_size': 12327,
                        'width': 240,
                        'file_unique_id': 'fshfsjgdj'
                    },
                    'mime_type': 'image/jpeg',
                    'file_size': 10474747,
                    'file_unique_id': 'sjfdhjkdh'
                },
                'chat': {
                    'last_name': 'Test',
                    'type': 'private',
                    'first_name': 'Test',
                    'id': 634737640
                },
                'caption': 'folder_name'
            },

            'update_id': 462499640
        }))
    result[0].message.date = datetime.fromtimestamp(result[0].message.date)
    result[1].message.date = datetime.fromtimestamp(result[1].message.date)
    result[0].message.reply_text = MagicMock()
    result[1].message.reply_text = MagicMock()
    return result
