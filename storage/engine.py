from storage.models import Expense
import json, pathlib

class JSONDatabase:

    _data_path: str = 'storage/'
    _objects: list[Expense] = []

    def __init__(self, base_file: str = 'data.json'):
        self.base_file = base_file
        self.load()

    def load(self):
        path = pathlib.Path(self._data_path).joinpath(self.base_file)
        if not path.is_file():
            with open(path, 'w+', encoding='utf-8') as f:
                f.write(json.dumps({}))
        with open(path, 'r+', encoding='utf-8') as f:
            data = f.read()
            if data != '':
                objects: dict[str, dict[str, str|int]] = json.loads(data)

                for object in objects.values():
                    self._objects.append(Expense.from_dict(object))

    def save(self):
        with open(self._data_path+self.base_file, 'w+', encoding='utf-8') as f:
            save_file = {}
            for id, expense in enumerate(self._objects):
                save_file[str(id)] = expense.to_dict()

            f.write(json.dumps(save_file))