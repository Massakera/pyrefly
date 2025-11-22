"""Demo file to test Github Actions integration with inline PR annotations."""

def returns_wrong_type() -> int:
    """This function returns a string instead of int."""
    return "not an int"  # Error: bad-return


def type_mismatch_assignment() -> None:
    """This function has a type mismatch."""
    x: int = 10
    x = "string"  # Error: bad-assignment
    print(x)


def another_error(value: str) -> int:
    """Returns the input directly instead of converting."""
    return value  # Error: bad-return
