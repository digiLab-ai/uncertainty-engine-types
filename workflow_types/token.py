from enum import Enum


class Token(str, Enum):
    TRAINING: str = "Training"  # Only used to mark nodes used for training models
    STANDARD: str = "Standard"  # The default token type
