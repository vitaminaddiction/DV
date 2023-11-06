// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myLineChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["2013-01","2013-02","2013-03","2013-04","2013-05","2013-06","2013-07","2013-08","2013-09","2013-10","2013-11","2013-12"],
    datasets: [{
         label: "쌀",
         lineTension: 0.3,
         backgroundColor: [
                 "rgba(255,255,255,0)",
                 "rgba(255,255,255,0)",
               ],
         borderColor: "rgba(93, 159, 95, 1)",
         pointRadius: 5,
         pointBackgroundColor: "rgba(93, 159, 95, 1)",
         pointBorderColor: "rgba(255,255,255,0.8)",
         pointHoverRadius: 5,
         pointHoverBackgroundColor: "rgba(93, 159, 95, 1)",
         pointHitRadius: 50,
         pointBorderWidth: 2,
         data: [87.460, 87.901, 88.038, 88.555, 88.258, 88.458, 88.231, 88.746, 88.905, 89.455, 89.001, 88.320],
       },
       {
         label: "수입쇠고기",
         lineTension: 0.3,
         backgroundColor: [
                 "rgba(255,255,255,0)",
                 "rgba(255,255,255,0)",
               ],
         borderColor: "rgba(2,117,216,1)",
         pointRadius: 5,
         pointBackgroundColor: "rgba(2,117,216,1)",
         pointBorderColor: "rgba(255,255,255,0.8)",
         pointHoverRadius: 5,
         pointHoverBackgroundColor: "rgba(2,117,216,1)",
         pointHitRadius: 50,
         pointBorderWidth: 2,
         data: [74.657, 77.634, 75.938, 75.120, 74.913, 75.176, 77.648, 78.278, 81.117, 80.591, 80.632, 81.352],
       },
       {
        label: "휘발유",
        lineTension: 0.3,
        backgroundColor: [
                "rgba(255,255,255,0)",
                "rgba(255,255,255,0)",
              ],
        borderColor: "rgba(131, 65, 164, 1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(131, 65, 164, 1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(131, 65, 164, 1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: [138.839, 140.689, 143.525, 140.713, 136.853, 137.100, 139.492, 140.528, 139.418, 137.149, 135.213, 135.374],
      },
      {
       label: "도시가스",
       lineTension: 0.3,
       backgroundColor: [
               "rgba(255,255,255,0)",
               "rgba(255,255,255,0)",
             ],
       borderColor: "rgba(131, 241, 129, 1)",
       pointRadius: 5,
       pointBackgroundColor: "rgba(131, 241, 129, 1)",
       pointBorderColor: "rgba(255,255,255,0.8)",
       pointHoverRadius: 5,
       pointHoverBackgroundColor: "rgba(131, 241, 129, 1)",
       pointHitRadius: 50,
       pointBorderWidth: 2,
       data: [131.442, 131.442, 136.792, 136.792, 136.759, 136.759, 136.750, 138.153, 138.229, 138.229, 138.251, 138.251],
     },
     {
      label: "전기료",
      lineTension: 0.3,
      backgroundColor: [
              "rgba(255,255,255,0)",
              "rgba(255,255,255,0)",
            ],
      borderColor: "rgba(224, 255, 133, 1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(224, 255, 133, 1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(224, 255, 133, 1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [113.297, 113.297, 113.297, 113.297, 113.297, 113.297, 113.297, 113.297, 113.297, 113.297, 116.362, 116.362],
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
