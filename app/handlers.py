import json
import numpy
from flask import Blueprint
from flask import request, jsonify
from app.classes import Import, Citizen, DumpSchema
from flask_restful import abort
from app.helpers import *
app_blueprint = Blueprint('api', __name__)

# неправильно работают исключения в проверке схемы
@app_blueprint.route('/imports', methods=['POST'])
def import_citizens():
    try:
        citizens = get_json_if_valid(request)
    except:
        abort(400)

    new_import = Import()
    database.session.add(new_import)
    database.session.commit()
    for citizen in citizens:
        citizen_item = Citizen(
            import_id=new_import.import_id,
            citizen_id=citizen['citizen_id']
        )
        citizen['relatives'] = str(citizen['relatives'])
        for field in citizen:
            setattr(citizen_item, field, citizen[field])

        database.session.add(citizen_item)
    database.session.commit()
    data = {
        'import_id': new_import.import_id
    }
    return jsonify({'data': data}), 201

# перепроверить после смены датабазы
@app_blueprint.route('/imports/<int:import_id>/citizens/<int:citizen_id>', methods=['PATCH'])
def patch_citizen_info(import_id, citizen_id):
    citizen = Citizen.query.get((import_id, citizen_id))
    database.session.delete(citizen)
    try:
        info = get_patch_if_valid(request)
    except:
        abort(400)
    if 'relatives' in info:
        info['relatives'] = str(info['relatives'])
        old_relatives = set(get_array(citizen.relatives))
        new_relatives = set(get_array(info['relatives']))
    for field in info:
        setattr(citizen, field, info[field])
    database.session.add(citizen)

    if 'relatives' in info:
        missed_relatives = old_relatives.difference(new_relatives)
        change_relatives(import_id, citizen_id, missed_relatives, "remove")

        acquired_relatives = new_relatives.difference(old_relatives)
        change_relatives(import_id, citizen_id, acquired_relatives, "append")

    database.session.commit()
    schema = DumpSchema()
    resp = schema.dump(citizen)
    resp['relatives'] = get_array(resp['relatives'])
    return jsonify({'data': resp}), 200


@app_blueprint.route('/imports/<int:import_id>/citizens', methods=['GET'])
def get_citizens_info(import_id):
    all_citizens = Import.query.get(import_id)
    schema = DumpSchema()
    if len(all_citizens.citizens) > 0:
        citizens = []
        for citizen in all_citizens.citizens:
            json_citizen = schema.dump(citizen)
            json_citizen['relatives'] = get_array(json_citizen['relatives'])
            citizens.append(json_citizen)
        return jsonify({'data': citizens}), 200
    else:
        return abort(400)


@app_blueprint.route('/imports/<int:import_id>/citizens/birthdays', methods=['GET'])
def get_presents_count(import_id):
    citizens = Import.query.get(import_id).citizens
    birthdays = {}
    for citizen in citizens:
        relatives = json.loads(citizen.relatives)
        b = {}
        for relative_id in relatives:
            birth_date = Citizen.query.get((import_id, relative_id)).birth_date
            day, month, year = map(int, birth_date.split('.'))
            if month in b:
                b[month] += 1
            else:
                b[month] = 1
        birthdays[citizen.citizen_id] = b
    data = dict((str(i), []) for i in range(1, 13))
    for citizen in birthdays.keys():
        presents = birthdays[citizen]
        for month in presents.keys():
            json_to_append = {
                'citizen_id': citizen,
                'presents': presents[month]
            }
            data[str(month)].append(json_to_append)
    return jsonify({'data': data}), 200


@app_blueprint.route('/imports/<int:import_id>/towns/stat/percentile/age', methods=['GET'])
def get_statistics(import_id):
    all_citizens = Import.query.get(import_id).citizens
    towns = {}
    for citizen in all_citizens:
        town = citizen.town
        if town not in towns:
            towns[town] = []
        towns[town].append(get_ages(citizen.birth_date))
    percentiles = []
    for town in towns.keys():
        date_array = numpy.array(towns[town])
        percentiles_json = {
            'town': town,
            'p50': round(numpy.percentile(date_array, 50), 2),
            'p75': round(numpy.percentile(date_array, 75), 2),
            'p99': round(numpy.percentile(date_array, 99), 2)
        }
        percentiles.append(percentiles_json)
    return jsonify({'data': percentiles}), 200
