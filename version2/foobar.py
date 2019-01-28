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

    # Format return value as appropriate for API Gateway's Lambda proxy integration
    # see: https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/
    return {"statusCode": 200, "headers": {"Content-Type": "text/html"}, "body": html}


def main():
    print(lambda_handler(None, None))


if __name__ == "__main__":
    exit(main())
