'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btn = document.querySelector('.close-modal');
const btnsOpenModal = document.querySelectorAll('.show-modal');


const open_modal = function() {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
}
const close_modal = function() {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
}


for (let button of btnsOpenModal)
    button.addEventListener('click', open_modal)
btn.addEventListener('click', close_modal);
overlay.addEventListener('click', close_modal);

document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        close_modal();
    }
});