from flask_marshmallow import Marshmallow

ma = Marshmallow()

class BookSchema(ma.Schema):
    class Meta:
        fields = ("_id", "title", "author", "isbn", "available_copies")

class MemberSchema(ma.Schema):
    class Meta:
        fields = ("_id", "name", "email", "joined_date")
