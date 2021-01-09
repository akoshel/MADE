#!/usr/bin/env python3
import logging
import bs4
from flask import Flask, abort, request, jsonify
import requests

logger = logging.getLogger("asset")
app = Flask(__name__)


class Asset:
    def __init__(self, char_code: str = None, name: str = None, capital: float = None, interest: float = None):
        self.char_code = char_code
        self.name = name
        self.capital = capital
        self.interest = interest

    def calculate_revenue(self, years: int, currency: dict) -> float:
        revenue = self.capital * ((1.0 + self.interest) ** years - 1.0)
        return revenue * currency[self.char_code]

    @classmethod
    def build_from_str(cls, raw: str):
        logger.debug("building asset object...")
        name, capital, interest = raw.strip().split()
        capital = float(capital)
        interest = float(interest)
        asset = cls(name=name, capital=capital, interest=interest)
        return asset

    def repr(self):
        repr_ = [self.char_code, self.name, self.capital, self.interest]
        return repr_


class CompositeAsset(Asset):
    def __init__(self, asset=None):
        super().__init__()
        self.asset_classes = []
        self.asset_list = []
        self.name_list = []
        if asset:
            self.asset_classes.extend([asset])
            self.asset_list.extend([asset.repr()])
            self.name_list.append(asset.repr()[1])

    def add(self, asset):
        self.asset_classes.append(asset)
        self.asset_list.append(asset.repr())
        self.name_list.append(asset.repr()[1])

    def cleanup(self):
        self.asset_classes = []
        self.asset_list = []
        self.name_list = []

    def calculate_revenue(self, years: int, currency: dict) -> float:
        result = sum(asset.calculate_revenue(years, currency) for asset in self.asset_classes)
        return result

    def __repr__(self):
        return ' '.join([str(c) for c in sorted(self.asset_list)])


app_bank = CompositeAsset()


@app.errorhandler(404)
def page_not_found(e):
    return "This route is not found", 404


@app.route("/cbr/daily")
def cbr_currency_base_daily():
    html_page = get_currencies('https://www.cbr.ru/eng/currency_base/daily/')
    return parse_cbr_currency_base_daily(html_page.text)


@app.route("/cbr/key_indicators")
def cbr_currency_base_key_indicators():
    html_page = get_currencies('https://www.cbr.ru/eng/key-indicators/')
    return parse_cbr_key_indicators(html_page.text)


@app.route("/api/asset/add/<string:char_code>/<string:name>/<float:capital>/<int:interest>")
@app.route("/api/asset/add/<string:char_code>/<string:name>/<int:capital>/<int:interest>")
@app.route("/api/asset/add/<string:char_code>/<string:name>/<float:capital>/<float:interest>")
@app.route("/api/asset/add/<string:char_code>/<string:name>/<int:capital>/<float:interest>")
def add_asset(char_code: str, name: str, capital: float, interest: float, app_bank_cls=app_bank):
    """Add user"""
    if name in app_bank_cls.name_list:
        abort(403)
    new_asset = Asset(char_code, name, capital, interest)
    app_bank_cls.add(new_asset)
    return f"Asset '{name}' was successfully added"


@app.route("/api/asset/cleanup")
def app_bank_cleanup(app_bank_cls=app_bank):
    """Cleanup all users from app_bank"""
    app_bank_cls.cleanup()
    return ''


@app.route("/api/asset/list")
def app_bank_list(app_bank_cls=app_bank):
    """Receive all users assets"""
    return jsonify(sorted(app_bank_cls.asset_list))


@app.route("/api/asset/get")
def app_bank_get_users(app_bank_cls=app_bank):
    """Get selected users params"""
    names = request.args.getlist('name')
    result = []
    for bank_client in app_bank_cls.asset_list:
        if bank_client[1] in names:
            result.append(bank_client)
    return jsonify(result)


@app.route("/api/asset/calculate_revenue")
def app_bank_calculate_revenue(app_bank_cls=app_bank):
    """Calculate summary revenue"""
    result = {}
    daily_page = get_currencies('https://www.cbr.ru/eng/currency_base/daily/')
    key_indicators_page = get_currencies('https://www.cbr.ru/eng/key-indicators/')
    currencies = parse_cbr_currency_base_daily(daily_page.text)
    key_indicators = parse_cbr_key_indicators(key_indicators_page.text)
    currencies.update(key_indicators)
    currencies['RUB'] = 1
    periods = request.args.getlist('period')
    for years in periods:
        result[int(years)] = app_bank_cls.calculate_revenue(int(years), currencies)
    return jsonify(result)


def get_currencies(path: str):
    """get page text"""
    try:
        html_page = requests.get(path)
    except:
        abort(503, "CBR service is unavailable")
    if not html_page.ok:
        abort(503, "CBR service is unavailable")
    return html_page


def parse_cbr_currency_base_daily(html_file: str) -> dict:
    """Parse base daily currencies"""
    currencies = {}
    parser = bs4.BeautifulSoup(html_file, 'lxml')
    tables_list = parser.find_all('div', attrs={'class': 'table-wrapper'})
    for table in tables_list:
        currency_list = table.find_all('tr')
        cols = [t.text for t in currency_list[0].find_all('th')]
        char_index = cols.index('Char сode')
        rate_index = cols.index('Rate')
        unit_index = cols.index('Unit')
        for row in currency_list[1:]:
            cur_row_text = row.find_all('td')
            if not cur_row_text:
                continue
            currencies[cur_row_text[char_index].text] = float(cur_row_text[rate_index].text) / int(
                cur_row_text[unit_index].text)
        return currencies


def parse_cbr_key_indicators(html_file: str) -> dict:
    """Parse cbt key indicators"""
    currencies = {}
    parser = bs4.BeautifulSoup(html_file, 'lxml')
    currency_list = parser.find_all('div', attrs={'class': 'key-indicator_content offset-md-2'})
    for cur_part in currency_list:
        for row in cur_part.find_all('tr'):
            t = row.find_all('td')
            try:
                currency = t[0].find('div', attrs={"class": "col-md-3 offset-md-1 _subinfo"})
                val = row.find('td', attrs={"class": "value td-w-4 _bold _end mono-num"})
                if not val:
                    val = t[2]
                val = float(val.text.replace(',', ''))
            except:
                continue
            if currency and val:
                currencies[currency.text] = val
    return currencies
