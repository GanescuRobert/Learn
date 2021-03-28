"use strict";

const calcTip = (value) => {
  return (value >= 50 && value <= 300 ? 0.15 : 0.2) * value;
};
// let value = 100;
// let tip = calcTip(value);
// console.log(tip);

let bills = [125, 555, 44];
let tips = bills.map(calcTip);
let totals = [];
for (const i of Array(bills.length).keys()) totals[i] = bills[i] + tips[i];

console.log(totals);
