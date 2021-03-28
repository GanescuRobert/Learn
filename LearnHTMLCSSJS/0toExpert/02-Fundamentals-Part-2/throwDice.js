"use strict";

let counter = new Array(6).fill(0);

console.log(counter);

for (let i = 1; i <= 10e5; i++) {
  let diceValue = Math.trunc(Math.random() * 6) + 1;
  counter[diceValue - 1]++;
}

let n = counter.length;

let mean = 10e5 / n;

let sum = 0;
for (let c of counter) sum = (c - mean) ** 2;
let variance = sum / n - 1;
let std = Math.sqrt(variance);

console.log(counter, mean, variance, std);
