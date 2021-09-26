from api.utils.database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from api.models.books import BookSchema

class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    created = db.Column(db.DateTime, server_default=db.func.now())
    books = db.relationship('Book', backref="Author", cascade="all, delete-orphan")
    
    def __init__(self, first_name, last_name, books=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.books = books
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Author
        load_instance = True
        sqla_session = db.session
    id = fields.Number(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    created = fields.String(dump_only=True)
    books = fields.Nested(BookSchema, many=True, only=['title','year','id'])

# from api.utils.database import db
# # from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
# from marshmallow import Schema, fields
# from api.models.books import BookSchema

# class Author(db.Model):
#     __tablename__ = 'authors'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     first_name = db.Column(db.String(20))
#     last_name = db.Column(db.String(20))
#     created = db.Column(db.DateTime, server_default=db.func.now())
#     books = db.relationship('Book', backref="Author", cascade="all, delete-orphan")
#     def __init__(self, first_name, last_name, books=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.books = books
#     def create(self):
#         db.session.add(self)
#         db.session.commit()
#         return self
        
# class AuthorSchema(Schema):
#     class Meta(Schema.Meta):
#         model = Author
#         sqla_session = db.session
#     # id = auto_field.Number(dump_only=True)
#     # first_name = auto_field.String(required=True)
#     # last_name = auto_field.String(required=True)
#     # created = auto_field.String(dump_only=True)
#     # books = auto_field.Nested(BookSchema, many=True, only=['title','year','id'])
#     id = fields.Number(dump_only=True)
#     first_name = fields.String(required=True)
#     last_name = fields.String(required=True)
#     created = fields.String(dump_only=True)
#     books = fields.Nested(BookSchema, many=True, only=['title','year','id'])