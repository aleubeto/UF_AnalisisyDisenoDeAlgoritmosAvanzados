//Versión iterativa
function factorialDP(n){
    var fac = 1;
    for(var i=n; i>0; i--){
        fac *= i;
    }
    return fac;
}

//Versión recursiva
function factorialRecursivo(n){
    if(n<=1)
        return 1;
    if(n == 2)
        return 2;
    return n*factorialRecursivo(n-1);
}

//Versión iterativa con arreglos de Óscar y Rocha
var f = [];
f[0] = 1;

const factorial_arreglos = (n) => {
    for(let i=1; i<=n; i++){
        f[i] = i * f[i-1];
    }
    return f[n];
}

//Ejecuciones
console.log(factorialDP(10));
console.log(factorialRecursivo(01));
console.log(factorial_arreglos(10));