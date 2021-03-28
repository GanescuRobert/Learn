let populationMyCountry = 19.41;
let myCountry = "Romania";
let myContinent = "Eune";
let language = "Romana";
const populationFinland = 6;
const populationAverage = 33;

const description = `${myCountry} is in ${myContinent}, and its ${populationMyCountry} million people speak ${language}`;
//1.
console.log(populationMyCountry / 2);
//2.
populationMyCountry++;
console.log(populationMyCountry);
//3.
if (populationMyCountry > populationFinland) console.log("Yes");
else console.log("No");
//4.
if (populationMyCountry < populationAverage) console.log("Yes");
else console.log("No");

console.log(description);
