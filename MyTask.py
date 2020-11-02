from luigi import Task, run
from database import MyDatabase


class checkdatabase(Task):
    data = {'romanov867': '2uprcOxd',
            'romanov867_bot1': 'XUjkF8HO',
            'romanov867_dinch': '8oBvHZPC',
            'romanov867_st': '9j0Jog6Y',
            'romanov867_test': 'h9dR5eoF'}

    def requires(self):
        return [MyDatabase([key, value]) for key, value in self.data.items()]

    def run(self):
        pass

    def output(self):
        pass


if __name__ == '__main__':
    run()
