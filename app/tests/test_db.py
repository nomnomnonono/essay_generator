from pathlib import Path

from app.db import EssayDB

DB_NAME = "test_essays.db"
TOPIC = "AI"
Path(DB_NAME).unlink(missing_ok=True)


def test_init() -> None:
    db = EssayDB(DB_NAME)
    assert db.db_name == DB_NAME


def test_add_essay() -> None:
    db = EssayDB(DB_NAME)

    response = db.add_essay(TOPIC, f"This is an essay on {TOPIC}")
    assert response is None

    response = db.add_essay(TOPIC, f"This is an essay on {TOPIC}")
    assert response is not None

    response = db.add_essay(TOPIC, 1.0)  # type: ignore
    assert response is not None


def test_get_esay() -> None:
    db = EssayDB(DB_NAME)

    response = db.get_essay(TOPIC)
    assert response == f"This is an essay on {TOPIC}"

    response = db.get_essay("Random")
    assert response is None
