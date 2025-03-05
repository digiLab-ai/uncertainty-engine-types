from uncertainty_engine_types import ID


def test_id():
    id = "fish_on_wheels"
    assert ID(id=id).model_dump() == {"id": id}
