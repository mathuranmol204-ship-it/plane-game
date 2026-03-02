let plane = document.getElementById("plane");
let position = 0;

function fly() {
    position += 5;
    plane.style.left = position + "px";
}

setInterval(fly, 100);
