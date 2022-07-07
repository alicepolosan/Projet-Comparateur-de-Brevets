
let map = new Map()
map.set(" Albanie ",  "black")
map.set(" Allemagne ", "blue")
map.set(" Autriche ", "blue")
map.set(" Bulgarie ", "blue")
map.set(" Belgique ", "blue")
map.set(" Danemark ", "blue")
map.set(" Estonie ", "blue")
map.set(" Finlande ", "blue")
map.set(" France ", "blue")
map.set(" Italie ", "blue")
map.set(" Lettonie ", "blue")
map.set(" Lituanie ", "blue")
map.set(" Luxembourg ", "blue")
map.set(" Malte ", "blue")
map.set(" Pays-Bas ", "blue")
map.set(" Portugal ", "blue")
map.set(" Slovénie ", "blue")
map.set(" Suède ", "blue")
map.set(" Chypre ", "black")
map.set(" Croatie ", "black")
map.set(" Espagne ", "black")
map.set(" Grèce ", "black")
map.set(" Hongrie ", "black")
map.set(" Irlande ", "black")
map.set(" Islande ", "black")
map.set(" Liechtenstein (cf. Suisse) ", "black")
map.set(" Macédoine du Nord ", "black")
map.set(" Monaco ", "black")
map.set(" Norvège ", "black")
map.set(" Pologne ", "black")
map.set(" République Tchèque ", "black")
map.set(" Roumanie ", "black")
map.set(" Royaume-Uni ", "black")
map.set(" Saint-Marin ", "black")
map.set(" Serbie ", "black")
map.set(" Slovaquie ", "black")
map.set(" Suisse ", "black")
map.set(" Turquie ", "black")

document.addEventListener("DOMContentLoaded", () => {
    
    const barCanvas = document.getElementById("BarCanvas"); /* On sélectionne l'élément canvas */
    let Pays_p = document.querySelectorAll(".pays-recup");
    let Pays = [];
    for (let i = 0; i < Pays_p.length; i++) {
        Pays.push(Pays_p[i].textContent);
    }
    console.log(Pays)
    for (let i = 0; i < Pays.length; i++) {
        let my_p = document.createElement('p')
        console.log(Pays[i])
        console.log(map.get(Pays[i]))
        my_p.textContent = Pays[i]
        my_p.style.color = map.get(Pays[i])
        document.getElementById('Pays').append(my_p)
    }
    let list0 = JSON.parse("[" + document.getElementById("list0").textContent + "]")[0]
    let list1 = JSON.parse("[" + document.getElementById("list1").textContent + "]")[0]
    let list2 = JSON.parse("[" + document.getElementById("list2").textContent + "]")[0]
    let list3 = JSON.parse("[" + document.getElementById("list3").textContent + "]")[0]
    let list4 = JSON.parse("[" + document.getElementById("list4").textContent + "]")[0]

    /* On crée une nouvelle instance à partir de la librairie Chart.js */
    /* On lui passe deux arguments : le canvas sur lequel on va afficher le graphique et toute la configuration */
    const mixedChart = new Chart(barCanvas, {
        type:'bar', 
        data: {
            labels: list0,
            datasets: [
                {
                    type : 'line',                            /* type du graphique */
                    label: 'Coûts cumulés - Brevet Européen',
                    data: list1,                              /* données représentées par le graphique */ 
                    fill: false,
                    backgroundColor: 'green',
                    borderColor: 'green'
                },
                {
                    type : 'line',
                    label: 'Coûts cumulés - Brevet Unitaire',
                    data: list2,
                    fill: false,
                    backgroundColor: 'blue',
                    borderColor: 'blue'
                },
                {
                    type : 'bar',
                    label: 'Coûts par année - Brevet Unitaire',
                    data: list3,
                    backgroundColor:'lightblue',
                    borderColor:'white'
                 }, 
                {
                    type : 'bar',
                    label: 'Coûts par année - Brevet Européen',
                    data: list4,
                    backgroundColor:'lightgreen',
                    borderColor:'white'
                }]
        },
        options: {                                               /* Système d'options pour modifier l'aspect du graphique  */
            title: { 
                display: true,
                fontSize: 25 ,
                position : 'top',
                text: 'Comparateur Brevet Unitaire et Brevet Européen'
            },
            scales: {
                yAxes: [{
                    scaleLabel: {
                    beginAtZero : true,
                    display: true,
                    grace : '10%',
                    labelString: 'Coûts (en euros)'
                    }
                }],
                xAxes: [{
                    scaleLabel: {
                    beginAtZero : true,
                    display: true,
                    labelString: 'Année'
                    }
                }],
            }
        }
    });
}); 

