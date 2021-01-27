var myArray = ['hello',45,true]
// Arrays are ordered lists of values, of any type.

myArray[1];  //45

//arrays are mutable and of variable length
myArray.push('world');
myArray.length;  //4


// add/modify at specific index
myArray[3] = 'Hello';


// add or remove ele from front or back end of array
myArray.unshift(3);  //add as first ele
someVar = myArray.shift()  //remove first ele
myArray.push(3)  //insert ele at last
someVar = myArray.pop()  //remove last ele and return it


//join all ele of an array with semicolon
var myArray0 = [32,false,'js',12,56,90];
myArray0.join(';')  //"32;false;js;12;56;90"


// get subarray slicing first arg included 2nd excluded
myArray0.slice(1,4)
console.log(myArray0)
console.log(someVar)
console.log(myArray)