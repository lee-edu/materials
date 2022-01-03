// Name:

const REPLACE_ME = null;
/* ----- Implement the following functions. -----*/

// Return the total price of all items _without using a loop_
// Hint: look up JS Array.prototype.reduce
const getTotalPrice = cart => REPLACE_ME;

// Return a list of the elements in cart for which fn returns true
// Hint: look up JS Array.prototype.filter
const filterBy = fn => cart => REPLACE_ME;

// Return a list of elements in cart for which fn returns false
// Hint: use filterBy
const rejectBy = fn => REPLACE_ME;

// Return a function that filters a given cart by
// whether the item's price is over the given threshold
// Hint: use filterBy
const filterByPrice = threshold => REPLACE_ME;

// Return a function that filters a given cart by
// whether the item has the specified tag
// Hint: use filterBy
const filterByTag = tag => REPLACE_ME;

// Return a cart in which the discountFn is applied to each item
const applyDiscount = discountFn => cart => REPLACE_ME;

// Return a function which applies
// the percent discount to each item in the given cart
// Hint: use applyDiscount
const applyPercentDiscount = percent => REPLACE_ME;

// Return a list of values for the specified attribute
// For example, getValues("price")(exampleCart) >>> [119.44, 347.29, ... ]
// Hint: use the spread operator `...` and `reduce`
const getValues = attribute => cart => REPLACE_ME;

// Return a cart that is sorted by the given attribute
// Hint: look up Array.prototype.sort and compareFunctions
const sortCart = compareFn => cart => REPLACE_ME;

// Return a cart that is sorted by price (ascending)
// Hint: use sortCart
const sortByPrice = cart => REPLACE_ME;

/* ----- TEST YOUR CODE BELOW ----- */
// Use exampleCart to test your code!
let exampleCart = [{
        "_id": 6067,
        "price": 119.44,
        "image": "http://placehold.it/32x32",
        "quantity": 7,
        "name": "ex veniam",
        "description": "Cillum non sint voluptate incididunt sunt proident labore enim eiusmod.",
        "tags": [
            "est",
            "sit",
            "sit",
            "ut",
            "mollit",
            "commodo",
            "ad"
        ]
    },
    {
        "_id": 5760,
        "price": 347.29,
        "image": "http://placehold.it/32x32",
        "quantity": 3,
        "name": "exercitation velit",
        "description": "Dolore ut aliquip officia anim non quis ex ex ea tempor aliquip nostrud do deserunt.",
        "tags": [
            "commodo",
            "enim",
            "ea",
            "aliqua",
            "deserunt",
            "tempor",
            "amet"
        ]
    },
    {
        "_id": 1707,
        "price": 499.75,
        "image": "http://placehold.it/32x32",
        "quantity": 8,
        "name": "sit ea",
        "description": "Ipsum tempor veniam consequat eiusmod cupidatat officia ea exercitation deserunt irure incididunt fugiat deserunt consequat.",
        "tags": [
            "occaecat",
            "do",
            "do",
            "aliqua",
            "qui",
            "anim",
            "sit"
        ]
    },
    {
        "_id": 7220,
        "price": 475.3,
        "image": "http://placehold.it/32x32",
        "quantity": 4,
        "name": "sunt quis",
        "description": "Cupidatat magna nulla est elit laboris consequat.",
        "tags": [
            "id",
            "pariatur",
            "aute",
            "nulla",
            "eu",
            "est",
            "nostrud"
        ]
    },
    {
        "_id": 4346,
        "price": 23.93,
        "image": "http://placehold.it/32x32",
        "quantity": 1,
        "name": "exercitation cupidatat",
        "description": "Deserunt pariatur est laboris ullamco do.",
        "tags": [
            "esse",
            "laboris",
            "consequat",
            "est",
            "amet",
            "culpa",
            "nisi"
        ]
    },
    {
        "_id": 8006,
        "price": 171.17,
        "image": "http://placehold.it/32x32",
        "quantity": 6,
        "name": "qui veniam",
        "description": "Quis adipisicing esse labore eiusmod tempor non dolore nisi reprehenderit eiusmod pariatur nisi.",
        "tags": [
            "aliqua",
            "deserunt",
            "aute",
            "deserunt",
            "magna",
            "sit",
            "officia"
        ]
    },
    {
        "_id": 6252,
        "price": 278.34,
        "image": "http://placehold.it/32x32",
        "quantity": 1,
        "name": "exercitation nisi",
        "description": "Anim nulla sunt voluptate non.",
        "tags": [
            "cupidatat",
            "officia",
            "aute",
            "ea",
            "ex",
            "quis",
            "proident"
        ]
    },
    {
        "_id": 2120,
        "price": 282.13,
        "image": "http://placehold.it/32x32",
        "quantity": 10,
        "name": "est ut",
        "description": "Sit commodo sit excepteur sit minim.",
        "tags": [
            "ipsum",
            "consequat",
            "consequat",
            "ipsum",
            "proident",
            "anim",
            "quis"
        ]
    },
    {
        "_id": 8745,
        "price": 144.48,
        "image": "http://placehold.it/32x32",
        "quantity": 5,
        "name": "ut velit",
        "description": "Consequat reprehenderit sunt exercitation nulla laborum nostrud occaecat ex sint in dolor deserunt.",
        "tags": [
            "sunt",
            "qui",
            "labore",
            "quis",
            "id",
            "aliqua",
            "minim"
        ]
    },
    {
        "_id": 4710,
        "price": 191.5,
        "image": "http://placehold.it/32x32",
        "quantity": 5,
        "name": "ad ex",
        "description": "Id do id Lorem laboris aliqua cupidatat velit ea fugiat anim commodo tempor pariatur.",
        "tags": [
            "velit",
            "enim",
            "pariatur",
            "est",
            "fugiat",
            "ut",
            "minim"
        ]
    },
    {
        "_id": 8125,
        "price": 487.97,
        "image": "http://placehold.it/32x32",
        "quantity": 6,
        "name": "nulla duis",
        "description": "Magna enim sunt sint aliqua eu cillum.",
        "tags": [
            "incididunt",
            "labore",
            "consectetur",
            "culpa",
            "velit",
            "ullamco",
            "aliqua"
        ]
    },
    {
        "_id": 1613,
        "price": 419.1,
        "image": "http://placehold.it/32x32",
        "quantity": 5,
        "name": "elit aliquip",
        "description": "Quis laborum magna anim ullamco ipsum id in laborum in enim sit quis aliquip consequat.",
        "tags": [
            "aliqua",
            "cillum",
            "veniam",
            "reprehenderit",
            "velit",
            "sint",
            "dolor"
        ]
    },
    {
        "_id": 2147,
        "price": 181.46,
        "image": "http://placehold.it/32x32",
        "quantity": 2,
        "name": "dolor culpa",
        "description": "Consectetur ad dolore ullamco cillum enim magna labore culpa anim.",
        "tags": [
            "quis",
            "nisi",
            "eiusmod",
            "minim",
            "do",
            "Lorem",
            "consequat"
        ]
    },
    {
        "_id": 1351,
        "price": 143.84,
        "image": "http://placehold.it/32x32",
        "quantity": 1,
        "name": "aute amet",
        "description": "Id eu reprehenderit Lorem dolor ut proident consequat ad adipisicing Lorem aliqua adipisicing minim amet.",
        "tags": [
            "enim",
            "est",
            "deserunt",
            "ex",
            "sint",
            "officia",
            "duis"
        ]
    },
    {
        "_id": 3497,
        "price": 127.77,
        "image": "http://placehold.it/32x32",
        "quantity": 7,
        "name": "culpa magna",
        "description": "Excepteur mollit ut cillum cillum.",
        "tags": [
            "labore",
            "eu",
            "dolore",
            "mollit",
            "esse",
            "ullamco",
            "et"
        ]
    },
    {
        "_id": 9422,
        "price": 140.82,
        "image": "http://placehold.it/32x32",
        "quantity": 4,
        "name": "adipisicing ex",
        "description": "Deserunt reprehenderit qui in aliqua sit ea irure ad eiusmod cillum elit.",
        "tags": [
            "duis",
            "proident",
            "ea",
            "nostrud",
            "dolor",
            "aute",
            "culpa"
        ]
    }
];
