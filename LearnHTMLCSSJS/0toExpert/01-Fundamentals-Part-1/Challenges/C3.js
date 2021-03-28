const arrSum = function (arr) {
  return arr.reduce((a, b) => a + b, 0);
};

// Data1
let Dolphins = [96, 108, 89];
let Koalas = [88, 91, 110];

let avgDolphins = arrSum(Dolphins) / Dolphins.length;
let avgKoalas = arrSum(Koalas) / Koalas.length;

console.log(avgDolphins);
console.log(avgKoalas);

if (Math.max(avgKoalas, avgDolphins) >= 100) {
  console.log("Game finish!\n");
  if (avgDolphins < avgKoalas) {
    console.log("The winner is Koalas !");
  } else if (avgDolphins > avgKoalas) {
    console.log("The winner is Dolphins !");
  } else if (avgDolphins === avgKoalas) {
    console.log("Tie game !");
  }
} else {
  console.log("Not finish yet.");
}

// Data2
Dolphins = [97, 112, 101];
Koalas = [109, 95, 123];

avgDolphins = arrSum(Dolphins) / Dolphins.length;
avgKoalas = arrSum(Koalas) / Koalas.length;

console.log(avgDolphins);
console.log(avgKoalas);

if (Math.max(avgKoalas, avgDolphins) >= 100) {
  console.log("Game finish!\n");
  if (avgDolphins < avgKoalas) {
    console.log("The winner is Koalas !");
  } else if (avgDolphins > avgKoalas) {
    console.log("The winner is Dolphins !");
  } else if (avgDolphins === avgKoalas) {
    console.log("Tie game !");
  }
} else {
  console.log("Not finish yet.");
}

// Data3
Dolphins = [97, 112, 101];
Koalas = [109, 95, 106];

avgDolphins = arrSum(Dolphins) / Dolphins.length;
avgKoalas = arrSum(Koalas) / Koalas.length;

console.log(avgDolphins);
console.log(avgKoalas);

if (Math.max(avgKoalas, avgDolphins) >= 100) {
  console.log("Game finish!\n");
  if (avgDolphins < avgKoalas) {
    console.log("The winner is Koalas !");
  } else if (avgDolphins > avgKoalas) {
    console.log("The winner is Dolphins !");
  } else if (avgDolphins === avgKoalas) {
    console.log("Tie game !");
  }
} else {
  console.log("Not finish yet.");
}
