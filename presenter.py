from datetime import datetime

def create_note():
    note = {"text":input("Текст замітки:"),
            "date":datetime.now()}
    return note



def read_notes(notes):
    for number,note in enumerate(notes,1):
        print(f""" {note['text']} Було додано {note['date']} """)
        print("-"*35)
