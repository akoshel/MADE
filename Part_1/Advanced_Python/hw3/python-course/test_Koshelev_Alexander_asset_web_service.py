from task_Koshelev_Alexander_asset_web_service import parse_cbr_currency_base_daily, parse_cbr_key_indicators, Asset, CompositeAsset


def test_parse_cbr_currency_base_daily():
    filename = 'sample_cbr_currency_base_daily.html'
    html_file = open(filename, 'r', encoding='utf-8')
    currencies = parse_cbr_currency_base_daily(html_file)
    assert 75 == int(currencies['USD'])


def test_parse_cbr_key_indicators():
    filename = 'sample_cbr_key_indicators.html'
    html_file = open(filename, 'r', encoding='utf-8')
    currencies = parse_cbr_key_indicators(html_file)
    assert 75 == int(currencies['USD'])


def test_asset_repr():
    asset = Asset('USD', 'Michael', 54.8, 0.05)
    assert asset.repr()[1] == 'Michael'

def test_composite_asset_repr():
    asset = Asset('USD', 'Michael', 54.8, 0.05)
    composite_asset = CompositeAsset()
    composite_asset.add(asset)
    composite_asset.add(asset)
    assert 2 == len(composite_asset.asset_list)