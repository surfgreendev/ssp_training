from self_service_portal.users.models import User


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"
