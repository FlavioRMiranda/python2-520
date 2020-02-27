
import ex_01


connection = ex_01.engine.connect()
insert_operation = ex_01.users_table.insert()

connection.execute(
    insert_operation,
    [
        {
            'name': 'Lucas',
            'age': 26,
            'password': 'admin' 
        }
    ]
)


