"use strict";

const worldPopulation = 7900;

const percentageOfWorld3 = (population) => {
  return Math.round((population / worldPopulation) * 10000) / 100;
};

function describePopulation(country, population) {
  console.log(
    `${country} has ${population} millions people, so it's about ${percentageOfWorld3(
      population
    )}% of the world population`
  );
}

describePopulation("China", 1441);
describePopulation("India", 1380);
describePopulation("United States", 331);
