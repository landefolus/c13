import json


def store_data(dat):
    with open("dat.json", "w") as f:
        json.dump(dat)

def restore_data():
    try:
        with open("dat.json", "r") as f:
            return json.load(f)
    except:
        return []



if __name__ == "__main__":
    print("Меня вызвали")
    dat = restore_data()
    print(dat)