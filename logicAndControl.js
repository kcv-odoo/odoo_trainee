var count = 1
if (count==3){
    // if count 3
} else if(count==4){
    // evaluated if count is 4
} else{
    // evaluated if its neither 3 and 4
}


// while loop
while(true) {
    // an infinite loop
}


// do-while loop ,they always runs at least one
var input;
do{
    input=getInput();
}while(!isValid(input))



// for loop
outer:
for(var i=0;i<10;i++){
    for(var j=0;j<10;j++){
        if(i==5&&j==5){
            break outer;
            // breaks out of outer loop instead of only the inner one
        }
    }
}


// for-in allows you to iteration over properties/values of an obj
var description = ''
var person = {fname:'Kamlesh',lname:'pathekar',age:21}
for(var x in person){
    description += person[x]+'';
} //description = 'paul ken 18
console.log(description)



// The for/of statement allows iteration over iterable objects (including the built-in String, 
// Array, e.g. the Array-like arguments or NodeList objects, TypedArray, Map and Set, 
// and user-defined iterables).
var myPets = "";
var pets = ["cat", "dog", "hamster", "hedgehog"];
for (var pet of pets){
    myPets += pet + " ";
} // myPets = 'cat dog hamster hedgehog 


// && is logical and, || is logical or
if(house.size=='big' && house.colour=='blue'){
    house.contains = 'bear';
}
if(colour=='red'||colour=='blue'){
    // colour is either red or blue
}


// && and || "short circuit", which is useful for setting default values.
var name = otherName || "default";


// The `switch` statement checks for equality with `===`.
// Use 'break' after each case
// or the cases after the correct one will be executed too.
grade = 2;
switch (grade) {
  case 1:
    console.log("Great job");
    break;
  case 2:
    console.log("OK job");
    break;
  case 3:
    console.log("You can do better");
    break;
  default:
    console.log("Oy vey");
    break;
}