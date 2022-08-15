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
//Ejecuciones
console.log(factorialDP(10));
console.log(factorialRecursivo(10));