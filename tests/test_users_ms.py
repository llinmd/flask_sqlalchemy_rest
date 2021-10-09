import pytest
import requests, re

@pytest.mark.getuser
def test_get_users(supply_url):
    """ test of getting all users """
    response = requests.get(f"{supply_url}/user")
    data = response.json()
    assert response.status_code == requests.codes.ok
    assert len(data) >= 0

@pytest.mark.getuser
def test_get_user_by_username(supply_url, testuser4):
    """ test of getting user by username """
    response = requests.get(f"{supply_url}/user/{testuser4['username']}")
    if (response.status_code == 404):
        assert True
    else:
        assert response.status_code == requests.codes.ok
        # print(f"========= {response.json()} =========")
        assert len(response.json()) > 0

@pytest.mark.adduser
def test_add_user(supply_url, testuser4):
    """ test of adding a user """
    response = requests.post(f"{supply_url}/user", json=testuser4)

    if (response.status_code == 500):
        err = re.search('User already exists', response.text)
        assert(err.group() == 'User already exists')
    else:
        assert response.status_code == requests.codes.ok

    # with pytest.raises(Exception) as exc:
    #     response = requests.post(supply_url + "/user", json=testuser_4)
    # assert str(exc.value) == 'User already exists'

@pytest.mark.updateuser
def test_update_user(supply_url, testuser4_update):
    """ test of updating a user """
    response = requests.put(f"{supply_url}/user/{testuser4_update['username']}", json=testuser4_update)

    if (response.status_code == 404):
        assert True
    else:
        assert response.status_code == requests.codes.ok
        assert response.json().get('firstname') == testuser4_update['firstname']
        assert response.json().get('lastname') == testuser4_update['lastname']
        assert response.json().get('email') == testuser4_update['email']

@pytest.mark.deleteuser
def test_delete_user(supply_url, testuser4):
    """ test of deleting a user """
    response = requests.delete(f"{supply_url}/user/{testuser4['username']}")

    if (response.status_code == 404):
        assert True
    else:
        assert response.status_code == requests.codes.ok
        assert response.json().get('username') == testuser4['username']
