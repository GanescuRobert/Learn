//1. 5. 7.
let numNeighbours = Number(
  prompt("How many neighbour countries does your country have?")
);

//2.
if (numNeighbours == 1) console.log("Only 1 border!");
//3.
else if (numNeighbours > 1) console.log("More than 1 border!");
//4.
else console.log("No borders");

//6.
console.log(typeof numNeighbours);
if (numNeighbours === 1) console.log("Only 1 border!");
else if (numNeighbours > 1) console.log("More than 1 border!");
else console.log("No borders");
