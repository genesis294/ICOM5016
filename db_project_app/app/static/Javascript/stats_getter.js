// When the document has finished loading:
$(document).ready(function(){
  stat_type = $(".stats").attr("id");
  url = stat_type + "Stats/get"
  if(stat_type == "daily" || stat_type == "weekly"){
    daily_stats(url);
  }
  else {
    regional_stats(url);
  }
});

function daily_stats(url) {
  $.getJSON( url, function( data ) {
    $.each( data, function( key, val ) {
      $("#req_num").append(val.requests);
      $("#ava_num").append(val.available);
      $("#don_num").append(val.donations);
      displayCharts(val);
    });
  });

}
function displayCharts(val) {
  var total = val.available + val.requests;
  new Chart(document.getElementById("submited_resources_pie_chart"), {
    type: 'doughnut',
    data: {
      labels: ["On Sale ("+((val.onSale/total)*100).toFixed(2)+"%)",
      "Requests ("+((val.requests/total)*100).toFixed(2)+"%)",
      "Donations ("+((val.donations/total)*100).toFixed(2)+"%)"],
      datasets: [{
        label: "Resources",
        backgroundColor: ["#C0392B", "#58D68D","#2980B9"],
        data: [val.onSale, val.requests, val.donations]
      }]
    },
    options: {
      responsive: false,
      maintainAspectRatio: true,
      title: {
        display: true,
        text: 'Added Resources',
        fontSize: 30
      },
      legend: {
        labels: {
          fontSize: 20
        }
      },
      tooltips: {
        bodyFontSize: 20,
        displayColors: false
      }
    }
  });
  new Chart(document.getElementById("supplies_available_bar_chart"), {
    type: 'bar',
    data: {
      labels: ["Donated", "On Sale"],
      datasets: [
        {
          label: "Resources",
          backgroundColor: ["#A569BD", "#F4D03F"],
          data: [val.donations,val.onSale]
        }
      ]
    },
    options: {
      responsive: false,
      maintainAspectRatio: true,
      legend: {
        display: false
      },
      tooltips: {
        display: false
      },
      title: {
        display: true,
        fontSize: 30,
        text: 'Donated vs On Sale Supplies'
      },
      scales: {
        yAxes: [{
                 ticks: {
                     beginAtZero: true,
                     steps: 10,
                     stepValue: 5,

                 }
        }],
        xAxes: [{
            ticks: {
                fontSize: 20
            }
        }]
      }
    }
  });
  console.log(val.ava);
  new Chart(document.getElementById("resources_by_type_bar_chart"), {
    type: 'horizontalBar',
    data: {
      labels: ["Batteries", "Clothes", "Food","Fuel", "Heavy Equipment",
          "Ice", "Medical Devices", "Medication", "Power Generators", "Tools",
          "Water"
          ],
      datasets: [
        {
          label: "Requests",
          backgroundColor: "#5D6D7E",
          data: [val.batteries_request,val.clothes_request,val.food_request,
            val.fuel_request,val.heavy_equipment_request, val.ice_request,
            val.medical_devices_request, val.medication_request,
            val.power_generators_request, val.tools_request,val.water_request]
        }, {
          label: "Supplies Available",
          backgroundColor: "#5499C7",
          data:  [val.batteries_available,val.clothes_available,val.food_available,
            val.fuel_available,val.heavy_equipment_available, val.ice_available,
            val.medical_devices_available, val.medication_available,
            val.power_generators_available, val.tools_available,val.water_available]
        }
      ]
    },
    options: {
      responsive: false,
      maintainAspectRatio: true,
      legend: {
        display: true
      },
      tooltips: {
        display: false
      },
      title: {
        display: true,
        fontSize: 30,
        text: 'Resources by Category'
      },
      scales: {
        yAxes: [{
                 ticks: {
                     beginAtZero: true,
                     steps: 10,
                     stepValue: 5,
                     fontSize: 20
                 }
        }],
        xAxes: [{
            ticks: {
                fontSize: 10
            }
        }]
      }
    }
  });

}
function regional_stats() {
  $.getJSON( "regionStats/get", function( data ) {
    $.each( data, function( key, val ) {
      // San Juan, Bayamon, Arecibo, Mayaguez, Ponce, Guayama, Humacao, Carolina
      districts = [];
      var i = 0;
      $.each( val, function( index, val ) {
        districts.push(val.district);
        $("#region_name_"+i).append(val.district);
        $("#req_num_"+i).append(val.requests);
        $("#ava_num_"+i).append(val.available);
        $("#don_num_"+i).append(val.donation);
        i++;

      });
      displayRegionChart(val, districts);
      i=0
      for(i; i<8; i++)
      {
        displayCategoryChart(val[i], val[i]['district'], i)
      }

    });
  });

}
function displayRegionChart(val, districts)
{
  new Chart(document.getElementById("resources_by_region_bar_chart"), {
    type: 'horizontalBar',
    data: {
      labels: districts,
      datasets: [
        {
          label: "Requests",
          backgroundColor: "#5D6D7E",
          data: [val[0]['requests'], val[1]['requests'], val[2]['requests'], val[3]['requests'],
          val[4]['requests'], val[5]['requests'], val[6]['requests']]
        }, {
          label: "Supplies Available",
          backgroundColor: "#5499C7",
          data: [val[0]['available'], val[1]['available'], val[2]['available'], val[3]['available'],
          val[4]['available'], val[5]['available'], val[6]['available']]
        }
      ]
    },
    options: {
      responsive: false,
      maintainAspectRatio: true,
      legend: {
        labels: {
          fontSize: 20
        }
      },
      tooltips: {
        display: false
      },
      title: {
        display: true,
        fontSize: 30,
        text: 'Resources per District'
      },
      scales: {
        yAxes: [{
                 ticks: {
                     beginAtZero: true,
                     steps: 10,
                     stepValue: 5,

                 }
        }]
      }
    }
  });

}
function displayCategoryChart(val, district, i){
  new Chart(document.getElementById("resources_by_category_in_region_bar_chart_"+i), {
    type: 'horizontalBar',
    data: {
      labels:["Batteries", "Clothes", "Food","Fuel", "Heavy Equipment",
          "Ice", "Medical Devices", "Medication", "Power Generators", "Tools",
          "Water"
          ],
      datasets: [
        {
          label: "Requests",
          backgroundColor: "#5D6D7E",
          data: [val.batteries_request,val.clothes_request,val.food_request,
            val.fuel_request,val.heavy_equipment_request, val.ice_request,
            val.medical_devices_request, val.medication_request,
            val.power_generators_request, val.tools_request,val.water_request]
        }, {
          label: "Supplies Available",
          backgroundColor: "#5499C7",
          data: [val.batteries_available,val.clothes_available,val.food_available,
            val.fuel_available,val.heavy_equipment_available, val.ice_available,
            val.medical_devices_available, val.medication_available,
            val.power_generators_available, val.tools_available,val.water_available]
        }
      ]
    },
    options: {
      responsive: false,
      maintainAspectRatio: true,
      legend: {
        labels: {
          fontSize: 20
        }
      },
      tooltips: {
        display: false
      },
      title: {
        display: true,
        fontSize: 25,
        text: 'Resources per Category in '+ district
      },
      scales: {
        yAxes: [{
                 ticks: {
                     beginAtZero: true,
                     steps: 10,
                     stepValue: 5,

                 }
        }]
      }
    }
  });
}
