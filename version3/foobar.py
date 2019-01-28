#!/usr/bin/env python3

import json
from datetime import datetime


def generate_html():
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


def lambda_handler(event, context):
    html = generate_html()

    # Format return value as appropriate for API Gateway's Lambda proxy integration
    # see: https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/
    return {"statusCode": 200, "headers": {"Content-Type": "text/html"}, "body": html}


def main():
    print(generate_html())


if __name__ == "__main__":
    exit(main())
