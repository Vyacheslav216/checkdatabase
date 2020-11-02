import luigi
import sys


class class1(luigi.Task):

    def requires(self):
        return class2()

    def output(self):
        return luigi.LocalTarget('class1.txt')

    def run(self):
        print('IN class A')


class class2(luigi.Task):
    a = [0]
    def requires(self):

        return []

    def run(self):
        _out = open('text.txt','w')
        _out.write("Hello World!\n")
        _out.close()
        print('in class B')
        self.a[0]=1
        print('in class B')



    def output(self):
        print('in class B')
        if(self.a[0]==1):
            print(1)
            return 1
        else:
            return luigi.LocalTarget('class2.txt')


if __name__ == '__main__':
    luigi.run()
# my.myerr1()

@class2.event_handler(luigi.Event.FAILURE)
def mourn_failure(task, exception):
    print(1)