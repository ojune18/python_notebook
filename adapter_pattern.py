class LoadDictionary:

    def convert(self, keys, values):
        print({keys[x]: values[x] for x in range(len(keys))})


class ArrayAdapter:

    def convert(self, arr):
        d = LoadDictionary()
        keys = []
        vals = []
        for item in arr:
            keys.append(item[0])
            vals.append(item[1])
        d.convert(keys, vals)


class UseAdapter:
    ArrayAdapter().convert([[1, 2], [3, 4], [5, 6], [7, 8]])
