from note import Note


class Notebook:

    def __init__(self, notes):
        self._notes = notes or []

    @property
    def notes(self):
        return self._notes[:]

    def add_note(self, note):
        if type(note) == Note:
            self._notes.append(note)
            return True
        raise ValueError('Value passed is not of Note type')

    def clear_notebook(self):
        self._notes = []

    def search_notebook(self, text=''):
        return list(filter(lambda x: text in x.__str__(), self.notes))

    def clear_content(self, note_id):
        n = list(filter(lambda x: x.note_id == note_id, self.notes))

        return n[0].clear_content() if len(n) > 0 else 'No Note found'

    def add_content(self, note_id, content):
        n = list(filter(lambda x: x.note_id == note_id, self.notes))

        return n[0].add_content(content) if len(n) > 0 else 'No Note found'

    def add_tag(self, note_id, tag):
        n = list(filter(lambda x: x.note_id == note_id, self.notes))

        return n[0].add_tag(tag) if len(n) > 0 else 'No Note found'

    def clear_tag(self, note_id, tag=None):
        n = list(filter(lambda x: x.note_id == note_id, self.notes))

        if len(n) > 0:
            n = n[0]
        else:
            return 'No note found'
        if tag:
            return n.remove_tag(tag)
        return n.clear_tags()


if __name__ == "__main__":
    n1 = Note('First Note', ['first'])
    n2 = Note('second note', ['second'])
    n3 = Note('third note', ['third', 'test'])

    n4 = Note('fourth note', ['fourth', 'bro'])
    n5 = Note('fifth note', ['second', 'bro'])

    notebook = Notebook([n1, n2, n3, n4, n5])

    while True:
        print(
            f"\n1. Enter 1 to modify the content of note id\n2.Enter 2 to add a tag on a note id"
            f"\n3. Enter 3 to clear note content\n4. Enter 4 to clear the tags\n5. Enter 5 to search a note"
            f"\n6. Any other choice to quit\n")
        n = int(input("Choose an option to perform an operation").strip())
        if n!=5:
            id = int(input('Enter note id').strip())
        if n == 1:
            print('Enter content to modify note ')
            content = input().strip()
            notebook.add_content(id, content)
        elif n == 2:
            print('Enter a tag to attach with note')
            content = input().strip()
            notebook.add_tag(id, content)
        elif n == 3:
            print('Your note content will be cleared')
            notebook.clear_content(id)
        elif n == 4:
            print('Your note tags will be cleared')
            notebook.clear_tag(id)
        elif n == 5:
            tag = str(input("Enter a term to be searched").strip())
            print(notebook.search_notebook(tag))
        else:
            exit(1)
