"use strict";

const voters = 50;

const sleep = (milliseconds) => {
  for (let i = 0; i <= milliseconds; i++);
};

for (let voter = 1; voter <= 50; voter++) {
  console.log(`Voter number ${voter} is currently voting`);
  sleep(10e8);
  console.log(`Voter number ${voter} is finish voting`);
}
