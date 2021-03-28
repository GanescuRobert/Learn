"use strict";

let myCountry = {
  country: "Romania",
  capital: "Bucuresti",
  language: "romanian",
  population: 19,
  neighbours: [
    "Moldova",
    "Ukraina",
    "Slovakia",
    "Hungary",
    "Serbia",
    "Bulgaria",
  ],
};

console.log(`${myCountry.country} has ${myCountry.population} million ${myCountry.language}-speaking people, ${myCountry.neighbours.length} neighbouring countries and a capital called ${myCountry.capital}.'
`);

console.log(myCountry.population);
myCountry.population += 2;
console.log(myCountry.population);
myCountry["population"] -= 2;
console.log(myCountry.population);
