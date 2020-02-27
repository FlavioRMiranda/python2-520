import sqlalchemy
import sqlalchemy.orm

import core.db
import models.user

core.db.Base.metadata.create_all(
	core.db.engine
)





