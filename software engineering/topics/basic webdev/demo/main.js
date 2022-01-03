let count = 0;
const counterLabel = document.querySelector(".CounterLabel")
const counterButton = document.querySelector(".CounterButton")
counterButton.addEventListener("click", function () {
    count++
    counterLabel.innerText = count
})

const loudButton = document.querySelector(".LoudButton")
loudButton.addEventListener("click", function () {
    loudButton.innerText += "!"
})

function foo(){}
const foo = function(){}
const foo = () => {}

