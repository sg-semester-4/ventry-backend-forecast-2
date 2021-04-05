from collections import namedtuple
import pandas as pd


class CursorExtras:
    def __init__(self, cursor):
        super().__init__()
        self.cursor = cursor

    def dictfetchall(self):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in self.cursor.description]
        return [
            dict(zip(columns, row))
            for row in self.cursor.fetchall()
        ]

    def namedtuplefetchall(self):
        "Return all rows from a cursor as a namedtuple"
        desc = self.cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in self.cursor.fetchall()]

    def dffetchall(self):
        "Return all rows from a cursor as a dataframe"
        df = pd.DataFrame(self.cursor)
        df.columns = [col[0] for col in self.cursor.description]
        return df
