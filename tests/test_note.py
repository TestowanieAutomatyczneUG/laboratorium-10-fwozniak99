import unittest

from sample.note import Note


class TestNote(unittest.TestCase):

    def test_get_note(self):
        note = Note('filip', 4.0)
        self.assertEqual(note.get_note(), 4)

    def test_get_name(self):
        note = Note('filip', 4.0)
        self.assertEqual(note.get_name(), 'filip')

    def test_note_lesser_than_2_exception(self):
        self.assertRaises(ValueError, Note, 'filip', 1.5)

    def test_note_greater_than_6_exception(self):
        self.assertRaises(ValueError, Note, 'filip', 6.5)

    def test_name_not_empty(self):
        self.assertRaises(ValueError, Note, '', 4.5)

    def test_name_not_str(self):
        self.assertRaises(TypeError, Note, 123, 3.5)

    def test_name_not_none(self):
        self.assertRaises(TypeError, Note, None, 2.5)

    def test_note_not_float(self):
        self.assertRaises(TypeError, Note, 'marcin', 4)
