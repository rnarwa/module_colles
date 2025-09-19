from planche_handler import PlancheSemaine

class Rapport:
    def __init__(self):
        self.student = None
        self.commentary = None
        self.exercices = None
        self.exercices_note = []
        self.note = ''

    def get_exercises(self, exe_list):
        self.exercices = exe_list

    def set_note(self, exercise, note):
        idx = self.exercices.index(exercise)
        self.exercices_note.insert(idx, note)
