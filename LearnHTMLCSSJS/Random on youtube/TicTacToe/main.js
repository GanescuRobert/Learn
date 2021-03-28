//HTML Elements

const statusDiv = document.querySelector('.status');
const resetDiv = document.querySelector('.reset');
const cellDivs = document.querySelectorAll('.game-cell');
//console.log(cellDivs);
//Game constants

const xSymbol = '×';
const oSymbol = '○';


//Game variables

let gameIsLive = true;
let xIsNext = true;

// functions
const checkWin = (winCon) => {
    for (let i = 0; i < 8; i++) {
        if (winCon[i][0] === winCon[i][1] && winCon[i][1] === winCon[i][2]) {
            if (winCon[i][0] === 'X' || winCon[i][0] === 'O') {
                gameIsLive = false;
                winner = winCon[i][0];
                statusDiv.innerHTML = `<span>${winner} has won!</span>`;
            }
        }
    }
};

const checkTie = (cellsValue) => {
    if (gameIsLive) {
        let c = 0;
        for (let i = 0; i <= 8; i++) {
            if (cellsValue[i] === 'X' || cellsValue[i] === 'O') {
                c++;
            }
        }
        if (c == 9) {
            gameIsLive = false;
            statusDiv.innerHTML = "Game is tied!";
        }
    }
};

const checkGameStatus = () => {
    const cellsValue = [];

    for (let i = 0; i < 9; i++) {
        cellsValue[i] = (cellDivs[i].classList[1]);
    }

    let winCon = [
                [cellsValue[0], cellsValue[1], cellsValue[2]],
                 [cellsValue[3], cellsValue[4], cellsValue[5]],
                 [cellsValue[6], cellsValue[7], cellsValue[8]],
                 [cellsValue[0], cellsValue[3], cellsValue[6]],
                 [cellsValue[1], cellsValue[4], cellsValue[7]],
                 [cellsValue[2], cellsValue[5], cellsValue[8]],
                 [cellsValue[0], cellsValue[4], cellsValue[8]],
                 [cellsValue[2], cellsValue[4], cellsValue[6]]
                ];

    checkWin(winCon);
    checkTie(cellsValue)
    if (gameIsLive) {
        xIsNext = !xIsNext;
        if (xIsNext) {
            statusDiv.innerHTML = `${xSymbol} is next`;
        } else {
            statusDiv.innerHTML = `<span>${oSymbol} is next</span> `;
        }
    }

};
//Event handlers

const handleReset = () => {
    xIsNext = true;
    statusDiv.innerHTML = `${xSymbol} is next`;
    gameIsLive = true;
    for (cell of cellDivs) {
        cell.classList.remove("X");
        cell.classList.remove("O");
    }
};

const handleCellClick = (e) => {
    const classList = e.target.classList;
    //console.log(location);
    if (!gameIsLive)
        return;
    if (classList[2] === 'X' || classList[2] === 'O') {
        return;
    }
    if (xIsNext) {
        classList.add('X');
        checkGameStatus(classList);

    } else {
        classList.add('O');
        checkGameStatus();
    }
};

//Event listeners

resetDiv.addEventListener('click', handleReset);
for (const cellDiv of cellDivs) {
    if (gameIsLive === true) {
        cellDiv.addEventListener('click', handleCellClick);
    }
}
