
from ..config.mysqlconnection import connectToMySQL
from ..models import new_ninjas 

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        self.ninjas = []


    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * From dojos;"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query)

        dojos = []

        for row in results:
            dojos.append(Dojo(row))
        return dojos


    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name,created_at, update_at) VALUES (%(name)s,NOW(), NOW());"
        return connectToMySQL("dojo_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojo_and_ninjas_schema").query_db(query,data)
        print(results)

        dojo = Dojo(results[0])
        for row in results:
            row_data = {
                "id": row["ninjas.id"],
                "dojo" : dojo,
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["updated_at"]
            }
            dojo.ninjas.append(new_ninjas.Ninja(row_data))

        return dojo 




