#! /usr/bin/env python

from panflute import *
import sys
import shlex
from collections import defaultdict
import subprocess
import os

def make_formatter(argline):
    command = shlex.split(argline)

    def _formatter(input):
        read, write = os.pipe()
        os.write(write, input.encode('utf-8'))
        os.close(write)

        output = subprocess.check_output(command, stdin=read).decode('utf-8')

        os.close(read)
        return output

    return _formatter


def null_formatter():
    def _formatter(input):
        return input, False
    return _formatter


def prepare(doc):
    doc.formatters = defaultdict(null_formatter)

    for lang, command in doc.get_metadata('formatters', default={}).items():
        doc.formatters[lang] = make_formatter(command)


def format_blocks(elem, doc):
    if not isinstance(elem, CodeBlock) or not elem.classes or 'no-format' in elem.classes:
        return

    formatter = doc.formatters[elem.classes[0]]
    try:
        elem.text = formatter(elem.text)
    except subprocess.CalledProcessError:
        elem.classes.append('format-error')

    return elem


def main(doc=None):
    return run_filter(format_blocks, prepare=prepare, doc=doc)


if __name__ == '__main__':
    main()
