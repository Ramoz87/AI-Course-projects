from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
AKnightAndKnave = Symbol("A says 'I am both a knight and a knave.'")
knowledge0 = And(
    AKnightAndKnave,
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnightAndKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
AAndBKnaves = Symbol("A says 'We are both knaves.'")
knowledge1 = And(
    AAndBKnaves,
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    Implication(AKnight, Not(AAndBKnaves)),
    Implication(AKnave, Or(Not(BKnave), Not(AKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),
    Implication(Or(AKnight, AKnave), BKnight),
    Implication(Or(BKnight, BKnave), AKnave)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
AIsKnight = Symbol("A says 'I am a knight.'")
AIsKnave = Symbol("A says 'I am a knave.'")
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    Implication(AKnight, And(AIsKnight, Not(AIsKnave))),
    Implication(AKnave, And(AIsKnight, Not(AIsKnave))),

    Implication(BKnight, And(CKnave, AIsKnave)),
    Implication(BKnave, And(CKnight, Not(AIsKnave))),

    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
