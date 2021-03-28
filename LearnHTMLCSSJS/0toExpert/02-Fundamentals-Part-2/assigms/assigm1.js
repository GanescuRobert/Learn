"use strict";

function describeCountry(country, population, capitalCity) {
  return `${country} has ${population} millions people and the most populated city is ${capitalCity}`;
}

console.log(describeCountry("China", 1439323776, "Shanghai"));
console.log(describeCountry("India", 1380004385, "Mumbai"));
console.log(describeCountry("United States", 331002651, "New York City"));
