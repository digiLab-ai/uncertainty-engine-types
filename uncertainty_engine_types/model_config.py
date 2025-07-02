from typing import Optional
from enum import Enum

from pydantic import BaseModel


class ModelType(str, Enum):
    classification = "BernoulliClassificationGPTorch"
    single_task = "SingleTaskGPTorch"
    variational = "SingleTaskVariationalGPTorch"


class ModelConfig(BaseModel):
    input_variance: Optional[float] = None
    input_retained_dimensions: Optional[int] = None
    output_variance: Optional[float] = None
    output_retained_dimensions: Optional[int] = None
    model_type: ModelType = ModelType.single_task
    kernel: Optional[str] = None
    warp_inputs: bool = False
    seed: Optional[int] = None
