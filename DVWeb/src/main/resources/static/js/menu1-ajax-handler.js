$(document).ready(function(){
    function fetchDataAndDrawChart() {
        let firstDate = $("#firstDate").val();
        let secondDate = $("#secondDate").val();
        let item = $("#item").val();

        $.ajax({
            url: 'http://13.209.19.170:5000/menu1',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({
                firstDate,
                secondDate,
                item
            }),
            success: function(response) {
                let imgSrc = 'data:image/png;base64,' + response.image;
                $("#image").attr("src", imgSrc);
                myBarChart.data.datasets[0].data = response.valList;
                myBarChart.data.labels = [firstDate, secondDate];
                myBarChart.data.datasets[0].label = item;
                myBarChart.update();
            }
        });
    }


    $("#graphBtn").click( () => {
        fetchDataAndDrawChart();
    });
});