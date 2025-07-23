# logger.py
import logging
import pytest

# Configure a global logger
logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)

# Add console handler (optional, for live debug)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%H:%M:%S')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Pytest hook to inject logs into pytest-html report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        setattr(rep, "log", getattr(item, "log", ""))

# Fixture to capture logs and attach them to HTML report
@pytest.fixture(autouse=True)
def capture_test_logs(request, caplog):
    caplog.set_level(logging.INFO)
    yield
    request.node.log = "\n".join(caplog.messages)
