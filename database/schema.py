from sqlalchemy import text


def create_schema(engine):
    with engine.begin() as connection:
        connection.execute(
            text(
                "CREATE SCHEMA IF NOT EXISTS warehouse"
            )
        )

        connection.execute(
            text(
                "CREATE SCHEMA IF NOT EXISTS analytics"
            )
        )
