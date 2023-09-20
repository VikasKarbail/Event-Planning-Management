function togleform(event){
    let id = event.target.getAttribute("data-value");
    console.log(id);
     let items=["Signin","Signup"];
     for(let i=0;i<items.length;i++){
        if(id==items[i]){
           document.getElementById(items[i]).style.display="block";
          
        }
        else{
            document.getElementById(items[i]).style.display="none";

        }

 }
}