// Array methods
// let arr=["apple","banana","cherry","graphs","pappaya","pomogranate","mango","annachi"]

// console.log(arr.length);
// let c=arr.toString()  // convert string
//let d=c.split(",")    // return array
// console.log(d);

// console.log(d.join("")); // return str


// var del=arr.pop()     // return pop element
// var del=arr.push("siva") // return last len

// console.log(arr.splice(-6));  // not working -1 , -5 .. (st,end)
// console.log(arr.toSpliced(-5)); // nagative skip the enter elements remaining to slice
            //array how many elments to want 

// console.log(arr.slice(1,4));

// console.log(arr.shift());  // del start of array

// console.log(arr.unshift("siva")); //insert start of array

// console.log(arr.indexOf("apple"));


// console.log(arr.includes("apple")); // like membership act , return boolean

// ***************************************************************************
// ForEach
// ========================
//syntax
    // forEach(arrow fun , condition)
// var arr1=[2,3,5,63,3434,34,3]
// var arr2=[]
// arr1.forEach((x)=> {
//     if (20<x){
//         arr2.push(x)
//     }
// })
// console.log(arr2);
// ******************************************************************

// map
// var arr1=[2,3,5,63,3434,34,3]
// let s=arr1.map((x)=>{
//     // console.log(x%2==0 ? `${x} Even` : `${x} odd`);
//     return x*x
     
// })
// console.log(s);

// ***********************************************************************
//Filter

// var arr1=[2,3,5,63,3434,34,3]
// let s=arr1.filter((x)=>{
//     // console.log(x%2==0 ? `${x} Even` : `${x} odd`);
//     if(x%2==0){
//         return x
//     }

     
// })
// console.log(s);

//***************************************************************************************** */
//reduce

// var arr1=[2,3,5,63,3434,34,3]
// let s=arr1.reduce((x,y)=>{
//     // console.log(x%2==0 ? `${x} Even` : `${x} odd`);
//     return x+y
     
// })
// console.log(s);


// find()   first matching element only return

//findIndex()
// 1225  in even numbers to change 00 o/p 1005
let g=[89,78,576,565];
console.log(g.indexOf(89))
