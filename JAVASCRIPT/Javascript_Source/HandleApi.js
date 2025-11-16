
// async function apiCall() {
//     try{
//         let response=await fetch("https://api.freeapi.app/api/v1/public/quotes/quote/random",{method: 'GET', headers: {accept: 'application/json'}});
//         if (!response.ok){
//             throw new Error("HTTP error "+response.status);
//         }
//         let data=await response.json();
//         return data;
//     }
//     catch(err){
//         console.log("Error caught",err);
//     }
    
// }
// async function get_api(){
//     let head=document.getElementsByClassName("name");
    
//     let result=await apiCall();
//     console.log(result);
//     head[0].textContent=result.data.id;
//     head[0].style="background-color: yellow; color:blue; padding: 20px;";

//     head[1].textContent=result.data.author;
//     head[1].style="background-color: yellow; color:blue; padding: 20px;";

//     head[2].textContent=result.data.content;
//     head[2].style="background-color: yellow; color:blue; padding: 20px;";


// }
// setInterval(get_api, 2000);
