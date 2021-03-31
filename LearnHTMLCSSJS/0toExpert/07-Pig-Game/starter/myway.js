'use strict';

let player0_score = Number(document.querySelector('#score--0').textContent);
let player1_score = Number(document.querySelector('#score--1').textContent);
let current_score = 0;



const get_active_player = function() {
    return document.querySelector('.player--0').classList.contains('player--active') ? "Player0" : "Player1";
}
const set_dice_image = function(value) {
    document.querySelector('.dice').src = 'dice-' + value + '.png';
}
const set_current_score = function() {
    if (get_active_player() === "Player0") {
        document.querySelector('#current--0').textContent = current_score;
    } else {
        document.querySelector('#current--1').textContent = current_score;
    }
}
const set_score = function() {
    if (get_active_player() === "Player0") {
        document.querySelector('#score--0').textContent = player0_score;
    } else {
        document.querySelector('#score--1').textContent = player1_score;
    }
}
const end_turn = function() {
    let player0 = document.querySelector('.player--0');
    let player1 = document.querySelector('.player--1');
    if (get_active_player() === "Player0") {
        player0.classList.remove('player--active');
        player1.classList.add('player--active');
    } else {
        player0.classList.add('player--active');
        player1.classList.remove('player--active');
    }
}



document.querySelector('.btn--roll').addEventListener('click', function() {
    let dice_value = Math.trunc(Math.random() * 6) + 1;
    current_score += dice_value;

    set_dice_image(dice_value);
    set_current_score()

    if (dice_value === 1) {
        current_score = 0;
        set_current_score();
        end_turn();
    }

});

document.querySelector('.btn--hold').addEventListener('click', function() {
    if (get_active_player() === "Player0") {
        player0_score += current_score;
    } else {
        player1_score += current_score;
    }
    current_score = 0;
    set_current_score();
    set_score();

    end_turn()
});

document.querySelector('.btn--new').addEventListener('click', function() {
    player0_score = 0;
    player1_score = 0;
    current_score = 0;
    document.querySelector('.player--0').classList.add('player--active');
    document.querySelector('.player--1').classList.remove('player--active');
    document.querySelector('#score--0').textContent = player0_score;
    document.querySelector('#score--1').textContent = player1_score;
    document.querySelector('#current--0').textContent = current_score;
    document.querySelector('#current--1').textContent = current_score;
});