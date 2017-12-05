// When the document has finished loading:
  $(document).ready(function(){
    var req = sessionStorage.getItem("req");
    var id = sessionStorage.getItem("rid");
    if(req==1)
    {
      $.getJSON( "requested/"+id, function( data ) {
        $.each( data, function( key, val ) {
          $("#prof_name").append(val.rname);
          $("#prof_id").append(val.rid);
          $("#prof_quantity").append(val.rquantity);


        });

      });
    }
    else {
      $.getJSON( "available/"+id, function( data ) {
        $.each( data, function( key, val ) {
          $("#prof_name").append(val.rname);
          $("#prof_id").append(val.rid);
          $("#prof_quantity").append(val.rquantity);
          if(val.rprice == 0)
          {
            $("#prof_price").append("Free");
            $(".profile").append("<input type='button' id='bttn' value='Reserve'></input>");
          }
          else {
            $("#prof_price").append("$ "+val.rprice);
            $(".profile").append("<input type='button' id='bttn' value='Purchase'></input>");
          }
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
          $(bttn).click(function () {
              window.location.href="/purchase";
          });


        });

      });
    }

});
