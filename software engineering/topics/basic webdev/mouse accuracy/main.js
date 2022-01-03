//-----------------------------
// Views
//-----------------------------
const StartView = document.querySelector(".Start");
const GameView = document.querySelector(".Game");
const ScoreboardView = document.querySelector(".Scoreboard");

//-----------------------------
// Start View
//-----------------------------
const startButton = document.querySelector(".Start button");
startButton.addEventListener("click", function () {
  StartView.style.display = "none";
  GameView.style.display = "block";
  startGame();
});

//-----------------------------
// Gameplay
//-----------------------------

// Keeping track of score
let numClicked = 0;
let numTotal = 0;

// The following times are in seconds
const TOTAL_TIME = 10;
const PAUSE_TIME = 1;
let TIME_LEFT = TOTAL_TIME;
const TARGET_INTERVAL = 0.5;

// Update the on-screen timer
const Timer = document.querySelector(".Timer");
Timer.innerText = TIME_LEFT; // First render
function updateTimerText() {
  Timer.innerText = --TIME_LEFT;
}

// Utility function for generating random integers
function randomInt(start, end) {
  return start + Math.floor(Math.random() * (end - start));
}

/**
 * startGame is called upon clicking start button,
 * and handles the timers for generating targets
 * and ending the game upon timeout
 */
function startGame() {
  // Set intervals for targets and timer
  const targetInterval = setInterval(generateTarget, TARGET_INTERVAL * 1000);
  const timerInterval = setInterval(updateTimerText, 1000);

  // Let the game run for TOTAL_TIME seconds
  setTimeout(() => {
    clearInterval(targetInterval);
    clearInterval(timerInterval);
  }, 1000 * (TOTAL_TIME - PAUSE_TIME));

  setTimeout(() => {
    clearGameView();
    initScoreboard();
  }, 1000 * TOTAL_TIME);
}

/* Generates a new randomly positioned target */
function generateTarget() {
  // Create a new target and style accordingly
  const target = document.createElement("div");
  target.className = "Target";
  target.style.left = `${randomInt(10, 90)}vw`;
  target.style.top = `${randomInt(10, 90)}vh`;

  // Pass event to target click handler
  target.addEventListener("click", (e) => {
    handleTargetClick(e);
  });

  GameView.appendChild(target);
  numTotal++;
}

/*
 * Adjusts score according to click and then remove target
 */
function handleTargetClick(e) {
  numClicked++;
  e.target.remove();
}

function clearGameView() {
  GameView.style.display = "none";
  ScoreboardView.style.display = "flex";
}

//-----------------------------
// Scoreboard
//-----------------------------
function initScoreboard() {
  const score = document.createElement("p");
  score.innerText = `You clicked ${numClicked} targets out of ${numTotal}!`;
  ScoreboardView.appendChild(score);
}
