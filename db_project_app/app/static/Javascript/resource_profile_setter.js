// When the document has finished loading:
  $(document).ready(function(){
    // Check if the resource is a request or an available supply
    var req = sessionStorage.getItem("req");
    // Get the id of the resource
    var id = sessionStorage.getItem("rid");
    // If it's a request
    if(req==1)
    {
      console.log(id)
      // Make the GET
      $.getJSON( "requested/"+id, function( data ) {
        $.each( data, function( key, val ) {
          // Fix date so the time isn't shown
          var date = val.rdate_added.slice(0, val.rdate_added.length - 12);
          //Product name
          $("#prof_name").append(val.rname);
          // Product id
          $("#prof_id").append(val.rid);
          // Product quantity
          $("#prof_quantity").append(val.rquantity);
          // Date added
          $("#prof_date").append(date);
        });

      });
    }
    else {
      // GET resource
      $.getJSON( "available/"+id, function( data ) {
        $.each( data, function( key, val ) {
          // Fix date so the time isn't shown
          var date = val.rdate_added.slice(0, val.rdate_added.length - 12);
          var category = val.rcategory;
          // Product name
          $("#prof_name").append(val.rname);
          // Product id
          $("#prof_id").append(val.rid);
          // Product quantity
          $("#prof_quantity").append(val.rquantity);
          // Date added
          $("#prof_date").append(date);

          // Water
          if (category == "water")
          {
            $(".profile").append("<p><b>Type: </b>" + val.wtype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.wbrand + "</p>");
          }
          // Ice
          else if (category == "ice") {
            $(".profile").append("<p><b>Size: </b>" + val.isize + "</p>");
          }
          // Food
          else if (category == "food"){
            $(".profile").append("<p><b>Type: </b>" + val.ftype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.fbrand + "</p>");
            $(".profile").append("<p><b>Amount: </b>" + val.famount + "</p>");
            $(".profile").append("<p><b>Exp. Date: </b>" + val.fexp_date + "</p>");
          }
          // Medication
          else if (category == "medication"){
            $(".profile").append("<p><b>Type: </b>" + val.mtype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.mbrand + "</p>");
            $(".profile").append("<p><b>Amount: </b>" + val.mamount + "</p>");
            $(".profile").append("<p><b>Dosage: </b>" + val.mdose + "</p>");
          }
          // Medical devices
          else if (category == "medical_devices"){
            $(".profile").append("<p><b>Type: </b>" + val.mdtype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.mdbrand + "</p>");
            $(".profile").append("<p><b>Power Source: </b>" + val.mdpower_type + "</p>");
            $(".profile").append("<p><b>Precision: </b>" + val.mdprecision + "</p>");
          }
          // Clothes
          else if (category == "clothes"){
            $(".profile").append("<p><b>Gender: </b>" + val.cgender + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.cbrand + "</p>");
            $(".profile").append("<p><b>Material: </b>" + val.cmaterial + "</p>");
          }
          // Power Generators
          else if (category == "power_generators"){
            $(".profile").append("<p><b>Brand: </b>" + val.pgbrand + "</p>");
            $(".profile").append("<p><b>Wats: </b>" + val.pgwatts + "</p>");
            $(".profile").append("<p><b>Gas: </b>" + val.pggas + "</p>");
          }
          // Batteries
          else if (category == "batteries"){
            $(".profile").append("<p><b>Type: </b>" + val.btype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.bbrand + "</p>");
            $(".profile").append("<p><b>Amount: </b>" + val.bsize + "</p>");
          }
          // Fuel
          else if (category == "fuel") {
            $(".profile").append("<p><b>Type: </b>" + val.fltype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.flbrand + "</p>");
            $(".profile").append("<p><b>Amount: </b>" + val.floctane + "</p>");
          }
          // Tools
          else if (category == "tools"){
            $(".profile").append("<p><b>Type: </b>" + val.ttype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.tbrand + "</p>");
          }
          // Heavy Equipment
          else if (category == "heavy_equipment"){
            $(".profile").append("<p><b>Type: </b>" + val.hetype + "</p>");
            $(".profile").append("<p><b>Brand: </b>" + val.hebrand + "</p>");
            $(".profile").append("<p><b>Size: </b>" + val.hesize + "</p>");
            $(".profile").append("<p><b>Weight: </b>" + val.heweight + "</p>");
            $(".profile").append("<p><b>Model: </b>" + val.hemodel + "</p>");
          }
          // If it was a donation then it is free
          if(val.sprice == 0)
          {
            $("#prof_price").append("Free");
            $(".profile").append("<input type='button' id='bttn' value='Reserve'></input>");
          }
          // Show price
          else {
            $("#prof_price").append("$ "+val.sprice);
            $(".profile").append("<input type='button' id='bttn' value='Purchase'></input>");
          }

          // CSS styling for the purchase button
          $(bttn).css({
            "background-color": "#4CAF50",
            "color": "white",
            "padding" : "14px 10px",
            "border": "none",
            "cursor": "pointer",
            "width": "50%",
            "margin-left": "75px",
            "font-size": "20px"
          });
          // Go to purchase page
          $(bttn).click(function () {
              window.location.href="/purchase";
          });


        });

      });
    }

});
