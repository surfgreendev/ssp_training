import pytest

from self_service_portal.users.models import User

# from self_service_portal.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


"""
@pytest.fixture
def user(db) -> User:
    return UserFactory()
"""
