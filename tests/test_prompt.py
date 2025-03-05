from uncertainty_engine_types import Prompt


def test_prompt():
    prompt = "Hello"
    assert Prompt(prompt=prompt).model_dump() == {"prompt": prompt}
