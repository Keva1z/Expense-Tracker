from datetime import datetime

class Expense:
    _total_id = 0

    def __init__(self, amount, description, **kwargs):
        self._total_id += 1
        self.id = self._total_id
        self.amount = amount
        self.description = description
        self.date = datetime.strptime(datetime.now().strftime("%d.%m.%Y"), "%d.%m.%Y")

        for key, value in kwargs.items():
            if key == 'date':
                self.date = datetime.strptime(value, "%d.%m.%Y")

    def __repr__(self):
        return f"Expense(id={self.id}, amount={self.amount}, description='{self.description}', date='{self.date}')"

    def to_dict(self) -> dict[str, str|int]:
        return {
            "id": self.id,
            "amount": self.amount,
            "description": self.description,
            "date": self.date.strftime("%d.%m.%Y")
        }
    
    @classmethod
    def from_dict(cls, data: dict[str, str|int]) -> 'Expense':
        return cls(amount=data.get('amount'),
                   description=data.get('description'),
                   date=data.get("date"))