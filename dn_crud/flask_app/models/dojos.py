from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas import Ninja

class Dojo :
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.ID = data['ID']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # ALL NINJAS list to append created Objects to access 
        self.all_ninjas = []

    @classmethod
    def add_dojo(cLs, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        result = connectToMySQL(cLs.DB).query_db(query, data)
        return result


    @classmethod 
    def get_all_dojos(cLs):
        query = """
        SELECT * FROM dojos;
        """
        result = connectToMySQL(cLs.DB).query_db(query)

        all_dojos = []
        for dojo in result:
            all_dojos.append(cLs(dojo))
        return all_dojos


    @classmethod
    def get_one_dojo(cLs, data):
        query = """
        SELECT * FROM dojos
        JOIN ninjas ON ninjas.dojo_ID = dojos.ID
        WHERE dojos.ID = %(ID)s;
        """
        result = connectToMySQL(cLs.DB).query_db(query,data)

        one_dojo = cLs(result[0])
        print(result)

        if result:
            for row in result:
                ninja_data = {
                    'ID' : row['ninjas.ID'],
                    'first_name' : row['first_name'],
                    'last_name' : row['last_name'],
                    'age' : row['age'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at'],
                    'dojo_ID' : row['dojo_ID']
                }
                one_dojo.all_ninjas.append(Ninja(ninja_data))
            return one_dojo
