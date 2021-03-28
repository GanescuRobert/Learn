"use strict";
const listOfNeighbours = [
  ["Canada", "Mexico"],
  ["Spain"],
  ["Norway", "Sweden", "Russia"],
];

for (let i = 0; i < listOfNeighbours.length; i++) {
  console.log(`Country${i + 1} have those neighbours: `);
  console.log(listOfNeighbours[i].join(" --- "));
}
