from src.sample.notes_service import NotesService
from src.sample.notes_storage import NotesStorage
from src.sample.note import Note

import unittest
from unittest.mock import *


class TestNotesService(unittest.TestCase):

    def setUp(self):
        self.temp = NotesService()

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_add_and_average(self, mock_method):
        mock_method.return_value = [Note("filip", 4.5)]
        self.temp.add(Note("filip", 4.5))
        self.assertEqual(self.temp.averageOf("filip"), 4.5)

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_average(self, mock_method):
        mock_method.return_value = [Note("filip", 4.5), Note("filip", 3.5)]
        self.temp.add(Note("filip", 4.5))
        self.temp.add(Note("filip", 3.5))
        self.temp.add(Note("dio", 3.5))
        self.assertEqual(self.temp.averageOf("filip"), 4.0)

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_add_average_missing_student_exception(self, mock_method):
        mock_method.return_value = []
        self.temp.add(Note("filip", 4.0))
        self.assertRaises(Exception, self.temp.averageOf, "marcin")

    @patch.object(NotesStorage, 'add')
    def test_add_exception(self, mock_method):
        mock_method.side_effect = TypeError()
        self.assertRaises(TypeError, self.temp.add, ["hello", 3])

    def test_clear(self):
        self.temp.add(Note("filip", 4.5))
        self.temp.add(Note("filip", 3.5))
        self.temp.clear()
        self.temp.notes_storage.notes = []
        self.assertEqual(self.temp.notes_storage.notes, [])

    def tearDown(self):
        self.temp = None

