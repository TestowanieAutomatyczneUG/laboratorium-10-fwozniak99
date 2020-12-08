class Note:
    def __init__(self, name, note):

        if type(name) != str or type(note) != float or name is None:
            raise TypeError("Wrong type!")

        if name == '':
            raise ValueError("Wrong name value! Cannot be empty")

        if note > 6 or note < 2:
            raise ValueError("Wrong note value! Must be between 2 and 6")

        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
