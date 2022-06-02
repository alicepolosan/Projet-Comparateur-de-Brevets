const barCanvas = document.getElementById("BarCanvas");

const barChart = new Chart(barCanvas, {
    type : 'bar',
    data : {
        labels : ['2021','2022','2023','2024'],
        datasets : [{
            data : [3000, 3200, 2900, 3600],
            backgroudColor : ["crimson", "lightblue", "lightgreen","lightviolet"]
        }]
    }
});