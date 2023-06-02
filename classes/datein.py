from datetime import date


class DateIn:
    def __init__(self, *args):
        super().__init__()
        print(*args)
        self.edate = args
        try:
            tmp = args[0]
            if not isinstance(tmp, date):
                tmp = tmp.split()[0].split('-')
                tmp = '.'.join([str(tmp[2]), str(tmp[1]), str(tmp[0])])
            else:
                tmp = f"{tmp.day:02}.{tmp.month:02}.{tmp.year:04}"
            self.rdate = tmp
        except:
            self.rdate = args[0]

    def __repr__(self):
        return self.rdate

    def __str__(self):
        return str(self.rdate)


if __name__ == '__main__':
    d = DateIn(2023, 12, 23)
    print(d.month + 10)
