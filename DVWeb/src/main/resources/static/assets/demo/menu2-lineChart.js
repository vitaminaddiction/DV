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
      label: "생활물가지수",
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
      data: [94.310, 94.750, 94.521, 94.327, 94.001, 93.771, 93.851, 94.485, 94.653, 94.142, 93.939, 94.107],
    },
    {
      label: "쌀",
      lineTension: 0.3,
      backgroundColor: [
                    "rgba(255,255,255,0)",
                    "rgba(255,255,255,0)",
                  ],
      borderColor: "rgba(255, 193, 7, 1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(255, 193, 7, 1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(255, 193, 7, 1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [87.460, 87.901, 88.038, 88.555, 88.258, 88.458, 88.231, 88.746, 88.905, 89.455, 89.001, 88.320],
    }
    ],
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
          min: 80,
          max: 100,
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

