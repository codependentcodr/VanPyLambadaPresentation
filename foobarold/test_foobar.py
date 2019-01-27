from datetime import datetime
from unittest.mock import Mock, patch

from foobar import generate_html, lambda_handler

@patch('foobar.datetime')
def test_generate_html_inserts_current_time(mock_datetime):
    current_time = datetime.now()
    mock_datetime.now.return_value = current_time

    result = generate_html()

    assert str(current_time) in result


@patch('foobar.generate_html')
def test_lambda_handler_response(mock_generate_html):
    mock_generate_html.return_value = "Test result"
    expected = {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": "Test result",
    }

    result = lambda_handler({}, {})
    
    assert result == expected
