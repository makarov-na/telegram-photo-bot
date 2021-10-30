import unittest
from unittest.mock import MagicMock, call

from bot.telegram_photo_bot import PhotoBot, CommentIsEmptyException
from tests.bot.test_data import get_test_post_with_document, get_test_posts_for_multiple_documents_in_one_post


class TestPhotoBot(unittest.TestCase):

    def setUp(self) -> None:
        self.root_dir = "/tmp/photo"
        self.photo_bot = PhotoBot(self.root_dir)
        self.photo_bot.downloadFile = MagicMock()
        self.context = MagicMock()
        self.update = get_test_post_with_document()

    def test_receive_update_multiple_documents_in_one_post_without_caption(self):
        # GIVEN
        first_update = get_test_posts_for_multiple_documents_in_one_post()[0]
        first_update.message.caption = None
        first_update.message.reply_text = MagicMock()
        second_update = get_test_posts_for_multiple_documents_in_one_post()[1]
        second_update.message.caption = None
        second_update.message.reply_text = MagicMock()

        # WHEN
        self.assertRaises(CommentIsEmptyException, self.photo_bot.receiveUpdate, first_update, self.context)
        self.assertRaises(CommentIsEmptyException, self.photo_bot.receiveUpdate, second_update, self.context)

        # THEN
        self.photo_bot.downloadFile.assert_not_called()
        first_update.message.reply_text.assert_called_once_with("Нужно указать комментарий")
        second_update.message.reply_text.assert_called_once_with("Нужно указать комментарий")

    def test_receive_update_multiple_documents_in_one_post_date_from_caption(self):
        # GIVEN
        first_update = get_test_posts_for_multiple_documents_in_one_post()[0]
        first_update.message.caption = "2021.10.04 Отпуск"
        second_update = get_test_posts_for_multiple_documents_in_one_post()[1]
        second_update.message.caption = None

        # WHEN
        self.photo_bot.receiveUpdate(first_update, self.context)
        self.photo_bot.receiveUpdate(second_update, self.context)

        self.photo_bot.downloadFile.assert_has_calls([call(self.context,
                                                           first_update.message.document.file_id,
                                                           self.root_dir + "/" + first_update.message.caption + "/" + first_update.message.document.file_name),
                                                      call(self.context,
                                                           second_update.message.document.file_id,
                                                           self.root_dir + "/" + first_update.message.caption + "/" + second_update.message.document.file_name)
                                                      ])

    def test_receive_update_multiple_documents_in_one_post_date_from_file(self):
        # GIVEN
        first_update = get_test_posts_for_multiple_documents_in_one_post()[0]
        second_update = get_test_posts_for_multiple_documents_in_one_post()[1]
        second_update.message.caption = None

        # WHEN
        self.photo_bot.receiveUpdate(first_update, self.context)
        self.photo_bot.receiveUpdate(second_update, self.context)

        self.photo_bot.downloadFile.assert_has_calls([call(self.context,
                                                           first_update.message.document.file_id,
                                                           self.root_dir + "/2021.10.03 " + first_update.message.caption + "/" + first_update.message.document.file_name),
                                                      call(self.context,
                                                           second_update.message.document.file_id,
                                                           self.root_dir + "/2021.10.03 " + first_update.message.caption + "/" + second_update.message.document.file_name)
                                                      ])

    def test_receive_update_single_document_without_caption(self):
        # GIVEN
        self.update.message.caption = None
        self.update.message.reply_text = MagicMock()

        # WHEN
        self.assertRaises(CommentIsEmptyException, self.photo_bot.receiveUpdate, self.update, self.context)

        # THEN
        self.photo_bot.downloadFile.assert_not_called()
        self.update.message.reply_text.assert_called_once_with("Нужно указать комментарий")

    def test_receive_update_single_document_date_from_caption(self):
        # GIVEN
        self.update.message.caption = '2021.01.01 Зарядье'

        # WHEN
        self.photo_bot.receiveUpdate(self.update, self.context)

        # THEN
        self.photo_bot.downloadFile.assert_called_once_with(self.context,
                                                            self.update.message.document.file_id,
                                                            self.root_dir + "/" + self.update.message.caption + "/" + self.update.message.document.file_name)

    def test_receive_update_single_document_date_from_file(self):
        # GIVEN
        self.update.message.caption = 'Зарядье'

        # WHEN
        self.photo_bot.receiveUpdate(self.update, self.context)

        # THEN
        self.photo_bot.downloadFile.assert_called_once_with(self.context,
                                                            self.update.message.document.file_id,
                                                            self.root_dir + "/2021.10.03 " + self.update.message.caption + "/" + self.update.message.document.file_name)
