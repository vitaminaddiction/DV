$(document).ready(function(){
    function fetchDataAndDrawChart() {
        let startDate = $("#startDate").val();
        let endDate = $("#endDate").val();
        let item = $("#item").val();
        console.log(startDate);
        console.log(generateMonths(startDate, endDate));

        $.ajax({
            url: 'http://192.168.0.208:5000/menu2',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({
                startDate,
                endDate,
                item
            }),
            success: function(response) {
                let imgSrc = 'data:image/png;base64,' + response.image;
                $("#image").attr("src", imgSrc);
                myLineChart.data.datasets[0].data = response.val1List;
                myLineChart.data.labels = generateMonths(startDate, endDate);
                myLineChart.data.datasets[1].data = response.val2List;
                myLineChart.data.datasets[1].label = item;
                myLineChart.update();
            }
        });
    }


    $("#graphBtn").click( () => {
        fetchDataAndDrawChart();
    });

    function generateMonths(startMonth, endMonth) {
        var startDate = new Date(startMonth);
        var endDate = new Date(endMonth);
        var labels = [];

        while (startDate <= endDate) {
            var year = startDate.getFullYear();
            var month = (startDate.getMonth() + 1).toString().padStart(2, '0'); // 월은 0부터 시작하므로 1을 더하고 2자리로 패딩
            labels.push(year + '-' + month);

            // 다음 달로 이동
            startDate.setMonth(startDate.getMonth() + 1);
        }

        return labels;
    }
});