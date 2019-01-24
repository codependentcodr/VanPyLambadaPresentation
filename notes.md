# Building a Basic AWS Lambda Function Without Frameworks

Presentation for VanPy in Jan 2019: https://www.meetup.com/vanpyz/events/257223309/

### Random thoughts

* The role of API gateway
* permissions (IAM stuff)
* different environments
* what does lambda pass as arguments to your fn
* returning HTML vs JSON
* story of recursive lambda, and surprises on your bill
* how to test, separation of lambda interface with rest of your code

### Gotchas

* Compiled dependencies

## What I Submitted

Building a Basic AWS Lambda Function Without Frameworks

"Give an example of building a basic AWS Lambda function in Python, and how one
would go about unit testing that function.  The function would be a simple
response endpoint that returns a rendered HTML page (generated from a Jinja2
template).

Would include:

* some basics of how to return HTML from Lambda
* some basics of how to write a Python-based AWS Lambda function, and how to
  turn it into a public HTTP endpoint that could be hit by real users via AWS
  API Gateway
* How to deal with compiled 3rd party dependencies (ex: lxml) in an AWS Lambda
  function written in Python
* some basics around how to separate Lambda-specific details from domain/problem
  specific concerns to aid with unit testing

The key idea is to approach this as an example of demystifying serverless
computing, as everything will be pure Python with no reliance on frameworks like
Zappa or Serverless.com"


## Presentation Notes

Notes on creating lambda:


create lambda
Don't author from scratch, instead blueprint, and "hello-world-python3"

Do simple example of the boilerplate it gives you
Do the test there

Go through fields,

* env vars
* execution role is permissions
* Basic settings -- memory and timeout, these are important

Illustrate how writing inline sucks.
Demonstrate taking code putting into local editor, saving file, zipping it & uploading.
Rename the module, function, etc.

Nothign magic, we could return whatever we want, like some raw html
-- do that.
-- make it "dynamic", embed the local time or something

Ok, note that this is plain python so you can run locally

run python, import function & run in the interpreter.
Now flesh out into ifmain block & run as cmd line script
Can we still upload to lambda?
Yes, exact same code, can run as a local cmd line script, or upload to lambda.  Cool!


Ok, now API gateway since we want users to be able to hit it on the web

Proxy integration yes.
Run it after doing that and notice you get error "Execution failed due to configuration error: Malformed Lambda proxy response"
This is because proxy response means your lambda has to return specifically formatted json.

```python
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html,
    }
```

https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/
