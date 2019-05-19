from datetime import datetime


class Note:
    cls_note_id = 0

    def __init__(self, text, tags):
        self._content = text
        self._created_at = datetime.now().isoformat()
        self._tags = tags or []
        self._last_modified = self._created_at
        Note.cls_note_id += 1
        self._note_id = Note.cls_note_id

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, text):
        self._content = text

    @property
    def tags(self):
        return self._tags[:]

    @property
    def note_id(self):
        return self._note_id;

    def add_tag(self, val):
        if val not in self.tags:
            self._tags.append(val)
            self._set_last_modified()
            return self.tags
        raise ValueError('Tag already present')

    def remove_tag(self, val):
        if val in self._tags:
            self._tags.remove(val)
            self._set_last_modified()
            return val
        raise ValueError('Tag not found')

    def clear_tags(self):
        self._tags.clear()
        self._set_last_modified()

    def reset(self):
        self._content = ''
        self._tags = []
        self._set_last_modified()

    def clear_content(self):
        self._content = ''
        self._set_last_modified()
        return True

    def _set_last_modified(self):
        self._last_modified = datetime.now().isoformat()

    def add_content(self, val):
        self._content += val

    def remove_content(self,val):
        self._content.replace(val,"")
        return self.content

    def __repr__(self):
        return f"\n{self._note_id}\n{self._content}\n{self._created_at}\n{self._tags}\n"



