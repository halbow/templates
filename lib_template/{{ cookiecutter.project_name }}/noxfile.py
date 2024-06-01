import nox


@nox.session
def tests(session):
    session.install(".[dev]")
    session.run("ruff", "format", "--diff")
    session.run("mypy", "src")
    session.run("pytest")
