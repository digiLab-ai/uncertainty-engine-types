from typing import Literal, Optional

from pydantic import BaseModel


class ModelConfig(BaseModel):
    train_test_ratio: float = 1.0
    input_variance: Optional[float] = None
    output_variance: Optional[float] = None
    model_type: Literal["SingleTaskGPTorch"] = "SingleTaskGPTorch"
    seed: Optional[int] = None
