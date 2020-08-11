phonebook = []

def search(t=""):
    for pos, one_record in enumerate(phonebook):
        for val in one_record.values():
            if val.find(t)>=0:
                return pos
    return -1

