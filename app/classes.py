from app import database
from marshmallow import Schema, fields
from marshmallow.validate import Range, Length, OneOf


class Import(database.Model):
    import_id = database.Column(database.Integer, primary_key=True)
    citizens = database.relationship('Citizen', backref='import', lazy=True)


class Citizen(database.Model):
    import_id = database.Column(database.Integer, database.ForeignKey('import.import_id'),
                                primary_key=True, nullable=False)
    citizen_id = database.Column(database.Integer, primary_key=True, nullable=False)
    town = database.Column(database.String)
    street = database.Column(database.String)
    building = database.Column(database.String)
    apartment = database.Column(database.Integer)
    name = database.Column(database.String)
    birth_date = database.Column(database.String)
    gender = database.Column(database.String)
    relatives = database.Column(database.String)


class CheckSchema(Schema):
    citizen_id = fields.Int(validate=Range(min=0))
    town = fields.Str(validate=Length(1, 256))
    street = fields.Str(validate=Length(1, 256))
    building = fields.Str(validate=Length(1, 256))
    apartment = fields.Int(validate=Range(min=0))
    name = fields.Str(validate=Length(min=1))
    birth_date = fields.Str(validate=Length(min=1))
    gender = fields.Str(validate=OneOf(choices=['male', 'female']))
    relatives = fields.List(fields.Int(), validate=Length(min=0))


class DumpSchema(Schema):
    citizen_id = fields.Int(validate=Range(min=0))
    town = fields.Str(validate=Length(1, 256))
    street = fields.Str(validate=Length(1, 256))
    building = fields.Str(validate=Length(1, 256))
    apartment = fields.Int(validate=Range(min=0))
    name = fields.Str(validate=Length(min=1))
    birth_date = fields.Str(validate=Length(min=1))
    gender = fields.Str(validate=OneOf(choices=['male', 'female']))
    relatives = fields.Str()
