import random
import time
import datetime
from uuid import uuid4
from bson import ObjectId


def create_int(length:int=2) -> int:
    start = 10 ** (length - 1)
    end = 10 ** length - 1
    return random.randint(start, end)


def create_float(front_length:int=2, back_length:int=2) -> float:
    start = 10 ** (front_length - 1)
    start2 = 10 ** (back_length - 1)
    end = 10 ** front_length - 1
    end2 = 10 ** back_length - 1

    front = random.randint(start, end)
    back = random.randint(start2, end2)
    f = '{0}.{1}'.format(front, back)
    return float(f)


def create_str(length:int=5) -> str:
    s = ''
    for i in range(length):
        num = random.randint(97, 122)
        s += chr(num)
    return s


def create_timestamp(is_int:bool=False):
    x = time.time()
    return int(x) if is_int else x


def create_datetime() -> datetime:
    return datetime.datetime.now()


def create_list(item_type='int', length=5) -> list:
    """

    :param item_type: int, str, float, dict, list, tuple, complex
    :param length:
    :return:
    """
    l = []
    if item_type == 'int':
        return [create_int(1) for _ in range(length)]
    elif item_type == 'str':
        return [create_str(4) for _ in range(length)]
    elif item_type == 'float':
        return [create_float(2, 2) for _ in range(length)]
    elif item_type == 'dict':
        return [
            {
                'a': 1,
                'b': 2,
                'c': 3
            }
            for _ in range(length)
        ]
    elif item_type == 'list':
        return [
            [1, 2, 3, 4, 5, 6]
            for _ in range(length)
        ]
    elif item_type == 'tuple':
        return [
            (1, 2, 3, 4, 5, 6)
            for _ in range(length)
        ]
    else:
        return [
            create_int(1),
            create_str(4),
            create_float(2, 2),
            {
                'a': 1,
                'b': 2,
                'c': 3
            },
            [1, 2, 3, 4, 5, 6],
            (1, 2, 3, 4, 5, 6)
        ]


def create_dict(simple:bool=True) -> dict:
    if simple:
        return {
            'a': 1,
            'b': 2,
            'c': 3
        }
    return {
        'a': create_int(1),
        'b': create_str(4),
        'c': create_float(2, 2),
        'd': {
            'a': 1,
            'b': 2,
            'c': {
                'a': 1,
                'b': 2,
                'c': 3
            }
        },
        'e': [1, 2, 3, 4, 5, 6],
        'f': (1, 2, 3, 4, 5, 6),
        'g': [
            {
                'name': 'xxx',
                'age': '20'
            },
            {
                'name': 'yyy',
                'age': '21'
            }
        ]
    }


def create_uuid():
    return uuid4()


def create_object_id():
    return ObjectId()


if __name__ == '__main__':
    print(create_int(3))
    print(create_float(3, 3))
    print(create_str(10))
    print(create_timestamp(is_int=True))
    print(create_list(length=5))
    print(create_dict(simple=False))
    print(create_uuid())
    print(create_object_id())