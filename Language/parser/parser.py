import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

# +Holmes sat.
# +Holmes lit a pipe.
# +We arrived the day before Thursday.
# +Holmes sat in the red armchair and he chuckled.
# +My companion smiled an enigmatical smile. 
# +Holmes chuckled to himself.
# +She never said a word until we were at the door here.
# +Holmes sat down and lit his pipe.
# +I had a country walk on Thursday and came home in a dreadful mess.
# I had a little moist red paint in the palm of my hand.

NONTERMINALS = """
S -> NP VP

AdjP -> Adj | Det AdjP
NP -> N | Det N | N PP | AdjP NP | NP Adv
VP -> V | VP NP | NP VP | VP Conj VP | VP PP | VP Adv | Adv VP

PP -> P | P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    result = []
    for word in nltk.tokenize.word_tokenize(sentence):
        word = word.lower()
        if all(c.isalpha() for c in word):
            result.append(word)
    return result


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    result = []
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            if not any(child.label() == "NP" for child in subtree.subtrees(lambda t: t != subtree)):
                result.append(subtree)
    return result


if __name__ == "__main__":
    main()
