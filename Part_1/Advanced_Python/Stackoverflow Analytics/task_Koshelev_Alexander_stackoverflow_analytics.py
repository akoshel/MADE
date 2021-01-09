import re
from datetime import datetime
import logging
import logging.config
import json
from collections import defaultdict, Counter
from argparse import ArgumentParser
import bs4
import yaml

DEFAULT_DATASET_PATH = 'sample_stackoverflow_posts_sample.xml'
DEFAULT_STOP_WORDS_PATH = 'sample_stop_words_en.txt'
DEFAULT_QUERY_PATH = 'sample_queries.csv'
DEFAULT_LOGGING_CONFIG_FILE = 'logging.conf.yml'
logger = logging.getLogger(__name__)


class Analytics:
    """Class to read dataset and stop words and print analytics"""

    def __init__(self, dataset, stop_words):
        parser = bs4.BeautifulSoup(dataset, 'lxml')
        self.stop_words = stop_words
        self.posts = parser.find_all('row')

    def query(self, query: list) -> dict:
        """Get query"""
        logger.debug('got query "%i,%i,%i"', query[0], query[1], query[2])
        words = defaultdict(int)
        for post in self.posts:
            date = datetime.strptime(post['creationdate'], '%Y-%m-%dT%H:%M:%S.%f')
            if query[0] <= date.year <= query[1] and post['posttypeid'] == '1':
                for word in set(re.findall(r"\w+", post['title'].lower())):
                    word = word.strip()
                    if word not in self.stop_words:
                        words[word] += int(post['score'])

        words_sorted = {k: v for k, v in sorted(words.items())}
        result_words = Counter(words_sorted).most_common(query[2])
        if len(result_words) < query[2]:
            logger.warning('not enough data to answer, found %i words out of %i for period "%i,%i"',
                           len(result_words), query[2], query[0], query[1])
        result = {'start': query[0], 'end': query[1], 'top': [[k, v] for k, v in result_words]}
        return result


def load_xml_dataset(filepath: str = DEFAULT_DATASET_PATH):
    """Load dataset"""
    logger.info('process XML dataset, ready to serve queries')
    xml_file = open(filepath, 'r', encoding='utf-8')
    return xml_file


def load_stop_words(filepath: str = DEFAULT_STOP_WORDS_PATH) -> set:
    """Load stop words"""
    stop_words_raw = open(filepath, 'r', encoding='koi8-r')
    stop_words = set()
    for word in stop_words_raw:
        stop_words.add(word.strip())
    return stop_words


def load_query_file(filepath: str = DEFAULT_QUERY_PATH) -> list:
    """Load query file"""
    queries_raw = open(filepath, 'r')
    queries = []
    for query in queries_raw:
        queries.append(list(map(int, query.split(','))))
    return queries


def setup_logging():
    """setup logging"""
    with open(DEFAULT_LOGGING_CONFIG_FILE) as config_fin:
        logging.config.dictConfig(yaml.safe_load(config_fin))


def process_cli_arguments(arguments):
    """Process CLI arguments"""
    print_analytic(arguments.xml_file, arguments.stop_words, arguments.queries)


def print_analytic(questions_path: str, stop_words_path: str, queries_path: str):
    """Get asked query"""
    xml_file = load_xml_dataset(questions_path)
    stop_words = load_stop_words(stop_words_path)
    queries = load_query_file(queries_path)
    analytics = Analytics(xml_file, stop_words)
    for query in queries:
        answer = analytics.query(query)
        print(json.dumps(answer))


def setup_parser(parser):
    parser.add_argument("-q", "--questions", dest="xml_file")
    parser.add_argument("-s", "--stop-words", dest="stop_words")
    parser.add_argument("-e", "--queries", dest="queries")


def main() -> None:
    setup_logging()
    parser = ArgumentParser(
        prog="analytics",
        description="tool to get analytics",
    )
    setup_parser(parser)
    arguments = parser.parse_args()
    process_cli_arguments(arguments)
    logger.info('finish processing queries')


if __name__ == "__main__":
    main()
