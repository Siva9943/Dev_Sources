// Destructer
// let a=["apple","banana"]
// let [x,y]=a
// console.log(x,y);
// let b={
//     name:"siva",
//     age:45,
// }
// let {name,age}=b;
// console.log(name);

// let user={
//     info:{
//         name:"siva",
//         age:34,
//     },
//     fruits:[23,54,32,67],
// }
// let {info:{name,age},fruits:[a,i,p,k]}=user
// console.log(name,age,a,i,k,p);

// Function destructuring
function Dest({name,age}){
    console.log(name,age);

    
}
Dest({name:"banu",age:90})

let g={name:"ksdfs",age:344,location:"chennai"}
let j=Object.entries(g)
console.log(j);
//Object.keys()
//Object.values()
//Object.entries()

