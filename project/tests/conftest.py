"""Configuration for the pytest test suite."""
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _pytest.main import Session


def pytest_sessionfinish(session: Session, exitstatus: int) -> None:
    """avoids issue of no tests causing gh action failure"""
    if exitstatus == 5:
        session.exitstatus = 0
