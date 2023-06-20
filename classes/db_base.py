from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    headers = {}
    def __repr__(self):
        out = []
        for attr, value in self.__dict__.items():
            if attr in self.headers:
                out.append(f'{attr} ({self.headers[attr]}): {str(value).strip()}')
        return f"<{'|'.join(out)}>"
