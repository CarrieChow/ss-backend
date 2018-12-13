from src import Base


def pytest_runtest_setup(item):
    Base.metadata.create_all()


def pytest_runtest_teardown(item, nextitem):
    Base.metadata.drop_all()
