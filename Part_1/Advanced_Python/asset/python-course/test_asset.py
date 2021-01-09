import pytest
from argparse import Namespace
from unittest.mock import patch, call, MagicMock
from asset import process_cli_arguments, do_busy_work, DEFAULT_SMALL_SLEEP_TIME, DEFAULT_BIG_SLEEP_TIME, Asset


@patch("asset.load_asset_from_file")
def test_process_arguments_call_load_once(mock_load_asset_from_file):
    with open("asset_example.txt") as fin:
        arguments = Namespace(asset_fin=fin,
                              periods=[1, 2, 5],
                              )
        expected_calls = [
            call(fin),
            call().calculate_revenue(1),
            call().calculate_revenue(2),
            call().calculate_revenue(5),
        ]
        process_cli_arguments(arguments)
        mock_load_asset_from_file.assert_called_once()
        mock_load_asset_from_file.assert_called_once_with(fin)
        mock_load_asset_from_file.assert_has_calls(expected_calls, any_order=True)

@patch("asset.sleep")
@patch("time.sleep")
def test_can_mock_time_sleep(mock_time_sleep, mock_asset_sleep):
    with open("asset_example.txt") as fin:
        arguments = Namespace(asset_fin=fin,
                              periods=[1, 2, 5],
                              )
        process_cli_arguments(arguments)
        mock_time_sleep.assert_called_once_with(DEFAULT_SMALL_SLEEP_TIME)
        mock_asset_sleep.assert_called_once_with(DEFAULT_BIG_SLEEP_TIME)

@patch("asset.Asset")
def test_asset_calculate_revenue_always_return_100500(mock_asset_class, capsys):
    #mock_asset_class = MagicMock(spec=Asset)
    mock_asset_class.calculate_revenue.return_value = 100500
    mock_asset_class.build_from_str.return_value = mock_asset_class
    with open("asset_example.txt") as fin:
        arguments = Namespace(asset_fin=fin,
                              periods=[1, 2, 5],
                              )
        process_cli_arguments(arguments)
        captured = capsys.readouterr()
        for line in captured.out.splitlines():
            assert "100500" in line, "Ohuet soobshenie"
