from enum import Enum


class Token(str, Enum):
    TRAINING = "Training"  # Only used to mark nodes used for training models
    STANDARD = "Standard"  # The default token type
