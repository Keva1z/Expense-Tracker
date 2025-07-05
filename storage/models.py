from datetime import datetime

class Base():
    _total_id = 0

    def __init__(self, *args, **kwargs):
        Base._total_id += 1

        self.id = self._total_id

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def to_dict(self) -> dict:
        data: dict = {}
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                data[key] = value
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Base':
        return cls(**data)

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id}, ' + \
               f"{', '.join(f'{k}={f'"{v}"' if isinstance(v, str) else v}' for k, v in self.__dict__.items() if k != 'id' and not k.startswith('_'))})"

class Expense(Base):

    def __init__(self, amount: int = 0, description: str = '', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.amount = amount
        self.description = description
        self.date = datetime.now().strftime("%d.%m.%Y")

    def __match(self, arg, length: int) -> str:
        arg = str(arg)
        if len(arg) > length: return arg[:length]
        return arg + ' '*(length-len(arg))

    def __repr__(self):
        return f'{self.__match(self.id, 3)} {self.__match(self.date, 11)} {self.__match(self.description, 11)}    ${self.amount}'
        