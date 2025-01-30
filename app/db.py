import sqlite3


class EssayDB:
    def __init__(self, db_name: str = "essays.db") -> None:
        self.db_name = db_name
        self._create_table()

    def _create_table(self) -> None:
        conn = sqlite3.connect(self.db_name)
        curs = conn.cursor()

        # Create table if not exists
        curs.execute('SELECT COUNT(*) FROM sqlite_master WHERE TYPE="table" AND NAME="essays"')
        if curs.fetchone()[0] == 0:
            curs.execute("CREATE TABLE essays (topic TEXT PRIMARY KEY, essay TEXT)")
            conn.commit()

        conn.close()

    def add_essay(
        self,
        topic: str,
        essay: str,
    ) -> None | AssertionError | sqlite3.IntegrityError | Exception:
        conn = sqlite3.connect(self.db_name)
        try:
            assert isinstance(topic, str)
            assert isinstance(essay, str)

            curs = conn.cursor()
            curs.execute("INSERT INTO essays VALUES (?, ?)", (topic, essay))
            conn.commit()
            return None
        except AssertionError as e:
            return e
        except sqlite3.IntegrityError as e:
            return e
        finally:
            conn.close()

    def get_essay(self, topic: str) -> str | None:
        assert isinstance(topic, str)

        conn = sqlite3.connect(self.db_name)
        curs = conn.cursor()
        curs.execute("SELECT essay FROM essays WHERE topic=?", (topic,))
        essay = curs.fetchone()
        conn.close()
        return essay[0] if essay else None
