let plane = document.getElementById("plane");
let position = 0;

function fly() {
    position += 5;
    plane.style.left = position + "px";
}

setInterval(fly, 100);
let gameStarted = false;

document.getElementById("startBtn").addEventListener("click", function() {
  gameStarted = true;
  this.style.display = "none";
});
let plane = document.getElementById("plane");
let positionX = 100;
let positionY = 200;
let gameStarted = false;

// Start button click
document.getElementById("startBtn").addEventListener("click", function() {
  gameStarted = true;
  this.style.display = "none";
});

// Keyboard movement
document.addEventListener("keydown", function(event) {

  if (!gameStarted) return; // jab tak start nahi dabaya, kuch nahi hoga

  if (event.key === "ArrowUp") {
    positionY -= 10;
  }
  if (event.key === "ArrowDown") {
    positionY += 10;
  }
  if (event.key === "ArrowRight") {
    positionX += 10;
  }
  if (event.key === "ArrowLeft") {
    positionX -= 10;
  }

  plane.style.left = positionX + "px";
  plane.style.top = positionY + "px";
});
