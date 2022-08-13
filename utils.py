
from werkzeug.exceptions import BadRequest
from os import path


def check_count_args(*args, **kwargs):
    if kwargs["cmd1"] and kwargs["val1"] == None:
        raise BadRequest("Введите значения")
    if kwargs["file_name"] == None:
        raise BadRequest("Обязательно нужно ввести название файла")
    if path.exists(kwargs["file_path"]) == False:
        raise BadRequest("Нет такого файла")

def foo(f, cmd, val):
    if cmd == "filter":
        return filter(lambda x: val in x, f)
    if cmd == 'map':
        val = int(val)
        return [x.split()[val] for x in f]
    if cmd == 'unique':
        return set(f)
    if cmd == "sort":
        return sorted(f, reverse=bool(val))
    if cmd == "limit":
        val = int(val)
        return list(f)[:val]


