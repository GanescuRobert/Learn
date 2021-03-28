"use strict";

const person1 = {
  fullname: "Mark Miller",
  weight: 78,
  height: 1.69,
  calcBMI: function () {
    this.bmi = Math.round((this.weight / this.height ** 2) * 100) / 100;
    return this.bmi;
  },
};

const person2 = {
  fullname: "John Smith",
  weight: 92,
  height: 1.95,
  calcBMI: function () {
    if (!this.bmi)
      this.bmi = Math.round((this.weight / this.height ** 2) * 100) / 100;
    return this.bmi;
  },
};
if (person1.calcBMI() < person2.calcBMI())
  [person1, person2] = [person2, person1];

console.log(
  `${person1.fullname}'s BMI (${person1.bmi}) is higher than ${person2.fullname}'s (${person2.bmi})!`
);
