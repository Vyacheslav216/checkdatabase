from datetime import datetime

import pymysql
from luigi import *
import sys

class MyDatabase(Task):
    data = ListParameter()

    def requires(self):
        return []

    def output(self):
        result = 0
        try:
            connection = pymysql.connect(
                host='vh275.sweb.ru',
                user=self.data[0],
                password=self.data[1],
                db=self.data[0],
                charset='utf8mb4',
            )
            connection.close()
            f = open('result.txt', 'a')
            f.write(f'{datetime.now().strftime("%Y:%m:%d %H:%M")} database {self.data[0]} connection OK\n')
            f.close()
        except:
            result = 1
            f = open('result.txt', 'a')
            f.write(f'{datetime.now().strftime("%Y:%m:%d %H:%M")} database {self.data[0]} connection {sys.exc_info()}\n')
            f.close()


        if (result == 1):
            return 1
        else:
            return LocalTarget('result.txt')


if __name__ == '__main__':
    run()
