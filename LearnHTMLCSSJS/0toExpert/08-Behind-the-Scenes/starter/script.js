'use strict';

function calcAge(birthYear) {
    const age = 2037 - birthYear;

    function printAge() {
        let output = `${firstname} are ${age}, born in ${birthYear}`;
        console.log(output);

        if (birthYear >= 1981 && birthYear <= 1996) {
            var millenial = true;
            const firstname = 'Steven';
            const str = `Oh, and you're a millenial,${firstname}`;
            console.log(str);

            function add(a, b) {
                return a + b;
            }
            output = "NEW OUTPUT!";
        }
        // console.log(str);
        console.log(millenial);
        // console.log(add(2, 3));
        console.log(output);
    }
    printAge();
    return age;
}

const firstname = "Jonas";
calcAge(1991);

//Variables
// console.log(me);
// console.log(job);
// console.log(year);
// var me = 'Jonas';
let job = 'teacher';
const year = 1991;



//Functions

console.log(addDecl(2, 3));
// console.log(addExpr(2, 3));
// console.log(addArrow(2, 3));

function addDecl(a, b) {
    return a + b;
}

// var addExpr = function addExpr(a, b) {
//         return a + b;
//     }
// var addArrow = (a, b) => {
//     return a + b;
// }

if (!numProducts) deleteShoppingCart();
var numProducts = 10;

function deleteShoppingCart() {
    console.log('All products deleted!');
}

let y = 2;
const z = 3;



console.log(this);

const calcAge1 = function(birthYear) {
    console.log(2037 - birthYear);
    console.log(this);
}

calcAge1(1991);

const calcAge2 = (birthYear) => {
    console.log(2037 - birthYear);
    console.log(this);
}

calcAge2(1991);

// const jonas = {
//     year: 1991,
//     calcAge: function() {
//         console.log(this);
//         console.log(2037 - this.year);
//     },
// };
// 
// jonas.calcAge();

// const matilda = {
//     year: 2017,
// };

// matilda.calcAge = jonas.calcAge;
// matilda.calcAge();

// const f = {};
// f.year = 2010;
// f.calcAge = jonas.calcAge;
// f.calcAge();

var firstName = 'Matilda';

const jonas = {
    firstName: 'Jonas',
    year: 1991,
    calcAge: function() {
        // console.log(this);
        console.log(2037 - this.year);
        // ! Solution 1
        const self = this;
        const isMillenial1 = function() {
            // console.log(this);
            // console.log(this.year >= 1981 && this.year <= 1996);
            console.log(self);
            console.log(self.year >= 1981 && self.year <= 1996);
        };
        // ! Solution 2
        const isMillenial2 = () => {
            console.log(this);
            console.log(this.year >= 1981 && this.year <= 1996);
        }
        isMillenial1();
        isMillenial2();
    },
    // greet: () => {
    //     console.log(`Hey ${this.firstName}`)
    // },
    greet: function() {
        console.log(this);
        console.log(`Hey ${this.firstName}`)
    }
};
jonas.greet();
jonas.calcAge();



const addExpr = function addExpr(a, b) {
    console.log(arguments);
    return a + b;
}
addExpr(2, 5);
addExpr(2, 5, 8, 12);
var addArrow = (a, b) => {
    // console.log(arguments);
    return a + b;
};

addArrow(2, 5);
// addArrow(2, 5, 8, 12);


let age = 30;
let oldAge = age;
age = 31;
console.log(age);
console.log(oldAge);

const me = {
    name: 'Jonas',
    age: '30',
};
const friend = me;
friend.age = 27;

console.log('Friend: ', friend);
console.log('Me: ', me);


// Primitive types
let lastName = 'Williams';
let oldLastName = lastName;
lastName = 'Davis';
console.log(lastName, oldLastName);


// Reference types
const jessica = {
    firstName: 'Jessica',
    lastName: 'Williams',
    age: 27,
};

const marriedJessica = jessica;
marriedJessica.lastName = 'Davis';

console.log('Before marriage: ', jessica);
console.log('After marriage: ', marriedJessica);

const jessica2 = {
    firstName: 'Jessica',
    lastName: 'Williams',
    age: 27,
    family: ['Alice', 'Bob'],
};

const marriedJessica2 = Object.assign({}, jessica2);
marriedJessica2.lastName = 'Davis';

const CopyJessica2 = JSON.parse(JSON.stringify(jessica2));
CopyJessica2.lastName = 'Davis';
jessica2.family.push('Marry');
jessica2.family.push('John');

console.log('Before marriage: ', jessica2);
console.log('After marriage: ', marriedJessica2);
console.log('After marriage: ', CopyJessica2);