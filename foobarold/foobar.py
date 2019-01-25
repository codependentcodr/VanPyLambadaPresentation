#!/usr/bin/env python3

import json
from lxml import html
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape


def lambda_handler(event, context):
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
    )

    template = env.get_template("welcome.jinja2")
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": template.render(the_time=datetime.now()),
    }


def main():
    print(lambda_handler(None, None))


if __name__ == "__main__":
    exit(main())
