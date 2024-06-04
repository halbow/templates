# type: ignore

import nox


@nox.session
def tests(session):
    session.install(".[dev]")
    session.run("ruff", "format", "--diff")
    session.run("ruff", "check")
    session.run("mypy", "src")
    session.run("pytest")
