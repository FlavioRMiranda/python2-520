import sqlalchemy
import ex_01

select_operation = sqlalchemy.select(
      [ ex_01.users_table ]

).where(ex_01.users_table.c.name == 'Flavio')


for result in select_operation.execute():
	print(result)
