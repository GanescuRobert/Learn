console.log("Hello world");

var button = document.querySelector(".button");
var image = document.querySelector(".img-lucrare");
var wasClicked = false;

button.addEventListener("click", function () {
    if (!wasClicked) {
        image.style.width = "250px";
        image.style.height = "300px"
        console.log("Button is pushed True");
        wasClicked = true;
    }
    else {
        image.style.width = "150px";
        image.style.height = "200px"
        console.log("Button is pushed False"); 
        wasClicked = false;
    }
}, false);