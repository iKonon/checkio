OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == "conjunction": return int(x and y)
    elif operation == "disjunction": return int(x or y)
    elif operation == "implication": return int((not x) or y)
    elif operation == "exclusive": return int(x != y)
    elif operation == "equivalence": return int(x == y)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 0, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(1, 1, "exclusive") == 0, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
