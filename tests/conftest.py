import pytest

BASE_URL = 'http://localhost:5000'

@pytest.fixture
def supply_url():
    return BASE_URL

@pytest.fixture
def testuser_4():
    return {
        'firstname': 'test',
        'lastname': 'user4',
        'username': 'testuser4',
        'password': 'Pass4',
        'email': 'testuser4@gmail.com'
    }
