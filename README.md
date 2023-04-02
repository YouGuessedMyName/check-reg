# check-reg

## What is check-reg

Check-reg is a simple command-line application written in python. Unlike most similar applications, it uses academic syntax for regular expressions. (See syntax)
Its main features are:

- Checking if a word is in a language described by a regular expression
- Finding some word in a language described by a regular expression
- Equality of regular expressions up to a certain word length

## Aproach

Check-reg uses a brute-force approach, which means that the run-time is exponential:
O(n^k), where n is the length of the input alphabet and k is the maximum length of the generated word.
These parameters can be edited at the top of the python file.

## Syntax

Check-reg uses + instead of | for disjunctions.
It also supports * (Arbitrary number of repetitions) and nested expressions with parenthesis.
1 is a special character that denotes the empty word.

## Usage

There is a constant SEARCH_LENGTH which determines what the maximum word length should be that the program tests on.
The constant ALPHABET consists of all letters in the alphabet.
If you want to change these parameters, do so in the python file.

### Checking if a word is in a language described by a regular expression

```cmd
python check-reg.py -m regex word
```

### Finding n words in a language described by a regular expression where n is a natural number

```cmd
python check-reg.py -f n regex
```

### Equality of regular expressions up to a certain word length

```cmd
python check-reg.py -e regex1 regex2
```
