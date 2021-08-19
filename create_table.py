import sqlalchemy
from sqlalchemy.dialects.postgresql import UUID

DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_NAME = "localdb"
engine = sqlalchemy.create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}", echo=True)

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("email", sqlalchemy.String(40), unique=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String(100)),
    sqlalchemy.Column("hashed_password", sqlalchemy.String()),
    sqlalchemy.Column(
        "is_active",
        sqlalchemy.Boolean(),
        server_default=sqlalchemy.sql.expression.true(),
        nullable=False,
    ),
)

tokens_table = sqlalchemy.Table(
    "tokens",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column(
        "token",
        UUID(as_uuid=False),
        server_default=sqlalchemy.text("uuid_generate_v4()"),
        unique=True,
        nullable=False,
        index=True,
    ),
    sqlalchemy.Column("expires", sqlalchemy.DateTime()),
    sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id")),
)
metadata.create_all(engine)
