//class ES6 feat , provide a more structure and cleaner way to work with objects,
  //static key ,encap,inheritance ...

  //clsss ,constructor and access modifiers
class UserOperation{
    static h=0;
    constructor (username,password){
        this.username=username;
        this.password=password;
        UserOperation.h++;
    }
    login(){
        console.log(`the logged user ${this.username}`);
        
    }
    logout(){
        console.log(`logouted `);
        
    }
    static test(){
        console.log(`that is static class var ${UserOperation.h}`);
        
    }
}
// let obj2=new UserOperation("siva","psaksd")
// let obj3=new UserOperation("siva","psaksd")
// let obj4=new UserOperation("siva","psaksd")
// obj2.login()
// obj2.logout()
// UserOperation.test()
// UserOperation.test()
// UserOperation.test()

class PaidUser extends UserOperation{
    constructor(username,password){
        super(username,password)
        this.storage=100;
    }
    feat(){
        console.log("welcome paid user");
        
    }
    get st(){
        console.log(this.storage);
        
    }
    set sta(name){
        this.storage=name;

    }

}
let paidUser1=new PaidUser("siav","dskhjdhf");
paidUser1.login()
paidUser1.sta=234;
paidUser1.st


export default PaidUser;

//   class Products{
//     #nam;//private field
//     constructor(name,price){
//         this.name=name;
//         this.price=price;
//         this.#nam="siva";
//     }
//     displayProducts(){
//         this._displayProducts();
//         console.log(`the private name : ${this.#nam}`);
//     }
//     displayProducts1(){
//         console.log(`the product name : ${this.name}`);
//         console.log(`the product price : ${this.price}`);
//     }
// }
// let obj=new Products("cycle",12000);
// let obj1=new Products("cycle2",1280);
// obj.displayProducts1();
// obj1._displayProducts();




//polymorphism
    //
//**************************************

//method overloading is not supported in javascript
// function foo(arg1) {
//     console.log(arg1);
// }
// function foo(arg1,arg2) {
//     console.log(arg1,arg2);
// }
// foo("Geeks");

//method override
// class Parant{
//     display(){
//         console.log("I am from Parant class");
//     }
// }
// class Child extends Parant{
//     display(){
//         console.log("toverride child ");
        
//     }
// }
// let obj = new Child();
// console.log(typeof(obj));
// obj.display();



function test(){
    for (let i=0;i<=3;i++){
    setTimeout(()=>{
        console.log(i);
        
    },4000)}
}
test();

