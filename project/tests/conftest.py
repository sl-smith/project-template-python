"""Configuration for the pytest test suite."""
import pytest


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    """Avoids issue of no tests causing gh action failure."""
    if exitstatus == 5:
        session.exitstatus = 0
