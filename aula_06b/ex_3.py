import psycopg2
import psycopg2.extras


connection = psycopg2.connect(
    user='admin',
    password='4linux',
    host='localhost',
    port=5432,
    database='projeto'
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

email = input('Digite seu email: ')
senha = input('Digite sua senha: ')


def find_user_by_email(email):




    cursor.execute('''

        SELECT * FROM users

        WHERE email = \'{}\';

    '''.format(email))
    return cursor.fetchone()


user = find_user_by_email(email)

if user:
	if  senha == user['password']:
		print("Autenticado")
	else:
		print("Algo errado ocorreu")


