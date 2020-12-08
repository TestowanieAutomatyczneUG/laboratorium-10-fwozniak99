from src.sample.notes_storage import NotesStorage


class NotesService:
    def __init__(self):
        self.notes_storage = NotesStorage()

    def add(self, note):
        self.notes_storage.add(note)

    def averageOf(self, name):
        all_student_grades = self.notes_storage.getAllNotesOf(name)

        if not all_student_grades:
            raise Exception("Name not found")

        number_of_grades = 0
        sum_of_grades = 0

        for grade in all_student_grades:
            number_of_grades += 1
            sum_of_grades += grade.get_note()

        return sum_of_grades/number_of_grades

    def clear(self):
        self.notes_storage.clear()