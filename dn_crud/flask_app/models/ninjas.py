from flask_app.config.mysqlconnection import connectToMySQL

class Ninja :
    DB = 'dojos_and_ninjas_schema'
    def __init__(self, data):
        self.ID = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_ID']

    
    @classmethod
    def add_ninja(cLs, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_ID)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_ID)s);
        """
        result = connectToMySQL(cLs.DB).query_db(query, data)
        return result