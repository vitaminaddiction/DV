$(document).ready(function(){
    function fetchDataAndDrawChart() {
        let firstDate = $("#firstDate").val();
        let secondDate = $("#secondDate").val();
        let item = $("#item").val();

        if (!firstDate)
            {
                firstDate = "기본 값";
            }
            if (!secondDate) {
                secondDate = "기본 값";
            }
            if (!item) {
                item = "기본 아이템";
            }

        $.ajax({
            url: 'http://192.168.0.32:5000/menu1',
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
                myBarChart.data.label = item;
                myBarChart.update();
            }
        });
    }

    fetchDataAndDrawChart();

    $("#graphBtn").click( () => {
        fetchDataAndDrawChart();
    });
});