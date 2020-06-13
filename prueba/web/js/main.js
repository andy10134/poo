function CalcularIMC() {
    var peso = document.querySelector("input[name='peso']").value;
    var altura = document.querySelector("input[name='altura']").value;

    eel.calculoICM(peso, altura)((ret) => {
        document.querySelector(".value").innerHTML = ret[0] + " Kg/m2";
        document.querySelector(".peso").innerHTML = ret[1];

        document.querySelector(".alert").style.visibility = "inherit";
        if(ret[0] <= 18.5){
            document.querySelector(".alert").className = "alert alert-secondary";
        }
        else if(ret[0] <= 24.9){
            document.querySelector(".alert").className = "alert alert-success";
        }
        else if(ret[0] < 29.9){
            document.querySelector(".alert").className = "alert alert-warning";
        }
        else{
            document.querySelector(".alert").className = "alert alert-danger";
        }
    })
}

function limpiar() {
    document.querySelector("input[name='peso']").value = "";
    document.querySelector("input[name='altura']").value = "";
    document.querySelector(".alert").style.visibility = "hidden";
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelector(".alert").style.visibility = "hidden";
})