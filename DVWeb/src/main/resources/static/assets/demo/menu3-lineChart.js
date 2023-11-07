// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myLineChart");
var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ["2016-10","2016-11","2016-12","2017-01","2017-02","2017-03","2017-04","2017-05","2017-06","2017-07","2017-08","2017-09"],
    datasets: [{
         label: "오징어",
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
         data: [49.419, 57.865, 62.568, 61.403, 64.832, 66.03, 67.378, 70.925, 73.02, 72.268, 72.428, 76.477],
       },
       {
         label: "식용유",
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
         data: [118.223, 110.929, 109.42, 108.858, 108.452, 109.297, 105.65, 111.39, 108.34, 108.34, 109.364, 105.92],
       },
       {
        label: "돼지고기",
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
        data: [96.022, 94.033, 91.761, 91.077, 91.56, 90.712, 93.23, 100.338, 103.423, 105.631, 104.436, 104.308],
      },
      {
       label: "당근",
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
       data: [86.283, 103.482, 124.871, 128.604, 117.952, 97.2, 90.678, 81.216, 76.118, 72.493, 69.782, 79.304],
     },
     {
      label: "생활물가지수",
      lineTension: 0.3,
      backgroundColor: [
              "rgba(255,255,255,0)",
              "rgba(255,255,255,0)",
            ],
      borderColor: "rgba(255, 36, 0, 1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(255, 36, 0, 1)",
      pointBorderColor: "rgba(255,255,255,0.8)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(255, 36, 0, 1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: [96.292, 96.245, 96.074, 97.516, 97.923, 97.914, 97.535, 97.582, 97.468, 97.487, 98.255, 98.606],
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
