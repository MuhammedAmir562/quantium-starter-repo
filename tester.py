import pytest
from app import app

def test_header(dash_duo):

    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)


def test_visualization(dash_duo):

    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-graph", timeout=20)


def test_region_picker(dash_duo):

    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region", timeout=20)

