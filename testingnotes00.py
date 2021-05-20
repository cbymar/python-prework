

"""
https://quintagroup.com/cms/python/python-unit-testing
Mocks are about behavior; stubs are about state
PyUnit, doctests, nose are
"""
import pytest
import myscript  # .py


def test_add():
    assert myscript.add(7,3) == 10
    # ..... and so on and so forth

# must save this script as test_[whatever].py
# @pytest decorators
"""
$ pytest -v -k "add or string"
$ pytest -v -k "add and string"
$ pytest -v -m number    ## // uses the decorators, like pytest.mark.number
Use pytest setup_module(): to create db connections, for instance.
Ditto with teardown module.
Use pytest.fixture decorator to create a context for any test functions to use.  
@pytest.fixture(scope="module")  
def db():
    db = StudentDB()
    db.connect("data.json")
    yield db
    #### .... tests happen
    db.close()

"""


