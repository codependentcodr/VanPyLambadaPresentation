# Building a Basic AWS Lambda Function Without Frameworks

Presentation for VanPy in Jan 2019: https://www.meetup.com/vanpyz/events/257223309/

## Outline

### What is Lambda and Serverless Computing?

* General overview of the idea of serverless, and how AWS Lambda is one such provider
  * others include Azure Functions and Google Cloud Functions
* Benefits:
  * no infrastructure to manage
  * easy to get up and running
  * cheap!
* Drawbacks:
  * it's a different way of approaching web development
  * thinking more in terms of functions than applications
* Great use cases:
  * "infinitely" scalable REST API's
  * weird periodic cron-job like things in the cloud
  * Alexa skills

### Lambda and Python

* It works!

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
