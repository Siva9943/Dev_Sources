//class ES6 feat , provide a more structure and cleaner way to work with objects,
  //static key ,encap,inheritance ...

  //clsss ,constructor and access modifiers
class Products{
    #nam;//private field
    constructor(name,price){
        this.name=name;
        this.price=price;
        this.#nam="siva";
    }
    displayProducts(){
        this._displayProducts();
        console.log(`the private name : ${this.#nam}`);
    }
    displayProducts1(){
        console.log(`the product name : ${this.name}`);
        console.log(`the product price : ${this.price}`);
    }
}
let obj=new Products("cycle",12000);
let obj1=new Products("cycle2",1280);
obj.displayProducts1();
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





