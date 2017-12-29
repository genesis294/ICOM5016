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
      $("#mat_num").append(val.matches);
      displayCharts(val);
    });
  });

}
function displayCharts(val) {
  var onsale = val.available - val.donations;
  var total = val.available + val.requests;
  console.log(onsale);
  console.log(total);
  new Chart(document.getElementById("submited_resources_pie_chart"), {
    type: 'doughnut',
    data: {
      labels: ["On Sale ("+((onsale/total)*100).toFixed(2)+"%)",
      "Requests ("+((val.requests/total)*100).toFixed(2)+"%)",
      "Donations ("+((val.donations/total)*100).toFixed(2)+"%)"],
      datasets: [{
        label: "Resources",
        backgroundColor: ["#C0392B", "#58D68D","#2980B9"],
        data: [onsale, val.requests, val.donations]
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
      labels: ["Donated", "For Sale"],
      datasets: [
        {
          label: "Resources",
          backgroundColor: ["#A569BD", "#F4D03F"],
          data: [val.donations,onsale]
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
  new Chart(document.getElementById("resources_by_type_bar_chart"), {
    type: 'horizontalBar',
    data: {
      labels: ["Water", "Ice", "Food", "Medication",
          "Medical Devices", "Clothes", "Fuel",
          " Power Generators", "Batteries", "Tools",
          "Heavy Equipment"],
      datasets: [
        {
          label: "Requests",
          backgroundColor: "#5D6D7E",
          data: [val.water_request,val.ice_request,val.food_request,
            val.medication_request,val.medical_devices_request,val.clothes_request,
            val.fuel_request,val.power_generators_request,val.batteries_request,
            val.tools_request,val.heavy_equipment_request]
        }, {
          label: "Supplies Available",
          backgroundColor: "#5499C7",
          data: [val.water_available,val.ice_available,val.food_available,
            val.medication_available,val.medical_devices_available,val.clothes_available,
            val.fuel_available,val.power_generators_available,val.batteries_available,
            val.tools_available,val.heavy_equipment_available]
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
      var i = 0;
      $.each( val, function( index, val ) {
        $("#region_name_"+i).append(val.district);
        $("#req_num_"+i).append(val.requests);
        $("#ava_num_"+i).append(val.available);
        $("#don_num_"+i).append(val.donations);
        $("#mat_num_"+i).append(0);
        i++;

      });
      displayRegionCharts(val, districts);
    });
  });

}
function displayRegionCharts(val, districts)
{
  new Chart(document.getElementById("resources_by_region_bar_chart"), {
    type: 'horizontalBar',
    data: {
      labels: districts,
      datasets: [
        {
          label: "Requests",
          backgroundColor: "#5D6D7E",
          data: [val["sanjuan"][0],val["bayamon"][0],val["arecibo"][0], val["mayaguez"][0],
        val["ponce"][0], val["guayama"][0], val["humacao"][0]]
        }, {
          label: "Supplies Available",
          backgroundColor: "#5499C7",
          data: [val["sanjuan"][1],val["bayamon"][1],val["arecibo"][1], val["mayaguez"][1],
        val["ponce"][1], val["guayama"][1], val["humacao"][1]]
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
