import pytest
from project import Project, User, AccessError, LevelError


@pytest.fixture
def project():
    return Project()


def test_load_users(project):
    users = project.load_users()
    assert len(users) >= 3


def test_login(project):
    project.login('Петр', 2)
    assert project.cur_user['name'] == 'Петр'


def test_wrong_login(project):
    with pytest.raises(AccessError):
        project.login('Вася', 123)


def test_add_user(project):
    project.login('Петр', 2)

    users_count = len(project.users)
    project.add_user(User('Новый', 5, 3))

    assert len(project.users) == users_count + 1


def test_add_user_wrong_level(project):
    project.login('Петр', 2)

    with pytest.raises(LevelError):
        project.add_user(User('Новый', 5, 10))
