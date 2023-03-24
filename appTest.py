import pytest

from app import login, signup, home, profile, manageprofile, jobs, jobsearch, interviews, results, account, logout


@pytest.fixture
def login_test():
    app = login()
    return app

@pytest.fixture
def signup_test():
    app = signup()
    return app

@pytest.fixture
def home_test():
    app = home()
    return app

@pytest.fixture
def profile_test():
    app = profile()
    return app

@pytest.fixture
def manageprofile_test():
    app = manageprofile()
    return app

@pytest.fixture
def jobs_test():
    app = jobs()
    return app

@pytest.fixture
def jobsearch_test():
    app = jobsearch()
    return app

@pytest.fixture
def interviews_test():
    app = interviews()
    return app

@pytest.fixture
def results_test():
    app = results()
    return app

@pytest.fixture
def account_test():
    app = account()
    return app

@pytest.fixture
def logout():
    app = logout()
    return app