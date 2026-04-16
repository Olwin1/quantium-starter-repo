import pytest
from pink_morsel_visualised import app  # make sure your main file is named app.py


@pytest.fixture
def dash_app():
    return app


# 1. Header is present
def test_header_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    header = dash_duo.wait_for_element("h1", timeout=10)
    assert header is not None
    assert "Pink Morsel Sales Dashboard" in header.text


# 2. Visualisation is present
def test_visualisation_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    graph = dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert graph is not None


# 3. Region picker is present
def test_region_picker_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)

    region_filter = dash_duo.wait_for_element("#region-filter", timeout=10)
    assert region_filter is not None