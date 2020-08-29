import time

class Worker:
    def __init__(self, name='wrkr'):
        self.name = name
        self.__boss: Boss = None

    @property
    def boss(self):
        return  self.__boss

    @boss.setter
    def boss(self, val):
        if isinstance(val, Boss):
            if self.__boss:
                self.__boss.rm_worker(self)
            self.__boss = val
            self.__boss.add_worker(self)
        else:
            if val is None:
                self.__boss.rm_worker(self)
                self.__boss = None


class Boss:
    def __init__(self):
        self.__workers = {}

    def rm_worker(self, wrkr):
        if wrkr in self.__workers:
            self.__workers.pop(wrkr)
            wrkr.boss = None

    def add_worker(self, wrkr):
        if isinstance(wrkr) and wrkr not in self.__workers:
            self.__workers.update(wrkr)
            wrkr.boss = self

boss = Boss()
boss2 = Boss()
wrkr1 = Worker()

wrkr1.boss = boss
wrkr1.boss = boss2
wrkr2 = Worker("222")

boss.add_worker(wrkr2)

class store_as_json:
    def __enter__(self, fn="dataa"):
        self.__fdata = open(fn, 'w')
        return self

    def store(self, car_owner):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fdata.close()


nikolaj, petr = '', ''

with store_as_json("data_nikolaj.json") as saveme:
    saveme.store(nikolaj)


class timeme:
    def __enter__(self):
        self.start_time = time.time()
        self.__myfile = open("qwerty.txt", 'a')
        self.__appended =0
        return self

    def hello(self, line=''):
        self.__myfile.write(f"{line}\n")
        self.__appended +=1
        # print("privet")

    def tst(self):
        f = 0/0

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__myfile.close()
        # print(exc_type, exc_val, exc_tb)
        print(f"Записано {self.__appended} Прошло : ", time.time() -    self.start_time)


if __name__ == '__main__':

    with timeme() as fff:
        fff.hello()
        try:
            fff.tst()
        except:
            pass
        pass

    #
    #
    # with timeme():
    #     time.sleep(1)
    #     # privet.hello()
    #     # print(type(privet))
    #     #
    #     # privet.write("123123 123123")
    #
    #     fp1 = open("qwe.txt")
    #     for line in fp1:
    #         print(line)
    #     fp1.close()

        #
        # try:
        #     f = open('data/file.txt', 'w')
        #     f.write('hello')
        #     f.close()
        # except:
        #     print('Some error!')
        #
        #
        #
        # with open("qwe123.txt",) as fp1,  open("ewq.txt", "w") as fw:
        #     for line in fp1:
        #         fw.write(line+"\n")
