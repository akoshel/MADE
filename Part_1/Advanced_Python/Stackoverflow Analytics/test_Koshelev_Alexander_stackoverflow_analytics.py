import pytest
from task_Koshelev_Alexander_stackoverflow_analytics import Analytics, load_xml_dataset, load_stop_words,\
    process_cli_arguments, load_query_file, DEFAULT_QUERY_PATH, DEFAULT_STOP_WORDS_PATH, DEFAULT_DATASET_PATH
from argparse import Namespace

@pytest.fixture
def xml_file():
    filepath = DEFAULT_DATASET_PATH
    return load_xml_dataset(filepath)

@pytest.fixture
def get_stop_words():
    filepath = DEFAULT_STOP_WORDS_PATH
    return load_stop_words(filepath)

@pytest.fixture
def get_queries():
    filepath = DEFAULT_QUERY_PATH
    return load_query_file(filepath)

def test_process_cli_arguments():
    arguments = Namespace()
    arguments.xml_file = DEFAULT_DATASET_PATH
    arguments.stop_words = DEFAULT_STOP_WORDS_PATH
    arguments.queries = DEFAULT_QUERY_PATH
    process_cli_arguments(arguments)
    assert True

def test_load_xml_dataset():
    filepath = DEFAULT_DATASET_PATH
    load_xml_dataset(filepath)
    assert True
    with pytest.raises(FileNotFoundError) as fe:
        filepath = 'incorrect'
        load_xml_dataset(filepath)


def test_load_stop_words(get_stop_words):
    stop_words = get_stop_words
    assert 'amount' in stop_words

def test_load_query_file(get_queries):
    assert 4 == len(get_queries)

def test_query(xml_file, get_stop_words):
    anal = Analytics(xml_file, get_stop_words)
    query_sample = [2002, 2008, 3]
    result = anal.query(query_sample)
    assert 'using' in result['top'][0][0]

