from pydantic import BaseModel, model_validator


class UncertaintyPlot(BaseModel, extra="forbid"):
    x_label: str
    y_label: str
    x_vals: list[float]
    mean: list[float]
    std: list[float]
    lower: list[float]
    upper: list[float]

    @model_validator(mode="after")
    def validate_length(cls, model):
        n = len(model.x_vals)
        for _list in [model.mean, model.std, model.lower, model.upper]:
            if n != len(_list):
                raise ValueError("All lists must have the same length")
        return model
