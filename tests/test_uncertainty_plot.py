import pytest
from pydantic import ValidationError

from uncertainty_engine_types import UncertaintyPlot


def test_uncertainty_plot(uncertainty_plot_data: dict):
    """
    Basic test that UncertaintyPlot model is working as expected.

    Args:
        uncertainty_plot_data: Some data to define a UncertaintyPlot object
    """

    # Instantiate a UncertaintyPlot object
    uncertainty_plot = UncertaintyPlot(**uncertainty_plot_data)

    assert uncertainty_plot.model_dump() == uncertainty_plot_data


def test_uncertainty_plot_raise_missing(uncertainty_plot_data: dict):
    """
    Test that UncertaintyPlot object raises an error when missing a required field.

    Args:
        uncertainty_plot_data: Some data to define a UncertaintyPlot object
    """

    # Remove a required field
    del uncertainty_plot_data["mean"]

    # Try to instantiate a UncertaintyPlot object with a missing required field
    with pytest.raises(ValidationError):
        UncertaintyPlot(**uncertainty_plot_data)


def test_uncertainty_plot_raise_wrong_length(uncertainty_plot_data: dict):
    """
    Test that UncertaintyPlot object raises an error when missing a required field.

    Args:
        uncertainty_plot_data: Some data to define a UncertaintyPlot object
    """

    # Remove a required field
    _uncertainty_plot_data = uncertainty_plot_data.copy()
    _uncertainty_plot_data["x_vals"] = [1., 2.]  # Missing the final value

    # Try to instantiate a UncertaintyPlot object with a missing required field
    with pytest.raises(ValidationError):
        UncertaintyPlot(**_uncertainty_plot_data)
