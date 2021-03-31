'use strict'

const reset_highscore = 0
const reset_score = 20;
let highscore = 0;
let guess_number;
let score;

function generate_random_number(min, max) {
    return Number(Math.floor(Math.random() * (max - min) + min));
}

function get_number() {
    return Number(document.querySelector(".guess").value);
}

function get_score() {
    return Number(document.querySelector(".score").innerHTML);
}

function set_highscore(score_value) {
    document.querySelector(".highscore").innerHTML = score_value;
}

function new_game() {
    document.querySelector(".highscore").innerHTML = reset_highscore.toString();
    highscore = reset_highscore;
}

function reset_game() {
    if (end_game()) {
        new_game();
        document.querySelector(".again").innerHTML = "Again";
    }
    document.querySelector(".guess").innerHTML = "";
    document.querySelector(".score").innerHTML = reset_score.toString();
    document.querySelector(".message").innerHTML = "Start guessing...";
    document.querySelector("header").style.background = "#222";
    display_on();
    main();
}


function end_game() {
    return highscore == reset_score;
}


function display_button_off() {
    document.querySelector(".check").style.display = "none";
}

function display_button_on() {

    document.querySelector(".check").style.display = "block";
}

function show_win_setup() {

    if (end_game()) {
        document.querySelector(".again").innerHTML = "New game!";
    }
    document.querySelector("header").style.background = "#0d8051";
    document.querySelector(".message").innerHTML = "You managed to get a new high score !!!";
    document.querySelector(".highscore").innerHTML = highscore.toString();
    display_button_off();
}

function show_lose_setup() {
    document.querySelector("header").style.background = "#6b011e";
    document.querySelector(".message").innerHTML = "Your score is less than high score !!!";
    display_button_off();
}

function try_again_setup() {
    document.querySelector(".guess").innerHTML = "";
    document.querySelector(".score").innerHTML = score.toString();
    document.querySelector(".message").innerHTML = "Wrong! Try again.";
}

function main() {
    guess_number = generate_random_number(1, 20);
    score = get_score();
    console.log(score, guess_number);

}

function check() {
    let my_number = get_number();

    if (my_number === guess_number) {
        if (score >= highscore) {
            highscore = score;
            show_win_setup()
            return;
        } else {
            show_lose_setup()
            return;
        }
    } else {
        if (score > 0) {
            score -= 1;
            try_again_setup();
        }
        if (score === 0) {
            show_lose_setup()
            return;
        }

    }
}

main();