let form = document.getElementById("myForm");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    
let tbody = document.getElementById("table_body");

let tr = document.createElement("tr");

});


