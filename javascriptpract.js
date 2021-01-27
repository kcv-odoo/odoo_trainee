//console.log to print data on console 
console.log('hi there ')
//var let direct assignment to declare variable 
var abc = 5;
let xyz = 10
pqr = 15
console.log(abc,xyz,pqr);
console.log(typeof(xyz))
//variable in js are dynamic type
xyz = "name"
console.log(typeof(xyz))
//array are ordered list of any type
let marray = [1,"hi",2]
console.log(marray)
//shift and unshift for removing and adding ele at begining
marray.unshift(5)
console.log(marray)
marray.shift() //for remove first ele
marray.push(23) //add at end
marray.pop() //remove from end

function myFunction()
{ 
     document.getElementById("demo").innerHTML = "paragraph changed"

}
