class MyDict(dict):
    keys_arr = set()

    def __init__(self):
        super().__init__()

    def add_item(self, item, vals):

        if type(item) == str:
            self.update({item.lower(): vals})
            self.keys_arr.add(item)
            return
        raise Exception('can only be string')

    def get_item(self, key):
        keys_arr = [x for x in self.keys_arr if x.lower() == key.lower()]
        if len(keys_arr) != 0:
            return self.get(key.lower())
        raise KeyError('Key not present')


d = MyDict()
d.add_item('avi',123)
d.add_item('AVI',890)
d.add_item('AvI',345)
print(d.get_item('AVi1'))