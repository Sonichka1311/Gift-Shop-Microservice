from datetime import date
from app import database
from app.classes import Citizen, CheckSchema


def get_array(string):
    if len(string) > 2:
        return [int(i) for i in string[1:-1].split(', ')]
    else:
        return []


def is_date_valid(birth_date):
    day, month, year = map(int, birth_date.split('.'))
    try:
        date(year, month, day)
        if get_ages(birth_date) < 0:
            raise Exception(400)
    except:
        raise Exception(400)


def get_json_if_valid(request):
    try:
        json = request.get_json(force=False, silent=False, cache=False)
        schema = CheckSchema(partial=False, unknown='RAISE')
        for citizen in json['citizens']:
            schema.validate(citizen, partial=False)
            is_date_valid(citizen['birth_date'])
            if len(citizen.keys()) != 9:
                raise Exception(400)
    except:
        raise Exception(400)

    return json['citizens']


def get_patch_if_valid(request):
    try:
        info = request.get_json(force=False, silent=False, cache=False)
        for field in info:
            if field in ['town', 'street', 'building']:
                if isinstance(info[field], str):
                    if not 0 < len(info[field]) < 257:
                        raise Exception(400)
                else:
                    raise Exception(400)
            elif field in ['name', 'birth_date', 'gender']:
                if isinstance(info[field], str):
                    if len(info[field]) < 1:
                        raise Exception(400)
                else:
                    raise Exception(400)

                if field == 'gender':
                    if info[field] not in ['male', 'female']:
                        raise Exception(400)
                elif field == 'birth_date':
                    is_date_valid(info['birth_date'])
            elif field == 'apartment':
                if isinstance(info[field], int):
                    if info[field] < 0:
                        raise Exception(400)
                else:
                    raise Exception(400)
            elif field == 'relatives':
                if isinstance(info[field], list):
                    for item in info[field]:
                        if isinstance(item, int):
                            if item < 0:
                                raise Exception(400)
                        else:
                            raise Exception(400)
                else:
                    raise Exception(400)
    except:
        raise Exception(400)

    return info


def change_relatives(import_id, citizen_id, relatives_to_change, func):
    for relative_id in relatives_to_change:
        relative = Citizen.query.get((import_id, relative_id))
        database.session.delete(relative)
        relatives = get_array(relative.relatives)
        if func == "append":
            relatives.append(citizen_id)
        elif func == "remove":
            relatives.remove(citizen_id)
        relative.relatives = str(relatives)
        database.session.add(relative)


def get_ages(birth_date):
    day, month, year = map(int, birth_date.split('.'))
    birthday = date(year, month, day)
    today = date.today()
    age = today.year - birthday.year
    if today.month < birthday.month:
        age -= 1
    elif today.month == birthday.month and today.day <= birthday.day:
        age -= 1
    return age
