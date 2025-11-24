//event loop
/*
    javascript is single threaded , 
    so it uses an event loop to decide 
    what to execute next.

    micro tasks = > will be complete queue
    and next
    macro tasks => started = settimeout , setinterval

*/
//prototype  == revel the hidden object prototype

// let c={name:"siva"}
// console.log(c.__proto__);

//stack
//callbackqueue
//microtask queue

//event delegation
    //using single parent event listerner to handle events of multiple child elements
//prototype => property of constructor function
//__proto__ => actual prototype of an object

//how does Garbage collection work?
    // JS uses mark and sweep algorithm to remove unreachable objects

//currying
  // return function
  //converting the function that takes multiple arguments into a sequence of functions
//   const add =a =>b =>a+b;
//   console.log(add(6,6));
  

//Event Bubbling 
   // Buttom to top


//Event capturing
    //top to buttom

//module system


//debouncing
    // run function after stop typing


//throttling
    //run function at fixed intervals (scroll)


// let a=10;
// let b=new Number(10)
// console.log(a==b,a===b);
//     //true ,false


//strict mode

// BOM - DOM
 
// Browser POP of methods
/*
1)alert()
2)prompt()
3)confirm()

*/
//callback hell

//promise states => pending , fulfilled , rejected

//micro task =>Promises
//macro task =>setTimeout , setInterval

//False values
    // 0,"",null,undefined,NaN,false
    
//type coercion

//Array.map()


//Array.filter()


//Array.reduce()


//call() =>pass args normally
//apply =>pass args array
//bind =>return new bound function

//generator function 
    // function that pauses / resumes using yield

// CORS - Cross origin resource sharing


// console.log(true+true);

// console.log(true-false);

// console.log([1,2]+[0,1,2]);


console.log(typeof(undefined));








