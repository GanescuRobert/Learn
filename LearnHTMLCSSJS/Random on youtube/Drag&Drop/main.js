const fill = document.querySelector('.fill');
const empties = document.querySelectorAll('.empty-cell');

// Fill Listeners

fill.addEventListener("dragstart", dragStart);
fill.addEventListener("dragend", dragEnd);

// Drag functions

// Loop through empties and call drag events

for (const empty of empties) {
    empty.addEventListener('dragover', dragOver);
    empty.addEventListener('dragenter', dragEnter);
    empty.addEventListener('dragleave', dragLeave);
    empty.addEventListener('drop', dragDrop);
}

function dragStart() {
    //console.log("start");
    this.className += ' hold';
    setTimeout(() => this.className = 'invisible', 0);
}

function dragEnd() {
    //console.log("end");
    this.className = 'fill'
}

function dragOver(e) {
    e.preventDefault();
    //console.log("Over");
}

function dragEnter(e) {
    //console.log("Enter");
    e.preventDefault();
    this.className += ' hovered';
}

function dragLeave() {
    //console.log("Leave");
    this.className = 'empty-cell';
}

function dragDrop() {
    //console.log("Drop");
    this.className = 'empty-cell';
    this.append(fill);
}
