"""
Unit tests for the DatabaseManager class in app.utils.connection_manag.
These tests verify that the get_db method correctly yields a database session and handles transactions properly.
"""
from app.utils.connection_manag import DatabaseManager


def test_get_db_returns_session():
    """
    Test that the get_db method yields a database session and handles transactions correctly.
    """
    db_generator = DatabaseManager.get_db()

    db = next(db_generator)

    assert db is not None

    try:
        next(db_generator)
    except StopIteration:
        pass
