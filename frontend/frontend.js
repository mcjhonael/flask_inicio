BASE_URL="http://127.0.0.1:5000/"
let formulario=document.getElementById("formulario");
let nombre=document.getElementById("nombre");
let apellido=document.getElementById("apellido");
let edad=document.getElementById("edad");

const postProductos=async()=>{
    const response=await fetch(`${BASE_URL}/productos`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            nombre:nombre.value,
            apellido:apellido.value,
            edad:+edad.value
        })
    })
    const json=await response.json()
    return json;
}

formulario.onsubmit=(e)=>{
    e.preventDefault()

    // let objProducto={
    //     nombre:"",
    //     apellido:"",
    //     edad:0
    // }
    // objProducto["nombre"] = nombre.value
    // objProducto["apellido"] = apellido.value
    // objProducto["edad"] = edad.value

    // console.log(objProducto);
    postProductos().then((res)=>{
        console.log(res);
    })
    
}