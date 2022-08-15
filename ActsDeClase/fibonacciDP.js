var f = [];
f[0] = 1;
f[1] = 1;

function fibonacciDP(n){
    for(var i=2; i<=n; i++){
        f[i] = f[i-1] + f[i-2];
    }
    return f[n];
}

//testing
console.log(fibonacciDP(10));
console.log(fibonacciDP(1000));
console.log(fibonacciDP(2000));