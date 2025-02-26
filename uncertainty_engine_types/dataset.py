from pydantic import BaseModel


class CSVDataset(BaseModel):
    csv: str
