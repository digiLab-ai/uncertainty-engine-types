from __future__ import annotations

from io import StringIO

from pydantic import BaseModel


class TabularData(BaseModel):
    csv: str

    def load_dataframe(self):
        """
        Return a pandas DataFrame from the CSV string.
        """

        import pandas as pd

        return pd.read_csv(StringIO(self.csv))

    @classmethod
    def read_csv(cls, file_path: str) -> "TabularData":
        """
        Create a TabularData instance from a CSV file.

        Args:
            file_path: The path to the CSV file.

        """

        import pandas as pd

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Convert the DataFrame to a CSV string
        csv = df.to_csv(index=False)

        return cls(csv=csv)
