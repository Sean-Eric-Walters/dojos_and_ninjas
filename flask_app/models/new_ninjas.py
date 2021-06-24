from flask_app import app
from ..models import dojo

from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__( self , data):
        self.id = data['id']
        self.dojo = data["dojo"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        ninjas = []

        for row in results:
            row_data = {
                "id": row["id"],
                "dojo" : dojo.Dojo.get_dojo({"id": row["dojo_id"]}),
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["created_at"],
                "updated_at" : row["updated_at"]
            }

            ninjas.append(Ninja(row_data))
        return ninjas
        
    
    @classmethod
    def insert(cls, data):
            query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(fname)s,%(lname)s,%(age)s, NOW(), NOW(), %(dojo_id)s);"
            return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)