import pymysql
from luigi import *


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

        except:
            result = 1


        if (result == 1):
            return 1
        else:
            return LocalTarget('result.txt')


if __name__ == '__main__':
    run()
