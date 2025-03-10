from typing import Optional

from pydantic import BaseModel


class ModelConfig(BaseModel):
    train_test_ratio: float
    input_variance: float
    output_variance: float
    model_type: str
    seed: Optional[int] = None
