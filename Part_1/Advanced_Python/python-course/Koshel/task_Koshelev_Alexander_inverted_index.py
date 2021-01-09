#!/usr/bin/env python3
import sys
from collections import defaultdict
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType, ArgumentTypeError
from typing import List, Dict, Set
from storage_policy import StoragePolicy
from io import TextIOWrapper
import re

class EncodedFileType(FileType):
    def __call__(self, string):
        # the special argument "-" means sys.std{in,out}
        if string == '-':
            if 'r' in self._mode:
                stdin = TextIOWrapper(sys.stdin.buffer, encoding=self._encoding)
                return stdin
            elif 'w' in self._mode:
                stdout = TextIOWrapper(sys.stdout.buffer, encoding=self._encoding)
                return stdout
            else:
                msg = 'argument "-" with mode %r' % self._mode
                raise ValueError(msg)

        # all other arguments are used as file names
        try:
            return open(string, self._mode, self._bufsize, self._encoding,
                        self._errors)
        except OSError as e:
            message = "can't open '%s': %s"
            raise ArgumentTypeError(message % (string, e))


class InvertedIndex:
    """Inverted Index class to load extract and get document id's for list of words"""

    def __init__(self, inv_index: Dict[str, List[int]]):
        self.inv_index = inv_index

    def query(self, words: List[str]) -> Set[str]:
        """Return the list of relevant documents for the given query"""
        assert isinstance(words, list)
        try:
            docs_id = set(self.inv_index[words[0]])
        except KeyError:
            docs_id = set()
        for word in words:
            try:
                docs_id = docs_id & set(self.inv_index[word])
            except KeyError:
                docs_id = set()
        return docs_id

    def dump(self, filepath: str):
        """Extract inverted index dictionary to json"""
        StoragePolicy.dump(self.inv_index, filepath)

    @classmethod
    def load(cls, filepath: str):
        """Load inverted index class"""
        cls.inv_index = StoragePolicy.load(filepath)
        return cls


def load_documents(filepath: str) -> Dict[str, List[int]]:
    """Loads documents and transfrom to dictionary"""
    f = open(filepath, 'r', encoding='utf-8')
    text_list = []
    for _ in f:
        text_list.append(f.readline().strip())
    article_dict = {}
    for article in text_list:
        if article == '':
            continue
        article_splitted = article.split('\t')
        article_dict[int(article_splitted[0])] = ' '.join(article_splitted[1:])
    return article_dict


def build_inverted_index(article_dict: Dict[str, List[int]]) -> None:
    """Build inverted index from articles dict except stop words"""
    index_dict = defaultdict(list)
    for art_id, article in article_dict.items():
        for token in set(article.split(' ')):
            index_dict[token].append(art_id)
    return index_dict


DEFAULT_DATASET_PATH = 'wikipedia_sample/wikipedia_sample'
DEFAULT_INVERTED_INDEX_STORE_PATH = 'inv_index.dat'

def callback_build(arguments):
    documents = load_documents(arguments.dataset)
    inverted_index = build_inverted_index(documents)
    inv_index = InvertedIndex(inverted_index)
    inv_index.dump(arguments.output)
    return inverted_index

def callback_query(arguments):
    inv_index = InvertedIndex.load(arguments.index)
    if arguments.query is None:
        for query in arguments.query_file:
            words = query.strip().split(' ')
            doc_ind = InvertedIndex.query(inv_index, words)
            print(','.join(map(str, list(doc_ind))))
    else:
        a = str(arguments.query).split('--query')
        for b in a:
            words = re.findall(r'\w+', b)
            doc_ind = InvertedIndex.query(inv_index, words)
            print(','.join(map(str, list(doc_ind))))



def setup_parser(parser):
    subparsers = parser.add_subparsers(help='choose command')
    build_parser = subparsers.add_parser(
        'build', help='build inverted index and save in binary format into hard drive'
    )
    build_parser.add_argument("-d", "--dataset", required=False,
                              default=DEFAULT_DATASET_PATH,
                              help="load dataset path",
                              )

    build_parser.add_argument("-o", "--output", required=False,
                              default=DEFAULT_INVERTED_INDEX_STORE_PATH,
                              help="path to store inverted index",
                              )
    build_parser.set_defaults(callback=callback_build)
    query_parser = subparsers.add_parser(
        'query', help='query inverted index ',
    )
    query_parser.add_argument("-i", "--index",
                              default=DEFAULT_INVERTED_INDEX_STORE_PATH,
                              help="path to read inverted index",
                              )
    query_file_group = query_parser.add_mutually_exclusive_group(required=True)
    query_file_group.add_argument("--query-file-utf8",
                                type=EncodedFileType('r', encoding='utf-8'),
                                dest='query_file',
                                default=TextIOWrapper(sys.stdin.buffer, encoding='utf-8'),
                                help="run utf8 file query",
                                )

    query_file_group.add_argument("--query-file-cp1251",
                                type=EncodedFileType('r', encoding='cp1251'),
                                dest='query_file',
                                default=TextIOWrapper(sys.stdin.buffer, encoding='cp1251'),
                                help="run cp1251 file query",
                                )

    query_file_group.add_argument("--query",
                                  dest='query',
                                  nargs='+',
                                  help="run usual query",
                                  )
    query_parser.set_defaults(callback=callback_query)


def main() -> None:
    parser = ArgumentParser(prog="inverted-index",
                            description='to build, load, dump and query inverted index',
                            formatter_class=ArgumentDefaultsHelpFormatter)
    setup_parser(parser)
    arguments = parser.parse_args()
    arguments.callback(arguments)



if __name__ == "__main__":
    main()
