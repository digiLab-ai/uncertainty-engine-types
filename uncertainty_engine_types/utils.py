from pydantic import ValidationError


def format_pydantic_errors(e: ValidationError) -> str:
    msgs = []
    for error in e.errors():
        loc = " -> ".join(map(str, error["loc"]))
        msgs.append(f"Error at '{loc}': {error['msg']}")
    return "\n".join(msgs)
