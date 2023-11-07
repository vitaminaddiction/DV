$(document).ready(function(){
    function fetchDataAndDrawChart() {
        let selected_year = $("#selected_year").val();
        let item = $("#item").val();

        console.log(selected_year);
        console.log(item);

        $.ajax({
            url: 'http://192.168.0.208:5000/menu4',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({
                selected_year,
                item
            }),
            success: function(response) {
                let imgSrc = 'data:image/png;base64,' + response.image;
                $("#image").attr("src", imgSrc);
                myPieChart.data.datasets[0].data = response.valList;
                myPieChart.data.labels = [selected_year];
                myPieChart.data.datasets[0].label = item;
                myPieChart.update();
            }
        });
    }


    $("#graphBtn").click( () => {
        fetchDataAndDrawChart();
    });
});