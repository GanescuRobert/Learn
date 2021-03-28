//1.
let populationMyCountry = 19.41;

//2.
// populationMyCountry = 13;
// populationMyCountry = 130;

const populationAverage = 33;

const aboveAverage = String(
  "Romania's population is " +
    (populationMyCountry - populationAverage) +
    " millions above average."
);
const belowAverage = String(
  "Romania's population is " +
    (populationAverage - populationMyCountry) +
    " millions below average."
);

populationMyCountry < populationAverage
  ? console.log(belowAverage)
  : console.log(aboveAverage);
