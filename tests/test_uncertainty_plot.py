import pytest
from pydantic import ValidationError

from uncertainty_engine_types import UncertaintyPlot


def test_uncertainty_plot(uncertainty_plot_data: dict):
    """
    Basic test that ResourceID model is working as expected.

    Args:
        resource_id_data: Some data to define a ResourceID object
    """

    # Instantiate a ResourceID object
    uncertainty_plot = UncertaintyPlot(**uncertainty_plot_data)

    assert uncertainty_plot.model_dump() == uncertainty_plot_data


def test_uncertainty_plot_raise_missing(uncertainty_plot_data: dict):
    """
    Test that ResourceID object raises an error when missing a required field.

    Args:
        uncertainty_plot_data: Some data to define a ResourceID object
    """

    # Remove a required field
    del uncertainty_plot_data["mean"]

    # Try to instantiate a ResourceID object with a missing required field
    with pytest.raises(ValidationError):
        UncertaintyPlot(**uncertainty_plot_data)
