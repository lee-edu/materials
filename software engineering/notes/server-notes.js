/**
 * In your Software Engineering folder, run
 * `npm init` to create a new Node project.
 * `package.json` contains metadata for Node projects,
 * and also handles dependencies.
 *
 * In your `package.json` you can also write scripts that
 * `npm` can run; for example,
 * `npm test` will run the `test` script.
 *
 * Install `nodemon` globally to make testing your code easier.
 *
 * You need to run `npm install express` in your project folder
 * in order to have access to the express library.
 */

// Load in the `express` library
const express = require("express");
const app = express();
const PORT = 4000;

// Use middleware that can parse JSON
app.use(express.json());

// Define the "/add" endpoint
// When a client makes a request, the server
// will call the defined callback function
app.get("/add", (request, response) => {
  // request.body is an Object representing the client's request
  const arr = request.body.array;
  const sum = 0; // Write actual code here!

  // Send HTTP code 200 back to the client
  // and the sum of the array in JSON format
  response.status(200).json(sum);
});

// Listen on PORT and log when the server is up
app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});