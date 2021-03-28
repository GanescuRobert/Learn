"use strict";

const calcAverage = (scores) => {
  return scores.reduce((a, b) => a + b, 0) / scores.length;
};
const checkWinner = (avgDolphins, avgKoalas) => {
  if (avgDolphins >= 2 * avgKoalas) return "Dolphins";
  if (avgKoalas >= 2 * avgDolphins) return "Koalas";
  if (avgKoalas === avgDolphins) return "Tie";
  return "No team wins";
};

// * Data1
let dolphinsScore = [44, 23, 71];
let koalasScore = [65, 54, 49];

console.log(calcAverage(dolphinsScore));
console.log(calcAverage(koalasScore));

console.log(
  "Result of the game: ",
  checkWinner(calcAverage(dolphinsScore), calcAverage(koalasScore))
);

// * Data2
dolphinsScore = [85, 54, 41];
koalasScore = [23, 34, 27];

console.log(calcAverage(dolphinsScore));
console.log(calcAverage(koalasScore));

console.log(
  "Result of the game: ",
  checkWinner(calcAverage(dolphinsScore), calcAverage(koalasScore))
);
