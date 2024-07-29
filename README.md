# Coding Challenges
## [Build Your Own wc Tool](https://codingchallenges.fyi/challenges/challenge-wc)

Custom Implementation of `wc` on Unix command line with options for byte, line, word, and character count.

## Usage
```bash
ccwc [-h] [-c] [-l] [-w] [-m] [filenames ...]
```

## Options
- `-h`, `--help` : Display this help and exit
- `-c`, `--bytes` : Display the byte count for each input file
- `-l`, `--lines` : Display the line count for each input file
- `-w`, `--words` : Display the word count for each input file
- `-m`, `--chars` : Display the character count for each input file

The default for no flags sent is to display the lines, words, and bytes with the filename.
  