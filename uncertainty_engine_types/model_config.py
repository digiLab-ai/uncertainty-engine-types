from typing import Literal, Optional

from pydantic import BaseModel


class ModelConfig(BaseModel):
    input_variance: Optional[float] = None
    input_retained_dimensions: Optional[int] = None
    output_variance: Optional[float] = None
    output_retained_dimensions: Optional[int] = None
    model_type: Literal["SingleTaskGPTorch"] = "SingleTaskGPTorch"
    kernel: Optional[str] = None
    seed: Optional[int] = None
