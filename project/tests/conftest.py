"""Configuration for the pytest test suite."""

def pytest_sessionfinish(session, exitstatus):
    """
    avoids issue of no tests causing gh action failure
    """
    if exitstatus == 5:
        session.exitstatus = 0
