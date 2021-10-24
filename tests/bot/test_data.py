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


def get_test_posts_for_multiple_documents_in_one_post():
    result = []
    result.append(
        dict2obj({
            'message': {
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
                'caption': 'folder_name'
            },

            'update_id': 462499639
        }))
    result.append(
        dict2obj({
            'message': {
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
                'caption': 'folder_name'
            },

            'update_id': 462499640
        }))
    return result
