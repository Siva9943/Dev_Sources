// id
let p1=document.getElementById("p1");
// p1.textContent="siva"
// p1.innerText="siva"
// p1.innerHTML=`<h1>Siva</h1>`
// p1.style="color:red;background:yellow;"

// note the getid only target in single element
//class
// let p1=document.getElementsByClassName("class");
// console.log(typeof(p1));

// p1[0].textContent="siva"
// p1[1].textContent="prakash"

// let p2=document.getElementsByTagName("p");
// p2[0].textContent="hello world"

// --------querySelector--------
// let p=document.querySelector("#p1");
// p.textContent="siva";
 //--------querySelectorAll---------
// let p=document.querySelectorAll("#p1");
// p[0].textContent="siva";
// p[1].textContent="siva";

// create Elemtents

let c=document.createElement("div");
let parent=document.getElementById("fetchData");
parent.appendChild(c);
// c.style="width:100px;height:100px;border:2px solid black;background-color:blue;";
// parent.style="width:100%;display:flex;justify-content:center";


// remove Element

// parent.removeChild(c)


// setAttribute(att,value)
let img=document.createElement("a");
parent.appendChild(img);
img.textContent="hello siva"
img.setAttribute("href","www.youtube.com")
img.setAttribute("id","test")


// getAttribute

// console.log(img.getAttribute("test"))

// ------addeventListener ----------------
            // click
// let btn=document.getElementById("click");
// btn.addEventListener("click",function(){
//     alert("hello siva why are click in this btn")
// })
            // mouseover
// let btn=document.getElementById("click");
// btn.addEventListener("mouseover",function(){
//     alert("hello siva why are click in this btn")
// })

        //mouseOut
// let btn=document.getElementById("click");
// btn.addEventListener("mouseout",function(){
//     alert("hello siva why are click in this btn")
// })

        //keyup event
    
// let btn=document.getElementById("click");
// btn.addEventListener("keydown",function(){
//     console.log("hello siva why are click in this btn")
// })

        //input event

// let input=document.getElementById("input");
// input.addEventListener("input",()=>{
//     p1.textContent=input.value;
// })

// let input=document.getElementById("input");
// input.addEventListener("change",()=>{
//     p1.textContent=input.value;
// })

// let input=document.getElementById("input");
// input.addEventListener("focus",()=>{
//     p1.textContent="eyuue";
// })

        //double click ---dblclick

// let btn=document.getElementById("click");
// btn.addEventListener("dblclick",function(){
//     alert("hello siva why are click in this btn")
// })


// input
    // blur , submit ,focus
//   mobile Events
    /* 
     touchstart
     touchend
     touchmove
     touchcancel
     */

// windows
/*
    load
    scroll
    resize
    unload
    DOMContentLoaded
*/
// media Events
// play,pause,ended,volumechange

// window.addEventListener("load",()=>{
//     p1.innerText="Loading.....";
//     p1.style="font-size:50px;color:black;"
//     setTimeout(()=>{
//         p1.innerText="welcome siva";
//         p1.style="color:blue;font-size:40px;bakground-color:gray;"
//     },5000)
// })

let obj={name:"siva",
    age:21,
    address:"chennai",
    lang:["tamil","english"],
}
let {name:n,age,lang:[x,y]}=obj;
console.log(y);



























// import axios from 'axios';

// axios.get('http://127.0.0.1:8000/get_emp')
// .then(responce =>{
//     const resData=responce.data;
//     console.log(resData);
    
// })
// .catch(error =>{
//     console.log(error);
    
// })


let dom=document.getElementById("api");

// fetch - Function used for making HTTP request to fetch resources.
//     (JSON style data , images, files)
//      simplifies asynchrorounous data fetching in js
//      used for interacting with API"S to retrive and send
//      data asynchrously over the web
    //      fetch(url,{options})  => fetch(url,{method:"POST/GET/PUT/DELETE/PATCH"})  default GET
// fetch('http://127.0.0.1:8000/get_emp')
// .then((res)=>{
//     if (!res.ok){
//         throw new Error("API fetch not responce");
//     }
//     else {
//         return res.json()
//     }
// })
// .then((data)=> {
//     console.log(data.data[0].Firstname);
// })
// .catch(error =>{
//     console.log(error);
// })

// fetchData();
// async function fetchData() {
//     let dom=document.getElementById("fetchData");
//     let head=document.createElement("h1");
//     try {
//         const res = await fetch(`http://127.0.0.1:8000/get_emp`);
        
//         if (!res.ok) {
//             throw new Error("API request failed");
//         }
//         const data = await res.json();
//         console.log(data);
//         let ul=document.createElement("ul");
//         for (emp in data.data){
//             console.log(emp);
            
//         }
//         (emp => {
//             let li=document.createElement("li");
//             li.textContent=`${emp.data[0].Firstname} ${emp.Lastname} - ${emp.Email}`;
//             ul.appendChild(li);
//         }
//         );
//         dom.appendChild(ul);
//         head.textContent="Employee List";
//         dom.appendChild(head);
        

//     } catch (err) {
//         const error = document.createElement("h1");
//         document.getElementById("fetchData").appendChild(error);
//         error.textContent = `Error: ${err.message}`;
//     }
// }


