import sqlalchemy
import core.db


class Mensagem(core.db.Base):

    __tablename__ = 'tb_mensagem'

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True
    )

    content = sqlalchemy.Column(
        sqlalchemy.String
       nullable=False
    )


