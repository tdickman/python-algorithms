import hashtable.errors

TABLE_SIZE = 256


class HashTable(object):
    def __init__(self):
        self.table = []
        for x in range(TABLE_SIZE):
            self.table.append(None)

    def __setitem__(self, key, value):
        '''Accepts strings as key input, and values can be any format'''
        index = hash(key) % TABLE_SIZE
        if not self.table[index]:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))

    def __getitem__(self, key):
        index = hash(key) % TABLE_SIZE
        if self.table[index]:
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]
        raise hashtable.errors.InvalidKey

    def __delitem__(self, key):
        index = hash(key) % TABLE_SIZE
        if self.table[index]:
            for i, pair in enumerate(self.table[index]):
                if pair[0] == key:
                    del self.table[index][i]
                    return
        raise hashtable.errors.InvalidKey
