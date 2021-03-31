'use strict';


// console.log(
//     document.querySelector('.message').textContent);
// document.querySelector('.message').textContent = 'Correct Number 🎉';
// document.querySelector('.number').textContent = 13;
// document.querySelector('.score').textContent = 10;
// document.querySelector('.guess').value = 10;

let secretNumber = Math.trunc(Math.random() * 20) + 1;
let score = 20;
let highscore = 0;

const displayMessage = function(message) {
    document.querySelector('.message').textContent = message;
}
const displayNumber = function(number) {
    document.querySelector('.number').textContent = number;
}
document.querySelector('.check').addEventListener('click', function() {
    const guess = Number(document.querySelector('.guess').value);
    if (!guess) {
        displayMessage("⛔ No number!");
    } else if (guess === secretNumber) {
        displayMessage('Correct Number 🎉');
        displayNumber(secretNumber);
        document.querySelector('header').style.backgroundColor = '#0d8051';
        document.querySelector('.number').style.width = '25rem';
        if (score > highscore) {
            highscore = score;
            document.querySelector('.highscore').textContent = highscore;
        }
    } else if (score > 1) {
        score--;
        let message = guess > secretNumber ? '📈 Too high!' : '📉 Too low!';
        displayMessage(message);
        document.querySelector('.score').textContent = score;
    } else {
        score = 0;
        displayMessage('💥 You lost the game!');
        displayNumber(secretNumber);
        document.querySelector('header').style.backgroundColor = '#6b011e';
        document.querySelector('.number').style.width = '25rem';
        document.querySelector('.score').textContent = score;
    }

});



document.querySelector('.again').addEventListener('click', function() {
    score = 20;
    secretNumber = Math.trunc(Math.random() * 20) + 1;
    displayNumber('?');
    displayMessage('Start guessing...');
    document.querySelector('.guess').value = '';
    document.querySelector('.score').textContent = score;
    document.querySelector('header').style.backgroundColor = "#222";
    document.querySelector('.number').style.width = "15rem";
});