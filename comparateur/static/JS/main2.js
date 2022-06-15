document.addEventListener("DOMContentLoaded", () => {
    const barCanvas = document.getElementById("BarCanvas");

    const mixedChart = new Chart(barCanvas, {
        type:'bar',
        data: {
            labels: ['2021','2022','2023','2024'],
            datasets: [
                {
                    type : 'line',
                    label: 'Coûts cumulés',
                    data: [3600, 6600, 11000, 13600],
                    fill: false,
                    backgroundColor: 'blue',
                    borderColor: 'blue'
                },
                {
                    type : 'line',
                    label: 'Coûts cumulés',
                    data: [3000, 6200, 9100, 13700],
                    fill: false,
                    backgroundColor: 'green',
                    borderColor: 'green'
                },
                {
                type : 'bar',
                label: 'Coûts par année - Brevet Unitaire',
                data: [3000, 3200, 2900, 4000],
                backgroundColor: [
                    'lightgreen',
                    'lightgreen',
                    'lightgreen',
                    'lightgreen'],
                borderColor:'white'
            }, 
            {
                type : 'bar',
                label: 'Coûts par année - Brevet Européen',
                data: [3600, 3000, 3500, 2600],
                backgroundColor: [
                    'lightblue',
                    'lightblue',
                    'lightblue',
                    'lightblue'],
                borderColor:'white'
            }]
        },
        options: { 
            scales: {
                y: {
                    beginAtZero: true,
                    title:'Coûts (€)'
                },
                x : {
                    title:'Temps (année)'
                }
            }
        }
    });
}); 

