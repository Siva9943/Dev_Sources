//callback function
// function greet(callback){
//     console.log("helos")
//     console.log(callback)
//     callback()

// }
// let g=greet(()=>console.log("hello"))

// async and await with promises
//async => makes a function return a promise
//await => makes an async function wait for a promise

async function dog_Promise(){
    return new Promise((res,rej)=>{
        setTimeout(()=>{
            const dog=true;
            if (dog){
                res("dog is walking")
            }
            else{
                rej("you aj")
            }
        },(1500))
    })
}
async function dog_Promise2(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            let dog1=true;
            if (dog1){
                resolve("You can walk the dog")
            }
            else{
                reject("you aj")
            }
        },(1500))
    })
}
async function dog_Promise3(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            const dog2=true;
            if (dog2){
                resolve("You can walk the dog")
            }
            else{
                reject("you aj")
            }
        },(1500))
    })
}

async function sampleTest(){
    try{

        // const result2 = await dog_Promise2();
        // console.log(result2);
      
        // const result3 = await dog_Promise3();
        // console.log(result3)

        const result = await dog_Promise();
        
        console.log(result);

    }
    catch(error){
        console.error(error);
    }
    
}
sampleTest()

// setTimeout

// console.log("heii siva");

// let c=setTimeout(function sampe(){
//     let a=7,b=9;
//     console.log("Settimeout");
    
// },4000);

// clearTimeout(c)

// setInterval
// let h=setInterval(()=>{
//     console.log("hii siva \n")
// },3000); 
// if (h==1){
//     clearInterval(h)
// }

//Arrow fun
// let g=()=> {
//     return console.log("hello siva");

// }
// g()
// var n=8,m=90;
// function sum_Of(n,m){
//     let i=(n,m) => {
//         return n+m
//     }
//     let f=i(n,m);
//     return f
// }
// console.log(sum_Of(n,m))
// Closures
// -------------------
 // parent function variables can be accessed by inner function
 //==================================================================
//Cosure is the combination of a function and the lexical environment within which that function was declared.
//  This means that an inner function retains access to the variables and parameters of its outer (enclosing) function, even after the outer function has finished executing. 

// var a = 4;
// function myFunction() {
//     a=90
//   return a * a;
// }
// console.log(myFunction());
// console.log(a);

// Initiate counter
// let counter = 0;

// function add() {
//   let counter = 0;
//   counter += 1;
//   return counter;
// }

// console.log(counter);

// console.log(add());
// console.log(add());
// console.log(add());
// console.log(counter);

//Higher order function
// function greet(name){
    
//     return function(message){    
//         console.log(`Hello ${name}, ${message}`)
//     }
// }
// greet("siva");
// greetMessage("Welcome to brocode")
// let g=greet("siva")("logged in successfully")
// console.log(g);

// function calculate(operation){
//     return function(a,b){
//         if (operation==="add"){
//             return a+b
//         }
//         else if (operation==="subtract"){
//             return a-b
//         }
//         else if (operation==="multiply"){
//             return a*b
//         }
//         else if (operation==="divide"){
//             return a/b
//         }
//         else{
//             return "invalid operation"
//         }
//     }
// }
// let add=calculate("add");
// console.log(add(5,3));
// let subtract=calculate("subtract");
// console.log(subtract(5,3));
// let multiply=calculate("multiply");
// console.log(multiply(5,3));
// let divide=calculate("divide");
// console.log(divide(5,3));



function outer(){
    let count =0;
    return function inner(){
        count++;
        return count;

    };

}
const counter = outer();
console.log(counter)
console.log(counter());

