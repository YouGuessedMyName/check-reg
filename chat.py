import re
import sys

def generate_strings(regex):
    """Generate all possible strings for the regular expression"""
    stack = [(regex, '')]
    while stack:
        expr, string = stack.pop()
        if not expr:
            yield string
        elif expr.endswith('*'):
            stack.append((expr[:-1], string))
            stack.append((expr, string + expr[-2]))
        elif '|' in expr:
            left, right = expr.split('|')
            stack.append((left, string))
            stack.append((right, string))
        elif expr.startswith('(') and expr.endswith(')'):
            stack.append((expr[1:-1], string))
        else:
            stack.append((expr[1:], string + expr[0]))


def compare_languages(regex1, regex2):
    """Compare the languages described by the two regular expressions"""
    strings1 = set(generate_strings(regex1))
    strings2 = set(generate_strings(regex2))
    if strings1 == strings2:
        print(f"The languages {regex1} and {regex2} are the same.")
    else:
        print(f"The languages {regex1} and {regex2} are different.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_regex.py <regex1> <regex2>")
    else:
        regex1 = sys.argv[1]
        regex2 = sys.argv[2]
        compare_languages(regex1, regex2)