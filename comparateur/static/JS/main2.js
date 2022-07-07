/* Ce document est le javascript associé à resultats.html. */

/* Création d'un dictionnaire (clé : pays, valeur : couleur (bleu/noir))
But : afficher les pays en couleur (bleu/noir) dans la page html de résultats 
(pour cela, il faut coder la correspondance entre pays et couleur). */

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

/* fin de la création du dictionnaire */

document.addEventListener("DOMContentLoaded", () => {
    
    const barCanvas = document.getElementById("BarCanvas");

    /* Affichage des pays sélectionnés en couleur */

    /* Récupération des pays sélectionnés */
    let Pays_p = document.querySelectorAll(".pays-recup"); 
    let Pays = [];
    for (let i = 0; i < Pays_p.length; i++) {
        Pays.push(Pays_p[i].textContent);
    }
    
    /* Affichage des pays sélectionnés en couleur (bleu/noir) dans l'onglet de résultats */
    for (let i = 0; i < Pays.length; i++) {
        let my_p = document.createElement('p')
        my_p.textContent = Pays[i]
        my_p.style.color = map.get(Pays[i])
        document.getElementById('Pays').append(my_p)
    }

    /* Affichage de la comparaison*/

    /* Récupération des listes des résultats déposées dans resultats.html et conversion*/
    let list0 = JSON.parse("[" + document.getElementById("list0").textContent + "]")[0]
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
                    label: 'Coûts cumulés - Brevet Européen',
                    data: list1,
                    fill: false,
                    backgroundColor: 'blue',
                    borderColor: 'blue'
                },
                {
                    type : 'line',
                    label: 'Coûts cumulés - Brevet Unitaire',
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

