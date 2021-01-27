//JavaScript's objects are equivalent to "dictionaries" or "maps" in other
// languages: an unordered collection of key-value pairs.

var myObj = {key1: "Hello", key2: "World"};

// keys are string and values can be ant type
var myObj = {mykey:'myvalue','my other key':4}

// accessing data using keys
console.log(myObj['my other key'])  //4


//using dot syntax
console.log(myObj.mykey);  //myvalue

// Objects are mutable; values can be changed and new keys added.
myObj.myThirdKey = true;

// If you try to access a value that's not yet set, you'll get undefined.
console.log(myObj.myFourthKey); // = undefined
console.log(myObj)