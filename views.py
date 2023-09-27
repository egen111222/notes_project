# Ми користувач який має список нотатків із датами
# ми їх можемо
# додавати
# читати
# видаляти

# всі нотати зберігаються у файлі заданому в конфігурації
from models import FILENAME
import os
from file_presenter import (check_file,
                            read_from_file,
                            write_to_file)

check_file(FILENAME)

notes = read_from_file(FILENAME)

print(notes)
while True:
    choice = input("""1 створити замітку
2 чиати замітки
3 видалити замітки
4 вихід:""")
    if choice == "1":
        note = create_note()
        notes.append(note)
    if choice == "2":
        read_notes(notes)
    if choice == "3":
        notes.clear()
    if choice == "4":
        break





