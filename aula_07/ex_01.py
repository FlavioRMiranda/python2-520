import datetime

import sqlalchemy


engine = sqlalchemy.create_engine(
    'sqlite:///app.db',
    echo=True
)

metadata = sqlalchemy.MetaData(bind=engine)

users_table = sqlalchemy.Table(
    'tb_users',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),
    sqlalchemy.Column(
        'name',
        sqlalchemy.String(50),
        index=True
    ),
    sqlalchemy.Column(
        'age',
        sqlalchemy.Integer,
        nullable=False
    ),
    sqlalchemy.Column(
        'password',
        sqlalchemy.String        
    ),
    sqlalchemy.Column(
        'created_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now
    ),
    sqlalchemy.Column(
        'updated_at',
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now
    )

)

address_table = sqlalchemy.Table(
    'tb_name',
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        primary_key=True
    ),


)

metadata.create_all(engine)
