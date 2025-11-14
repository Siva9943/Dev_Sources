//Let , const
//Template Literals like format Specifier
let a=90;
(function temp(n){
    console.log(`${n}`)
})(a);
let obj=[4,5,7,"fgfg"]
// for (let i=0.6; i<0.9;){
//     console.log("sdf");
//     i++;
// };
for (let b in obj){
    console.log(obj[b]);

}
let data="add"
switch(data){
    case "add":
        console.log("data1");
        break;
    case "sub":
        console.log("data2");  
        break;
    default:
        console.log("finisshs");        
}
let obj1=[4,5,7,56,454]
let obj2=[2,4,6,8,10]
obj1.map((x,y)=>console.log(x,y),obj2);

