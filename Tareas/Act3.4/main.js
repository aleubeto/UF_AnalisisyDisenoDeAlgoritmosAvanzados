//    tsc filename.ts
//    node filename.js
var tamano = 5;
var graph = [
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0], //5
];
var mapa = new Map();
for (var i = 0; i < tamano; i++) {
    mapa.set(graph[i], -1);
}
for (var i = 0; i < tamano; i++) {
    for (var j = 0; j < tamano; j++) {
        if (graph[i][j] == 1) {
            if (mapa.get(graph[j]) == mapa.get(graph[i])) {
                mapa.set(graph[i], (Math.max(mapa.get(graph[i]), mapa.get(graph[j])) + 1));
                j = 0;
            }
        }
    }
}
for (var i = 0; i < tamano; i++) {
    mapa.set(graph[i], 0);
    for (var j = 0; j < tamano; j++) {
        if (graph[i][j] == 1) {
            if (mapa.get(graph[j]) == mapa.get(graph[i])) {
                mapa.set(graph[i], (Math.max(mapa.get(graph[i]), mapa.get(graph[j])) + 1));
                j = 0;
            }
        }
    }
}
for (var i = 0; i < tamano; i++) {
    console.log("Node: " + (i + 1) + " , Assigned Color: " + mapa.get(graph[i]));
}
