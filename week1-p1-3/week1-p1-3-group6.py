class HashTable:
    def __init__(self):
        self.table = {}

    def hash(self, number):
        hash_number = str(pow(number+number/101+number/92 -
                              number/97+number/171+number/163, 0.5)).zfill(14)[1:13]
        return hash_number

    def _conflict(self, number, hashcode):
        return str(hashcode) in self.table and self.table[hashcode]['value'] != number

    def insert(self, number, data=None):
        number = float(number)
        hashcode = self.hash(number)
        while self._conflict(number, hashcode):
            hashcode = str(float(hashcode)+1)
        self.table[hashcode] = {'value': number, 'data': data}

    def get(self, number):
        number = float(number)
        hashcode = self.hash(number)
        while self._conflict(number, hashcode):
            hashcode = str(float(hashcode)+1)
        return self.table.get(hashcode, None)


hash_table = HashTable()
input_list = input('input numbers : ').split(' ')
input_list = [float(d) for d in input_list]
M = float(input('input M : '))
_get = False

for a in input_list:
    if not hash_table.get(M-a):
        hash_table.insert(a)
    else:
        _get = True
        print(f'Get！ {a}+{M-a}={M}')
        break

if not _get:
    print('Not Find')
