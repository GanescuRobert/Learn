// Remember, we're gonna use strict mode in all scripts now!
"use strict";

const x = 23;
const calcAge = birthYear => 2037 - birthYear;
console.log(calcAge(1991));

let ans = "asd asdasdwq asdq saczx q".split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');

console.log(ans);

// return masked string
function maskify(cc) {
    return cc.length > 4 ? "#".repeat(cc.length - 4) + cc.slice(-4) : cc;
}

console.log(maskify("4556364607935616"));

function digital_root(n) {
    while (n.length != 1) {
        console.log(n);
        let numbers = n.split('');
        n = String(numbers.reduce((a, b) => parseInt(a) + parseInt(b), 0));
    }
    return n;
}

console.log(digital_root("493193"));

function friend(friends) {
    let ans2 = [];
    for (let myfriend of friends) {
        console.log(myfriend);
        if (myfriend.length == 4)
            ans2.push(myfriend);
    }
    return ans2;
}

console.log(friend(["Ryan", "Kieran", "Jason", "Yous"]));

function longest(s1, s2) {
    return Array.from(new Set(s1 + s2)).sort().join('');

}
console.log(longest("aretheyhere", "yestheyarehere"));

function spinWords(words) {
    let ans = "";
    for (const word of words.split(" ")) {

        ans +=
            word.length >= 5 ?
            word.split('').reverse().join('') :
            word;
        ans += " ";

    }
    return ans.slice(0, -1);
}


console.log(spinWords("Hey fellow warriors"));

function likes(names) {
    switch (names.length) {
        case 0:
            console.log("no one likes this");
            break;
        case 1:
            console.log(`${names[0]} likes this`);
            break;
        case 2:
            console.log(`${names[0]} and ${names[1]} like this`);
            break;
        case 3:
            console.log(`${names[0]}, ${names[1]} and ${names[2]} like this`);
            break;
        default:
            console.log(`${names[0]}, ${names[0]} and ${names.length-2} othrs like this`);
    }
}

console.log(likes(['Alex', 'Jacob', 'Mark', 'Max']));

var uniqueInOrder = function(iterable) {
    ans = []
    for (let i = 1; i <= iterable.length; i++) {
        if (iterable[i - 1] !== iterable[i])
            ans.push(iterable[i - 1]);
    }
    ans.push(iterable[-1]);
    if (ans[-1] !== iterable[-2])
        ans.pop();
    return ans;

}

console.log(uniqueInOrder('AAAABBBCCDAABBB'));

function digPow(n, p) {
    let ns = String(n).split('');
    let numbers = [];
    for (const i of ns) {
        numbers.push(Number(i));
    }

    for (let i = 0; i < numbers.length; i++) {
        numbers[i] = Math.pow(numbers[i], p++);
    }
    let sol = numbers.reduce((a, b) => a + b, 0);
    if (sol % n === 0)
        return sol / n;
    else
        return -1;
}

console.log(digPow(89, 1));

function rot13(message) {
    let chs = message.split('');

    for (let indx in chs) {
        if (("a".charCodeAt(0) <= chs[indx].charCodeAt(0) && chs[indx].charCodeAt(0) <= "z".charCodeAt(0)) || ("A".charCodeAt(0) <= chs[indx].charCodeAt(0) && chs[indx].charCodeAt(0) <= "Z".charCodeAt(0))) {
            let pos = (chs[indx].charCodeAt(0)) + 13;
            if (pos > "Z".charCodeAt(0) && pos <= "g".charCodeAt(0))
                pos = pos - "Z".charCodeAt(0) + "A".charCodeAt(0) - 1;

            if ("z".charCodeAt(0) < pos)
                pos = pos - "z".charCodeAt(0) + "a".charCodeAt(0) - 1;
            chs[indx] = String.fromCharCode(pos);


        }
    }
    return chs.join('');
}
console.log(rot13("x3Z"));

console.log("####----####");
// const temperatures = [3, -2, -6, -1, 9, 'error', 13, 17, 15, 14, 9, 5];
const temperatures = [3, 2, 6, 1, 9, 13, 17, 15, 14, 9, 5];

const minValue = function(temps) {
    // let min = temps[0];
    let min = 0;
    for (const t of temps) {
        if (min > t)
            min = t;
    }
    return min;
};
const maxValue = function(temps) {
    // let max = temps[0];
    let max = 0;
    for (const t of temps) {
        if (max < t)
            max = t;
    }
    return max;
};

const calcTempAmplitude = function(temps) {
    let min = minValue(temps);
    let max = maxValue(temps);
    //return Math.abs(max) - Math.abs(min);
    return max - min;
};

const calcTempAmplitude2 = function(temps1, temps2) {
    let temps = Array.prototype.concat(temps1, temps2);
    console.log(temps, temps1, temps2);
    return calcTempAmplitude(temps);
}

console.log(calcTempAmplitude2(temperatures.slice(0, temperatures.length / 2), temperatures.slice(temperatures.length / 2)));


const measureKelvin = function() {
    const measurement = {
        type: 'temp',
        unit: 'celsius',
        // value: Number(prompt('Degrees celsius:')),
        value: 10,
    };
    const kelvin = measurement.value + 273;

    return kelvin;
};

console.log(measureKelvin());