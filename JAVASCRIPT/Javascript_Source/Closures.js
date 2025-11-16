
//Closures - the outer function ,return the inner fun , to remain or build the outer fun variables and arguments to use inner funtion

// function parant(){
//     let count=0;
//     return ()=>{
//         count+=1;
//         console.log(count);
//     }
// }
// let p=parant();
// p();
// p();
// p();

// map
// let arr=[34,334,34,3];
// let res=arr.map(x=>x*5)
// console.log(res);

//forEach

// let arr=[34,334,34,3];
// let app=[];
// let res=arr.forEach(x=>{
//     app.unshift(x*3);

// }
// )
// console.log(app);

//filter

// let arr=[34,334,34,3];
// let res=arr.filter(x=>x<100)
// console.log(res);

//reduce

// let arr=[34,334,34,3];
// let res=arr.reduce((x,y,z,h)=>{
//     console.log("index",z);
//     console.log("full",h);
//     return x+y
    
//     })
// console.log(res);
// reduce((acc,curr)=>{acc+curr},initialValue)
    // acc=> accumulator 
    // curr => current item
    //initial value


let arr=[
    ["a","b","c"],
    ["c","d","f"],
    ["d","f","g"],
];
let res=arr.flat().reduce((acc,curVal)=>{
    
    if(acc[curVal]){
        acc[curVal]++;
    }
    else{
        acc[curVal]=1;
    }
    return acc
    
},{});
console.log(res);
