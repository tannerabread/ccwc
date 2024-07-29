import argparse

def arg_parser():
    parser = argparse.ArgumentParser(
        prog='ccwc - custom wc',
        description='custom implementation of wc',
    )
    parser.add_argument('-c', '--bytes', dest='byte_count',
        help='Display the byte count for each input file.',
        action='store_true')
    parser.add_argument('-l', '--lines', dest='line_count',
        help='Display the line count for each input file.',
        action='store_true')
    parser.add_argument('-w', '--words', dest='word_count',
        help='Display the word count for each input file.',
        action='store_true')
    parser.add_argument('-m', '--chars', dest='char_count',
        help='Display the character count for each input file. If the current locale does not support multibyte characters this will match the -c option.',
        action='store_true')

    parser.add_argument('filenames', nargs='*', default=[])

    return parser