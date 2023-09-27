from datetime import datetime

def create_note():
    note = {"text":input("Текст замітки:"),
            "date":datetime.now()}
    return note



def read_notes(notes):
    pass
