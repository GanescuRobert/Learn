'use strict';

const printForecast = function(arr) {
    for (const indx in arr) {
        console.log(`... ${arr[indx]}C in ${indx+1} days ...\n`);
    }
}
let temperatures1 = [17, 21, 23];
let temperatures2 = [12, 5, -5, 0, 4];
printForecast(temperatures2);