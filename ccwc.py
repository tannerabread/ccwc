#!/usr/bin/env python3

import sys
from arg_parser import arg_parser as ap
from count_file import count_file

parser = ap()

def __main__():
    args = parser.parse_args()
    if not sys.stdin.isatty():
        stdin = sys.stdin.readlines()
        print(f"{len(stdin)}")
    for file in args.filenames:
        count_file(file, args.byte_count, args.line_count, args.word_count, args.char_count)

__main__()
