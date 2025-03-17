from pydantic import BaseModel


class UncertaintyPlot(BaseModel):
    x_label: str
    y_label: str
    x_vals: list[float]
    mean: list[float]
    std: list[float]
    lower: list[float]
    upper: list[float]
