#!/usr/bin/env python3

import json
from datetime import datetime


def lambda_handler(event, context):
    html = f"""
    <html>
    <head>
    <title>Hello VanPy!</title>
    </head>

    <body>
    <h1>Hello VanPy!</h1>

    <p>The current time is {datetime.now()}</p>
    </body>
    </html>
    """

    return html


def main():
    print(lambda_handler(None, None))


if __name__ == "__main__":
    exit(main())
