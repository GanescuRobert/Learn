"use strict";
let countries = [
  ["China", 1439],
  ["India", 1380],
  ["Indonesia", 331],
  ["United States", 273],
];

console.log(countries.length === 4);

const worldPopulation = 7900;

const percentageOfWorld3 = (population) => {
  return Math.round((population[1] / worldPopulation) * 10000) / 100;
};

let percentages = countries.map(percentageOfWorld3);
console.log(percentages);
