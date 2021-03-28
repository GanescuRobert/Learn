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
  describe: function () {
    console.log(
      `${this.country} has ${this.population} million ${this.language}-speaking people, ${this.neighbours.length} neighbouring countries and a capital called ${this.capital}.'`
    );
  },
  checkIsland: function () {
    this.isIsland = this.neighbours.length === 0;
    return this.isIsland;
  },
};
if (!myCountry.checkIsland()) myCountry.describe();
