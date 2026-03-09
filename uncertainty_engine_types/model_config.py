from typing import Literal, Optional

from pydantic import BaseModel

ModelType = Literal[
    "BernoulliClassificationGPTorch",
    "SingleTaskGPTorch",
    "SingleTaskVariationalGPTorch",
]
"""The type of model to use."""


class ModelConfig(BaseModel):
    """
    The configuration for training a model in the Uncertainty Engine.
    """

    custom_config: Literal[False] = False
    """
    Indicates this is not a custom config. Will always be `False` for
    `ModelConfig`.
    """

    input_variance: Optional[float] = None
    """Amount of variance to retain in input data."""

    input_retained_dimensions: Optional[int] = None
    """Number of dimensions to retain in input data."""

    output_variance: Optional[float] = None
    """"Amount of variance to retain in output data."""

    output_retained_dimensions: Optional[int] = None
    """Number of output dimensions to retain in output data."""

    model_type: ModelType = "SingleTaskGPTorch"
    """The type of model to use."""

    kernel: Optional[str] = None
    """The covariance kernel."""

    warp_inputs: bool = False
    """Whether to warp inputs."""

    seed: Optional[int] = None
    """Seed for reproducibility."""
