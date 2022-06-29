document.addEventListener("DOMContentLoaded", () => {
    const barCanvas = document.getElementById("BarCanvas");
    let list0 = JSON.parse("[" + document.getElementById("list0").textContent + "]")[0]
    console.log(list0)
    let list1 = JSON.parse("[" + document.getElementById("list1").textContent + "]")[0]
    let list2 = JSON.parse("[" + document.getElementById("list2").textContent + "]")[0]
    let list3 = JSON.parse("[" + document.getElementById("list3").textContent + "]")[0]
    let list4 = JSON.parse("[" + document.getElementById("list4").textContent + "]")[0]
    const mixedChart = new Chart(barCanvas, {
        type:'bar',
        data: {
            labels: list0,
            datasets: [
                {
                    type : 'line',
                    label: 'Coûts cumulés',
                    data: list1,
                    fill: false,
                    backgroundColor: 'blue',
                    borderColor: 'blue'
                },
                {
                    type : 'line',
                    label: 'Coûts cumulés',
                    data: list2,
                    fill: false,
                    backgroundColor: 'green',
                    borderColor: 'green'
                },
                {
                type : 'bar',
                label: 'Coûts par année - Brevet Unitaire',
                data: list3,
                backgroundColor:'lightgreen',
                borderColor:'white'
            }, 
            {
                type : 'bar',
                label: 'Coûts par année - Brevet Européen',
                data: list4,
                backgroundColor:'lightblue',
                borderColor:'white'
            }]
        },
        options: { 
            plugins: {
                title: {
                    display: true,
                    text: 'Comparateur Brevet Unitaire et Brevet Européen'
                }
            },
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

