/* 
return Array
Object.keys(var)
Object.values(var) =>[v,v,v,v]
object.entries(var)  => [[k,v],[k,v]]
Object.assign(targetvar,value)
Object.freeze(var) => stop modifications
Object.seal(var) => next , prevent stop add,remove 
                update only
                ex obj.a=5
                    obj.a=10


*/
// set Object
// let a=[1,2,34,5,6,7,565,6454,4]
// let myset= new Set();
// myset.add(2);
// myset.add({name:"siva"})
// myset.add(a);
// myset.delete(3)
// // myset.delete(5)
// console.log(myset.size);

// let arr=Array.from(myset)
// console.log(arr);

// set methods
// add()
//delete()
//has(value) like includes()
//clear()
//size like length

//map object
//  key - value paires
// a key in the Map may only occur once

let my_map=new Map();
my_map.set("a",1)
my_map.set("a",2)

my_map.set("b",2)
my_map.set("c",2)
my_map.set("d",2)
my_map.set("e",2)
console.log(my_map);
console.log(my_map.has("a"));

// for (i of my_map){
//     console.log(i);
    
// }  //separate array key-value

// for (i of my_map.keys()){
//     console.log(i);
    
// }  //separate key

// for (i of my_map.values()){
//     console.log(i);
    
// }

// for ([k,v] of my_map){
//     console.log(k,v);
    
// } //destucturing

// let my_map1={name:"siva"}
// for (i of my_map1){
//     console.log(i);
// }
//map convert array only 2D array
// let arr=[[7,8],[8,9]]
// let f=new Map(arr); //not support Map.from() must new reference object needed.
// console.log(f);


//for in   us   for of

//for in ==> spealist in object
     // using string,array will be return index
// for of  ==> used for array,string,map,set
    // iterate the values

import P from "./OOPS"
let p =new P("name","hkjhj");
p.login()
P.set
