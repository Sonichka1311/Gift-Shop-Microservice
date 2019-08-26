import unittest
import flask_testing
import json

from flask_testing import TestCase
from app import create_app
from app.data import *
from app.helpers import *
from app.classes import Citizen


class MyTest(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test2.db'
    TESTING = True

    def create_app(self):
        return create_app(self)

    def setUp(self):
        database.create_all()

    def tearDown(self):
        database.session.remove()
        database.drop_all()

    def test_import(self):
        response = self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        self.assertEqual(RESPONSE, response.json)
        self.assertStatus(response, 201)

    def test_patch(self):
        self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        response = self.client.patch("/imports/1/citizens/3", data=json.dumps(CITIZEN), headers=HEADERS)
        self.assertEqual(NEW_CITIZEN_INFO, response.json['data'])
        self.assertEqual(RELATIVE_CITIZEN, get_array(Citizen.query.get((1, 1)).relatives))
        self.assert200(response)

    def test_get(self):
        self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        response = self.client.get("/imports/2/citizens")
        self.assertEqual(DATA['citizens'], response.json['data'])
        self.assert200(response)

    def test_get_presents(self):
        self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        self.client.patch("/imports/1/citizens/3", data=json.dumps(CITIZEN), headers=HEADERS)
        response = self.client.get("/imports/1/citizens/birthdays")
        self.assertEqual(PRESENTS, response.json['data'])
        self.assert200(response)

    def test_get_percentile(self):
        self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        self.client.patch("/imports/1/citizens/3", data=json.dumps(CITIZEN), headers=HEADERS)
        response = self.client.get("/imports/1/towns/stat/percentile/age")
        self.assertEqual(PERCENTILES, response.json)

    def test_import_error(self):
        response = self.client.post("/imports", data=ERROR_DATA_1, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_2, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_3, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_4, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_5, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_6, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_7, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_8, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_9, headers=HEADERS)
        self.assert400(response)

        response = self.client.post("/imports", data=ERROR_DATA_10, headers=HEADERS)
        self.assert400(response)

    def test_patch_error(self):
        self.client.post("/imports", data=json.dumps(DATA), headers=HEADERS)
        response = self.client.patch("/imports/1/citizens/3", data=json.dumps(ERROR_CITIZEN_1), headers=HEADERS)
        self.assert400(response)

        response = self.client.patch("/imports/1/citizens/3", data=json.dumps(ERROR_CITIZEN_2), headers=HEADERS)
        self.assert400(response)

        response = self.client.patch("/imports/1/citizens/3", data=json.dumps(ERROR_CITIZEN_3), headers=HEADERS)
        self.assert400(response)


if __name__ == '__main__':
    unittest.main()
