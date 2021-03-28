"use strict";

let country = "Romania";
let neighbours = [
  "Moldova",
  "Ukraina",
  "Slovakia",
  "Hungary",
  "Serbia",
  "Bulgaria",
];
neighbours.push("Utopia");
neighbours.pop();

if (!neighbours.includes("Germany"))
  console.log("Probably not a central European country :D");

neighbours.push("Sweden");
neighbours = neighbours.sort(() => Math.random() - 0.5);
console.log(neighbours);

neighbours[neighbours.indexOf("Sweden")] = "Republic of Sweden";
console.log(neighbours);
