import pytest

from uncertainty_engine_types.user_role import UserRole


@pytest.mark.parametrize(
    "role, expected",
    [
        (UserRole.MEMBER, "member"),
        (UserRole.ADMIN, "admin"),
    ],
)
def test_member_value(
    role: UserRole,
    expected: str,
) -> None:
    """Test that the value of each UserRole member is correct."""

    assert role == expected


@pytest.mark.parametrize(
    "role",
    [
        UserRole.MEMBER,
        UserRole.ADMIN,
    ],
)
def test_is_str_instance(role: UserRole) -> None:
    """Test that each UserRole member is an instance of str."""

    assert isinstance(role, str)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("member", UserRole.MEMBER),
        ("admin", UserRole.ADMIN),
    ],
)
def test_from_value(value: str, expected: UserRole) -> None:
    """Test that a UserRole can be created from its value."""

    assert UserRole(value) is expected


@pytest.mark.parametrize(
    "bad_value",
    [
        "su",
        "owner",
        "",
        "ADMIN",
        "Member",
    ],
)
def test_invalid_value_raises(bad_value: str) -> None:
    """Test that creating a UserRole with an invalid value raises a ValueError."""

    with pytest.raises(ValueError):
        UserRole(bad_value)


def test_all_members() -> None:
    """Test that all UserRole members are correctly defined."""

    members = {role.value for role in UserRole}
    assert members == {"member", "admin"}
