HEADERS = {'Content-Type': 'application/json; charset=utf-8', 'Accept': 'text/plain'}

DATA = {
    "citizens": [
    {
         "citizen_id": 1,
         "town": "Москва",
         "street": "Льва Толстого",
         "building": "16к7стр5",
         "apartment": 7,
         "name": "Иванов Иван Иванович",
         "birth_date": "26.12.1986",
         "gender": "male",
         "relatives": [2]
    },
    {
        "citizen_id": 2,
        "town": "Москва",
        "street": "Льва Толстого",
        "building": "16к7стр5",
        "apartment": 7,
        "name": "Иванов Сергей Иванович",
        "birth_date": "01.04.1997",
        "gender": "male",
        "relatives": [1]
    },
    {
        "citizen_id": 3,
        "town": "Керчь",
        "street": "Иосифа Бродского",
        "building": "2",
        "apartment": 11,
        "name": "Романова Мария Леонидовна",
        "birth_date": "23.11.1986", "gender": "female",
        "relatives": []
    }
    ]
}

RESPONSE = {
    'data': {
        'import_id': 1
    }
}

CITIZEN = {
    "name": "Иванова Мария Леонидовна",
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "relatives": [1]
}

NEW_CITIZEN_INFO = {
    "citizen_id": 3,
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "name": "Иванова Мария Леонидовна",
    "birth_date": "23.11.1986",
    "gender": "female",
    "relatives": [1]
}

RELATIVE_CITIZEN = [2, 3]

PRESENTS = {
    "1": [],
    "2": [],
    "3": [],
    "4": [{
        "citizen_id": 1,
        "presents": 1
    }],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [{
        "citizen_id": 1,
        "presents": 1
    }],
    "12": [
        {
            "citizen_id": 2,
            "presents": 1
        },
        {
            "citizen_id": 3,
            "presents": 1
         }
    ]
}

PERCENTILES = {
    "data": [
        {
            "town": "Москва",
            "p50": 32.0,
            "p75": 32.0,
            "p99": 32.0
        }
    ]
}

ERROR_DATA_1 = '{\
\"citizens\": [\
    {\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"street\": \"Льва Толстого\",\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12.1986\",\
         \"gender\": \"male\",\
         \"relatives\": [2]\
    }\
}'

ERROR_DATA_2 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"street\": \"Льва Толстого\",\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12.1986\",\
         \"gender\": \"male\",\
         \"relatives\": [2]\
    }]\
'

ERROR_DATA_3 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"street\": \"Льва Толстого\",\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12.1986\",\
         \"gender\": \"male\",\
         \"relatives\": [2],\
         \"extra_field\": 123\
    }]\
}'

ERROR_DATA_4 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"street\": \"Льва Толстого\",\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12.1986\",\
         \"gender\": \"male\",\
         \"rels\": [2],\
    }]\
}'

ERROR_DATA_5 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 0,\
         \"town\": \"Москва\",\
         \"street\": \"Льва Толстого\",\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12.1986\",\
         \"gender\": \"male\",\
         \"relatives\": [2],\
    }]\
}'

ERROR_DATA_6 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12.1986\",\
         \"gender\": \"male\",\
         \"relatives\": [2],\
    }]\
}'

ERROR_DATA_7 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12\",\
         \"gender\": \"male\",\
         \"relatives\": [2],\
    }]\
}'

ERROR_DATA_8 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": 123,\
         \"building\": \"16к7стр5\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12\",\
         \"gender\": \"male\",\
         \"relatives\": [2],\
    }]\
}'

ERROR_DATA_9 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"building\": \"\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12\",\
         \"gender\": \"male\",\
         \"relatives\": [2],\
    }]\
}'

ERROR_DATA_10 = '{\
\"citizens\": \
    [{\
         \"citizen_id\": 1,\
         \"town\": \"Москва\",\
         \"building\": \"16к\",\
         \"apartment\": 7,\
         \"name\": \"Иванов Иван Иванович\",\
         \"birth_date\": \"26.12\",\
         \"gender\": \"m\",\
         \"relatives\": [2],\
    }]\
}'

ERROR_CITIZEN_1 = {
    "name": "",
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "relatives": [1]
}

ERROR_CITIZEN_2 = {
    "name": "Иванова Мария Леонидовна",
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": 7,
    "relatives": 123
}

ERROR_CITIZEN_3 = {
    "name": "Иванова Мария Леонидовна",
    "town": "Москва",
    "street": "Льва Толстого",
    "building": "16к7стр5",
    "apartment": "234",
    "relatives": [1]
}