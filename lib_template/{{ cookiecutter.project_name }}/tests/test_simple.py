from {{ cookiecutter.project_name }} import abc
from {{ cookiecutter.project_name }}.simple import add_one



def test_add_one(self):
    assert add_one(5) == 6


