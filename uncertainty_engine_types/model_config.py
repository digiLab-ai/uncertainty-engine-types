from typing import Literal, Optional

from pydantic import BaseModel

ModelType = Literal[
    "BernoulliClassificationGPTorch",
    "SingleTaskGPTorch",
    "SingleTaskVariationalGPTorch",
]


class ModelConfig(BaseModel):
    input_variance: Optional[float] = None
    input_retained_dimensions: Optional[int] = None
    output_variance: Optional[float] = None
    output_retained_dimensions: Optional[int] = None
    model_type: ModelType = "SingleTaskGPTorch"
    kernel: Optional[str] = None
    warp_inputs: bool = False
    seed: Optional[int] = None
