#!/usr/bin/env python3

import json
from datetime import datetime

from lxml import html
from jinja2 import Environment, FileSystemLoader, select_autoescape


def generate_html():
    env = Environment(
        loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
    )
    template = env.get_template("welcome.jinja2")
    return template.render(the_time=datetime.now())


def lambda_handler(event, context):
    html = generate_html()

    return {"statusCode": 200, "headers": {"Content-Type": "text/html"}, "body": html}


def main():
    print(generate_html())


if __name__ == "__main__":
    exit(main())
