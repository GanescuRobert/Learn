"use strict";

const calcTip = (value) => {
  return (value >= 50 && value <= 300 ? 0.15 : 0.2) * value;
};

const bills = [22, 295, 176, 440, 37, 105, 10, 1100, 86, 52];
let tips = bills.map(calcTip);
let totals = [];
for (let i = 0; i < bills.length; i++) totals.push(bills[i] + tips[i]);

console.log(bills, tips, totals);

console.log(totals.reduce((a, b) => a + b, 0) / totals.length);
