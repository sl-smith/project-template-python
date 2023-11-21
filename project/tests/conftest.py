"""Configuration for the pytest test suite."""
from pytest import Session


def pytest_sessionfinish(session: Session, exitstatus: int) -> None:
    """Avoids issue of no tests causing gh action failure."""
    if exitstatus == 5:
        session.exitstatus = 0
