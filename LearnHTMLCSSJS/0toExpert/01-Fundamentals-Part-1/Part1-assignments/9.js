// Previous code commented.

let myCountry = "Romania";
let myLangaugage = "Romana";
let myPopulation = 19.31;
let myIsIsland = false;

console.log(typeof myCountry);
if (myCountry === "Canada") console.log("Sorry, I live in Canada :D");
else {
  myCountry = String(prompt("Country: "));
  myLangaugage = String(prompt("Langugage: "));
  myPopulation = Number(prompt("Population: "));
  ans = String(prompt("Is island ?(y/n): "));
  if (ans === "y") myIsIsland = true;
  else myIsIsland = false;
}

const wishLanguage = "English";
const wishPopulation = 50;
const wishIsIsland = false;

if (
  (wishLanguage === myLangaugage) &
  (wishPopulation === myPopulation) &
  (myIsIsland <= wishIsIsland)
)
  console.log(`You should live in ${myCountry} :)`);
else console.log(`${myCountry} does not meet your criteria :(`);
