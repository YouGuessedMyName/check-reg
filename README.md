# check-reg

## What is check-reg

Check-reg is a simple command-line application written in python. Its main features are:

- Checking if a word is in a language described by a regular expression
- Finding some word in a language described by a regular expression
- Comparison of regular expressions

## Aproach

Check-reg uses a brute-force approach, which means that the run-time is exponential:
O(n^k), where n is the length of the input alphabet and k is the maximum length of the generated word.
These parameters can be edited at the top of the python file.

## Syntax

Check-reg uses + instead of | for disjunctions.
It also supports * (Arbitrary number of repetitions) and nested expressions with parenthesis.

## Usage

### Checking if a word is in a language described by a regular expression

```cmd
python check-reg.py -m regex word```

### Finding some word in a language described by a regular expression

```cmd
python check-reg.py -f regex```

### Comparison of regular expressions

```cmd
python check-reg.py -f regex1 regex2```
