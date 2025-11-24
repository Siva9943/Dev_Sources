/* syntax
try{
}
catch(err){
}
finally{
}
*/
try{
    let r=10/0;
    console.log(r);
}
catch(err){
    throw new Error("error",err)
}
finally{
    console.log("welcome siva");
    
}

async function APiTest() {
    try{
        let responce=await fetch(`https://api.freeapi.app/api/v1/public/quotes/quote/random`)
        
            if(!responce.ok){
                throw new Error("Network error");
            }
            let data=await responce.json();
            return data;
    }
    catch(err){
        console.log(err);
    }
}
async function testRun() {
    let data=await APiTest();
    console.log(data.data.get("author"));
}
testRun()
