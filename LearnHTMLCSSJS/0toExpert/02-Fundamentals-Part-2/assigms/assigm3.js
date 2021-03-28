"use strict";

const worldPopulation = 7900;

const percentageOfWorld3 = (country, population) => {
  return `${country} has ${population} millions people, so it's about ${
    Math.round((population / worldPopulation) * 10000) / 100
  }% of the world population`;
};

console.log(percentageOfWorld3("China", 1441));
console.log(percentageOfWorld3("India", 1380));
console.log(percentageOfWorld3("United States", 331));
