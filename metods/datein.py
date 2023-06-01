from datetime import date


class DateIn(date):
    def __init__(self, *args):
        super().__init__()
        self.edate = args
        self.rdate = '.'.join([str(args[2]), str(args[1]), str(args[0])])

    def __repr__(self):
        return self.rdate

    def __str__(self):
        return self.rdate


if __name__ == '__main__':
    d = DateIn(2023, 12, 23)
    print(d.month + 10)
