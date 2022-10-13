
//    tsc filename.ts
//    node filename.js

function coloring(tamano, graph) {
    let mapa = new Map();

    for (let i = 0; i < tamano; i++){
        mapa.set(graph[i], -1)
    }

    for (let i = 0; i < tamano; i++){
        for (let j = 0; j < tamano; j++){
            if (graph[i][j] == 1){
                if (mapa.get(graph[j]) == mapa.get(graph[i])){
                    mapa.set(graph[i], (Math.max(mapa.get(graph[i]), mapa.get(graph[j])) + 1))
                    j = 0
                } 
            }
        }
    }

    for (let i = 0; i < tamano; i++){
        mapa.set(graph[i], 0)
        for (let j = 0; j < tamano; j++){
            if (graph[i][j] == 1){
                if (mapa.get(graph[j]) == mapa.get(graph[i])){
                    mapa.set(graph[i], (Math.max(mapa.get(graph[i]), mapa.get(graph[j])) + 1))
                    j = 0
                } 
            }
        }
    }

    for (let i = 0; i < tamano; i++){
        console.log("Node: " + (i+1) + " , Assigned Color: " + mapa.get(graph[i]))
    }
    console.log("\n")
}

let tamano1  = 5;
let graph1 = [
    [0,0,1,0,1], //1
    [0,0,1,1,1], //2s
    [1,1,0,1,0], //3
    [0,1,1,0,1], //4
    [1,1,0,1,0], //5
];

let tamano2  = 5;
let graph2 = [
    [0,1,1,1,0], //1
    [1,0,0,0,1], //2s
    [1,0,0,1,1], //3
    [1,0,1,0,1], //4
    [0,1,1,1,0], //5
];

let tamano3  = 4;
let graph3 = [
    [0,1,1,0], //1
    [1,0,1,1], //2s
    [1,1,0,0], //3
    [0,1,0,0], //4
];

let tamano4  = 4;
let graph4 = [
    [0,1,0,1], //1
    [1,0,1,0], //2s
    [0,1,0,1], //3
    [1,0,1,0], //4
];

coloring(tamano1, graph1)
coloring(tamano2, graph2)
coloring(tamano3, graph3)
coloring(tamano4, graph4)