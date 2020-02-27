import sqlalchemy

engine = sqlalchemy.create_engine(
	'sqllite:///projeto.db',
	echo=True
)

Base = sqlalchemy.ext.declarative.declarative_base()


