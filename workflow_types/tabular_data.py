from io import StringIO

from pydantic import BaseModel


class TabularData(BaseModel):
    csv: str

    def load_dataframe(self):

        import pandas as pd

        return pd.read_csv(StringIO(self.csv))
