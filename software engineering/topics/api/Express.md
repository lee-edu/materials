# Building an API with Express
[Express](https://expressjs.com/) is a Node framework that allows you to run a server and expose endpoints for users to access. In other words, it allows you to create an API!

## Objectives
This problem set allows you to practice:
    - Writing Javascript programs
    - Working on Node projects with `npm`
    - Using `express` to expose endpoints
    - Using Postman to test an API

## Task
### API
Write an API with the following `GET` endpoints. Each endpoint takes at least one parameter: an array of numbers.
  - `/add` returns the sum of the array
  - `/product` returns the product of the array
  - `/evens` returns an array of all even numbers of the original array
  - `/min` and `/max` should return the min/max number of the array, respectively
  - `/sort` should take an additional boolean parameter `ascending`, and return the correctly sorted array of numbers
  - `/target` should take an additional number parameter `target`, and return whether there are **two** numbers in the array that sum to `target`

Your code should use higher order functions where appropriate. For example, `reduce` will be very useful!

You should be using **Postman** to test each endpoint as you're writing this code.

## Submission
On Google Classroom, submit two files:
    1. Your `server.js` file
    2. A document that describes your Postman tests
