import re
import sys

# Regular expression checker
# Written by YouGuessedMyName 18-02-2023
# Link to GitHub repo:
GITHUB_LINK = ""
# More information in the readme.md file

# Contains adapted code from gen_words by Stack Overflow user Kevin 
# https://stackoverflow.com/questions/55694495/how-do-i-iterate-over-all-words-up-to-permutations-of-the-alphabet-in-python

# In the future it might be interesting to look at implementing the following algorithm:
# https://sulzmann.blogspot.com/2008/11/playing-with-regular-expressions.html

# Run-time: O(|ALPHABET|^(SEARCH_LENGTH))
SEARCH_LENGTH = 10 # The maximum word length that should be compared
ALPHABET = "ab" # Only use letters in the alphabet please

def main():
    # -h or -i
    if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "-i" or sys.argv[1] == "--info":
        print(f"More information and usage instructions can be found on github.\n{GITHUB_LINK}")
    # -v
    if sys.argv[1] == "-v":
        print("1.0")
    # -m regex word
    if sys.argv[1] == "-m" or sys.argv[1] == "--match":
        match(sys.argv[2], sys.argv[3])
    # -f regex
    if sys.argv[1] == "-f" or sys.argv[1] == "--find":
        find(int(sys.argv[2]), sys.argv[3])
        
    # -e regex1 regex2
    elif sys.argv[1] == "-e" or sys.argv[1] == "--match":
        equal(sys.argv[2], sys.argv[3])
    
def match(regex, word):
    if re.fullmatch(regex, word):
        print("Word is in the language")
    else:
        print("Word is not in the language")

def find(n: int, regex):
    if n == 0:
        return
    res = [] # Use a list because we want to print in order of word length.
    pr = to_python_regex(regex)
    for word in gen_words(ALPHABET, SEARCH_LENGTH-1):
        if re.fullmatch(pr, word):
            n -= 1
            if word == "":
                word = "lambda"
            res.append(word)
            if n <= 0:
                break
    if len(res) == 0:
        print(f"Empty language for w where |w| <= {SEARCH_LENGTH}")
    else:
        print(f"Words found: '{res}'")
    
def equal(regex1, regex2):
    pr1 = to_python_regex(regex1)
    pr2 = to_python_regex(regex2)
    for word in gen_words(ALPHABET, SEARCH_LENGTH-1):
        m1 = re.fullmatch(pr1, word)
        m2 = re.fullmatch(pr2, word)
        if bool(m1) != bool(m2):
            if word == "":
                word = "lambda"
            print(f"{regex1} != {regex2}\tCounterexample: '{word}'\n")
            if m1:
                print(f"'{word}' is in\t{regex1}\n'{word}' is not in {regex2}")
            else:
                print(f"'{word}' is not in\t{regex1}\n'{word}' is in {regex2}")
            return
    print(f"{regex1} = {regex2} for w where |w| <= {SEARCH_LENGTH}")

def gen_words(alphabet, size=None, recursive=True):
    """ADAPTED FROM gen_words by user Kevin on stackoverflow.
       https://stackoverflow.com/questions/55694495/how-do-i-iterate-over-all-words-up-to-permutations-of-the-alphabet-in-python

       Generates all words in alphabet of size size and smaller. 

    Args:
        alphabet (string)
        size (int, optional). Defaults to None.

    Yields:
        generator
    """
    if size is None:
        i = 0
        while True:
            yield from gen_words(alphabet, i)
            i += 1
    if size == 0:
        yield ""
    else:
        for s in gen_words(alphabet, size-1):
            if recursive:
                yield s
                recursive = False
            # For every word in all permutations of n-1, try adding all characters in alphabet to it.
            for c in alphabet:
                yield s + c

def to_python_regex(s):
    # 1 is removed by the input string, regex will interpret "1" as "", "1a" as "a", and "1+a+b" as "+a+b"
    return s.replace("+", "|").replace("1", "")

if __name__ == "__main__":
    main()