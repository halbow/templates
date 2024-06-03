from {{ cookiecutter.project_name }} import Stuff


def test_add_one():
    assert Stuff().abc() == 3
