from enum import Enum


class UserRole(str, Enum):
    """Defines user roles for access control."""

    ADMIN = "admin"
    MEMBER = "member"
