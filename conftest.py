import pytest


@pytest.fixture()
# this will excuate at in the begning

def setup():

    print("lanching")
    yield
    print("quting")

    # /yeild will excuate at the end of the project
