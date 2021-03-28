let js = "amazing";
if (js == "amazing")
  //alert("JS is FUN");

  console.log(1 + 2 + 3 + 4);

let firstname = "Jonas";

console.log(firstname);
console.log(firstname);
console.log(firstname);
console.log(firstname);

const now = 2037;
const ageJonas = now - 1991;
const ageSarah = now - 2018;
console.log(ageJonas * 2, ageSarah / 10, 2 ** 3);

const firstName = "jonas";
const lastName = "schmedtmann";
console.log(firstName + " " + lastName);

let x = 10 + 5;
x += 10;
x *= 4;
x++;
++x;
console.log(x);

console.log(ageJonas > ageSarah);

const isFullAge = ageSarah >= 18;

console.log(now - 1991 >= now - 2018);
let y;
x = y = 1 + 2;
console.log(x, y);

const averageAge = (ageJonas + ageSarah) / 2;
console.log(averageAge);

//type conversion
const inputYear = "1991";
console.log(Number(inputYear), inputYear);
console.log(Number(inputYear) + 18);
console.log(Number("Jonas"));
console.log(typeof NaN);

console.log(String(23), 23);

//type coercion
console.log("I m " + 23 + " years old");
console.log("23" - "10" - 3);
console.log("23" / "2");
console.log("23" > "18");

let n = "1" + 1;
n--;
console.log(n);

// 5 falsy values: 0, '', undefined, null, NaN
console.log(Boolean(0));
console.log(Boolean(""));
console.log(Boolean(undefined));
console.log(Boolean({ a: 2 }));

const money = 100;

if (money) {
  console.log("Don't spend it all");
} else console.log("You should get a job");

let height = 0;

if (height) {
  console.log("Yay!");
} else {
  console.log("Height is Undefined");
}

const favourite = 23; // = Number(prompt("What's your favourite number ?"));

console.log(favourite);
console.log(typeof favourite);

if (favourite === 23) {
  console.log(23);
} else if (favourite === 7) {
  console.log(7);
} else if (favourite === 9) {
  console.log(9);
} else console.log("Not lucky");

if (favourite !== 23) {
  console.log("why not 23 ?");
}

// OPERATORS
const hasDriversLicense = true; //A
const hasGoodVision = true; //B
console.log(hasDriversLicense && hasGoodVision);
console.log(hasDriversLicense || hasGoodVision);
console.log(!hasDriversLicense && hasGoodVision);
console.log(!hasDriversLicense || hasGoodVision);
console.log(!hasDriversLicense && !hasGoodVision);
console.log(!hasDriversLicense || !hasGoodVision);

const shouldDrive = hasDriversLicense && hasGoodVision;
if (shouldDrive) {
  console.log("Able to drive");
} else {
  console.log("Not able to drive");
}

// SWITCH
const day = "Tuesday";

switch (day) {
  case "Monday":
    console.log("Plan 1 course structure");
    break;
  case "Tuesday":
  case "Wednesday":
    console.log("Plan 3 course structure");
    break;
  case "Thursday":
  case "Friday":
    console.log("Plan 5 course structure");
    break;
  case "Saturday":
  case "Sunday":
    console.log("Plan 7 course structure");
    break;
  default:
    console.log("Not a valid day");
}
