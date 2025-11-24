const eventname=new Event("event");
const eventWithData=new CustomEvent("eventWithData",
    {
        detail:{
            name:"siva",
        }
    });


// Advance 
//Clousure = > is a funtion that retain acess to its outer fun variable,even after the outer function has finished executing .
//a  function that remmebers/ keeps access to its outer functions variable even after the outer function has finished execting.
//

function outer(num){
    let count=0;
    function inner(name){
        count++;
        console.log(`the value of count is ${count}`);
        console.log(`the name is ${name}`);
        console.log(`the num of outer fun ${num}`);
    }
    return inner
}
let closure=outer(60);
closure("siva");
closure("aji");
closure("banu");

// Higher order function
/* 
a function that takes another function as argument Or return a function

takes another function as an argument
    return another function as its result
    more reusablity
     map
     filter
     reduce


*/

//Call back function
/*
a function passed as an argument to another funtion and executed later
function name pass a parameter to executer later 

*/
