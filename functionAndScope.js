function myFunction(thing){
    return thing.toUppercase()
}
myFunction('foo')


function myFunction(){
    return //<-semicolon automatically inserted
    {thisIsAn: 'object literal'};
}
myFunction() //undefined


// js functions are first-class objects
function myFunction(){
    // this code will be called after some seconds
}
setTimeout(myFunction,5000);


function myFunction(){
    // this code will be called every 5 seconds
}
setInterval(myFunction, 5000);



setTimeout(function(){
    // take some seconds
}, 5000);


if (true){
    var i = 5;
}
i; // = 5 - not undefined as you'd expect in a block-scoped language


// scope.
(function(){
    var temporary = 5;
    // We can access the global scope by assigning to the "global object", which
    // in a web browser is always `window`. The global object may have a
    // different name in non-browser environments such as Node.js.
    window.permanent = 10;
})();
temporary; // raises ReferenceError
permanent; // = 10


function sayHelloInFiveSeconds(name){
    var prompt = 'hello, '+ name + '!'
    function inner(){
        alert(prompt);
    }
    setTimeout(inner,5000)
}
sayHelloInFiveSeconds("Adam");