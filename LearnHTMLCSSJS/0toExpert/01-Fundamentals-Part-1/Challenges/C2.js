//Data1
let winnerName;
let winnerBmi;
let losserName;
let losserBmi;

let massMark = 78;
let heightMark = 1.69;

let massJohn = 92;
let heightJohn = 1.95;

bmiMark = massMark / heightMark ** 2;
bmiJohn = massJohn / heightJohn ** 2;

if (bmiMark > bmiJohn) {
  winnerName = "Mark";
  winnerBmi = bmiMark;
  losserName = "John";
  losserBmi = bmiJohn;
} else {
  winnerName = "John";
  winnerBmi = bmiJohn;
  losserName = "Mark";
  losserBmi = bmiMark;
}

console.log(
  `${winnerName}'s BMI--> (${
    Math.round(winnerBmi * 100) / 100
  }) is higher than ${losserName}'s (${Math.round(losserBmi * 100) / 100})!`
);

//Data2
massMark = 95;
heightMark = 1.88;

massJohn = 85;
heightJohn = 1.76;

bmiMark = massMark / heightMark ** 2;
bmiJohn = massJohn / heightJohn ** 2;

if (bmiMark > bmiJohn) {
  winnerName = "Mark";
  winnerBmi = bmiMark;
  losserName = "John";
  losserBmi = bmiJohn;
} else {
  winnerName = "John";
  winnerBmi = bmiJohn;
  losserName = "Mark";
  losserBmi = bmiMark;
}

console.log(
  `${winnerName}'s BMI--> (${
    Math.round(winnerBmi * 100) / 100
  }) is higher than ${losserName}'s (${Math.round(losserBmi * 100) / 100})!`
);
