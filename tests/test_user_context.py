from uncertainty_engine_types import UserContext


def test_user_id_is_optional(user_context_data: dict[str, str]) -> None:
    del user_context_data["user_id"]
    user_context = UserContext(**user_context_data)
    assert user_context.user_id is None
