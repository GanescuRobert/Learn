"use strict";

// *2. Activating Strict Mode

let hasDriversLicense = false;
const passTest = true;

if (passTest) hasDriversLicense = true;

if (hasDriversLicense) console.log("I can drive!");

// ! reserved words
// const interface = "Audio";
// const private = 534;

// *3. Functions
function logger() {
  console.log("My name is Jonas");
}

// calling / running / invokeing function
logger();

function fruitProcessor(apples, oranges) {
  return Math.min(apples, oranges);
}
let apples = Math.round(Math.random() * 100);
let oranges = Math.round(Math.random() * 100);
console.log(
  `From ${apples} appels and ${oranges} oranges, we can make ${fruitProcessor(
    apples,
    oranges
  )} juices`
);

// *4. Function declarations vs Expressions

//declarations
function calcAge1(birthYeah) {
  return 2037 - birthYeah;
}
const age1 = calcAge1(1991);
console.log(age1);

//Expressions
const calcAge2 = function (birthYeah) {
  return 2037 - birthYeah;
};
const age2 = calcAge2(1991);
console.log(age1, age2);

// *5. Arrow Function

const calcAge3 = (birthYeah) => 2037 - birthYeah;
const age3 = calcAge3(1991);
console.log(age3);

const yearsUntilRetirement = (birthYeah, firstname) => {
  const age4 = 2037 - birthYeah;
  return `${firstname} retires in ${65 - age4} years`;
};

const yur = yearsUntilRetirement(1991, "Jonas");
console.log(yur);

// *6. Functions calling other functions

function cutFruitPieces(fruit, chunks) {
  return fruit * chunks;
}
function fruitProcessor2(apples, oranges) {
  //   console.log(apples, oranges);
  let applePieces = cutFruitPieces(apples, 4);
  let orangePieces = cutFruitPieces(oranges, 8);
  return `${Math.min(
    applePieces,
    orangePieces
  )} juices made with ${applePieces} apple pieces and ${orangePieces} orange pieces`;
}

apples = Math.round(Math.random() * 10);
oranges = Math.round(Math.random() * 5);

console.log(fruitProcessor2(apples, oranges));

// *9 Introduction to Arrays
const friends = ["Michael", "Steven", "Peter"];

for (let friend of friends) console.log(friend);

console.log(friends.sort());

friends[3] = "a";

console.log(friends);
friends[6] = "a";
console.log(friends[5]);
console.log(friends);

const years = [1990, 1967, 2002, 2010, 2018];
for (let year of years) console.log(calcAge3(year));
console.log("########################################");
// *10 basic Array operations
//add
years.unshift(2001); // front
years.push(2000); //end
console.log(years.length);
console.log(years.join("---"));
//remove
years.shift(); // front
years.pop(); // end
console.log(years.length);
console.log(years.join("---"));

// indexof -> get index of value if exist else -1
// includes -> get bool by value exist

console.log(years.map(calcAge3));
console.log("########################################");

// *12 Introduction to Objects

const jonasArray = [
  "Jonas",
  "Schmedtmann",
  2037 - 1991,
  "teacher",
  ["Michael", "Peter", "Steven"],
];
jonasArray.values;
const jonas = {
  firstname: "Jonas",
  lastname: "Schmedtmann",
  age: 2037 - 1991,
  job: "teacher",
  friends: ["Michael", "Peter", "Steven"],
};

// *13 Dot vs. Bracket Notation
console.log(jonas.lastname);
console.log(jonas["lastname"]);

console.log((jonas["fullname"] = jonas.firstname + " " + jonas.lastname));
console.log(jonas.fullname);
console.log(jonas);

// let ans = prompt(
//   "What do you want about jonas ? (firstname/lastname/age/job/friends"
// );
// if (jonas[ans]) console.log(jonas[ans]);
// else console.log("do not exist");

console.log(
  `${jonas.firstname} has ${jonas.friends.length} friends, and his best friend is called ${jonas.friends[0]}`
);

// *14 Object Methods

const mike = {
  firstname: "Mike",
  lastname: "Schmedtmann",
  birthYeah: 1991,
  job: "teacher",
  friends: ["Michael", "Peter", "Steven"],
  hasDriversLicense: true,
  thatsMe: function () {
    console.log(`That's ${this.firstname}, I have ${this.age} years.`);
  },
  calcAge: function () {
    if (this.age) return this.age;
    this.age = 2037 - this.birthYeah;
    return this.age;
  },
  getSummary: function () {
    return `${this.firstname} is a ${this.calcAge()}-year old ${
      this.job
    }, and he has ${
      this.hasDriversLicense === true ? "a" : "not a"
    } driver's license`;
  },
};
mike.thatsMe();
console.log(mike.calcAge());

console.log(mike.getSummary());

// * 16. Iteration The for Loop

// console.log("Lifting weights repetition 1");
// console.log("Lifting weights repetition 2");
// console.log("Lifting weights repetition 3");
// console.log("Lifting weights repetition 4");
// console.log("Lifting weights repetition 5");
// console.log("Lifting weights repetition 6");
// console.log("Lifting weights repetition 7");
// console.log("Lifting weights repetition 8");
// console.log("Lifting weights repetition 9");
// console.log("Lifting weights repetition 10");

for (let i = 1; i <= 10; i++) console.log(`Lifting weights repetition ${i}`);

// *18. Looping Backwards and Loops in Loops

const jonas18 = [
  "Jonas",
  "Schmedtmann",
  2037 - 1991,
  "teacher",
  ["Michael", "Peter", "Steven"],
];
for (let i = jonas18.length - 1; i >= 0; i--) console.log(jonas18[i]);

for (let exercise = 1; exercise <= 4; exercise++) {
  console.log(`------------ Exercise start ${exercise} ------------`);
  for (let rep = 1; rep <= 6; rep++) console.log(`---- Rep ${rep} ----`);
}
console.log("----------------");
let repW = 0;
while (repW <= 10) {
  console.log(`---- Rep ${repW} ----`);
  repW++;
}

let dice;
while (dice !== 6) {
  dice = Math.trunc(Math.random() * 6) + 1;
  console.log("Value of dice: ", dice);
}
