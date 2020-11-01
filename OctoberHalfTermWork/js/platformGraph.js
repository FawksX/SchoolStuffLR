// Code via CanvasJS

window.onload = function () {

    var chart = new CanvasJS.Chart("chartContainer", {
        animationEnabled: true,
        title:{
            horizontalAlign: "center"
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            indexLabelFontSize: 17,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            dataPoints: [
                { y: 18, label: "PC" },
                { y: 47, label: "Console" },
                { y: 34, label: "Mobile" },
                { y: 2, label: "Other"}
            ]
        }]
    });
    chart.render();

    var chart2 = new CanvasJS.Chart("industryWorth", {
        animationEnabled: true,
        title:{
            horizontalAlign: "center"
        },
        data: [{
            type: "doughnut",
            startAngle: 60,
            indexLabelFontSize: 17,
            indexLabel: "{label} - #percent%",
            toolTipContent: "<b>{label}:</b> {y} (#percent%)",
            dataPoints: [
                { y: 51, label: "Mobile ($70Bn)" },
                { y: 24, label: "PC ($32.9Bn)" },
                { y: 25, label: "Console ($34.6Bn)" }
            ]
        }]
    });
    chart2.render();

}

