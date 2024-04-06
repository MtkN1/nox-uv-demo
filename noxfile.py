import nox


@nox.session(venv_backend="uv", python=["3.8", "3.9", "3.10", "3.11", "3.12"])
def tests(session: nox.Session):
    session.install("-r", "requirements/test.txt")
    session.run("pytest", "tests")
