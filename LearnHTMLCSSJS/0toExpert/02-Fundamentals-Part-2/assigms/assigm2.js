"use strict";

const worldPopulation = 7900;

function percentageOfWorld1(country, population) {
  return `${country} has ${population} millions people, so it's about ${
    Math.round((population / worldPopulation) * 10000) / 100
  }% of the world population`;
}

console.log(percentageOfWorld1("China", 1441));
console.log(percentageOfWorld1("India", 1380));
console.log(percentageOfWorld1("United States", 331));

const percentageOfWorld2 = function (country, population) {
  return `${country} has ${population} millions people, so it's about ${
    Math.round((population / worldPopulation) * 10000) / 100
  }% of the world population`;
};

console.log(percentageOfWorld2("China", 1441));
console.log(percentageOfWorld2("India", 1380));
console.log(percentageOfWorld2("United States", 331));
