from tests.bot.test_util import dict2obj


def get_test_post_with_document():
    return dict2obj({
            'message': {
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
                'caption': 'folder_name'
            },

            'update_id': 462499639
        })