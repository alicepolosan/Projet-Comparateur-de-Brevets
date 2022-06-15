document.addEventListener("DOMContentLoaded", () => {
    const barCanvas = document.getElementById("BarCanvas");

    const mixedChart = new Chart(barCanvas, {
        type:'bar',
        data: {
            labels: ['2021','2022','2023','2024'],
            datasets: [{
                type : 'bar',
                label: 'Coûts par année',
                data: [3000, 3200, 2900, 4000],
                backgroundColor: [
                    'pink',
                    'lightblue',
                    'lightgreen',
                    'yellow'],
                borderColor:'white'
            }, {
                type : 'line',
                label: 'Coûts cumulés',
                data: [3000, 6200, 9100, 13700],
                fill: false,
                backgroundColor: 'crimson',
                borderColor: 'crimson'
            }]
        },
        options: { 
            scales: {
                yAxes: [{
                    suggestedMax: 6000,
                    suggestedMin: 1000
                }]
            }
        }
    });
}); 

/* Mes problèmes : 
1.Je n'arrive pas à faire en sorte que mes options soient bien prises en compte... 
en tout cas la partie y ou yAxes...

2. Pour utiliser les données qu'Anaïs aura calculé en python, 
il faut que je trouve un moyen de convertir des array ou des listes python en array js
--> en utilisant Json ?? */