let name = "Billy";
// Variables defined with let can be reassigned new values.
name = "William";



const pi = 3.14;
pi = 4.13; // You cannot do this.


const isEven = (number) => {
    return number % 2 === 0;
};
isEven(7); // false


// I put the word "equivalent" in double quotes because a function defined
// using the lambda syntax cannnot be called before the definition.
// The following is an example of invalid usage:

add(1, 8);

const add = (firstNumber, secondNumber) => {
    return firstNumber + secondNumber;
};