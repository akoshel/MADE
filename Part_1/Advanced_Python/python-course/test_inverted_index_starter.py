from inverted_index import load_documents, build_inverted_index, InvertedIndex, callback_build, callback_query, EncodedFileType
import pytest
from argparse import ArgumentTypeError
import logging



class Build_arguments():

    def __init__(self):
        self.dataset = 'small_wiki_sample'
        self.output = 'inverted.index'


class Query_arguments():

    def __init__(self):
        self.index = 'inverted.index'
        self.query_file = None
        self.query = None


def test_EncodedFileType_call():
    with pytest.raises(ValueError) as ve:
        efp = EncodedFileType('o', encoding='utf-8')
        EncodedFileType.__call__(efp, '-')
    with pytest.raises(ArgumentTypeError) as ae:
        efp = EncodedFileType('r', encoding='utf-8')
        EncodedFileType.__call__(efp, 'not -')

def test_callback_build():
    arguments = Build_arguments()
    callback_build(arguments)
    assert True

def test_callback_query(capsys, caplog):
    caplog.set_level("DEBUG")
    arguments = Query_arguments()
    with open('queries', mode='r', encoding='ascii') as file:  # b is important -> binary
        file_content = file.readlines()
    arguments.query_file = file_content
    callback_query(arguments)
    file.close()
    captured = capsys.readouterr()
    assert '' == captured.err
    assert any('Load' in message for message in caplog.messages)
    assert all(record.levelno <= logging.WARNING for record in caplog.records), (
        """ Oh kak ya dovolen"""
    )
    assert True
    arguments = Query_arguments()
    arguments.query = ['were', 'have']
    callback_query(arguments)

    assert True


def test_load_documents(wiki_docs):
    assert isinstance(wiki_docs, dict)


def test_load_documents_exception():
    with pytest.raises(FileNotFoundError) as fnfe:
        articles = load_documents('wikipedia_sample/ikipedia_sample')


def test_build_inverted_index(wiki_docs):
    index_dict = build_inverted_index(wiki_docs)
    assert isinstance(index_dict, dict)


@pytest.fixture()
def wiki_docs():
    return load_documents('small_wiki_sample')


@pytest.fixture()
def load_inverted_index():
    return InvertedIndex.load('inv_index.dat')


def test_inverted_index_dump(wiki_docs):
    index_dict = build_inverted_index(wiki_docs)
    inv_index = InvertedIndex(index_dict)
    inv_index.dump('inv_index.dat')
    assert True


def test_inv_index_load(load_inverted_index):
    assert isinstance(load_inverted_index.inv_index, dict)


def test_inv_index_query(load_inverted_index, wiki_docs):
    words = ['after', 'were']
    doc_ind = InvertedIndex.query(load_inverted_index, words)
    assert {25, 290}.issubset(doc_ind)
    words = ['neizvesnie', 'slova']
    doc_ind = InvertedIndex.query(load_inverted_index, words)
    assert len(doc_ind) == 0
    words = ['after', 'were']
    index_dict = build_inverted_index(wiki_docs)
    inv_index = InvertedIndex(index_dict)
    doc_ind = inv_index.query(words)
    assert {25, 290}.issubset(doc_ind)
