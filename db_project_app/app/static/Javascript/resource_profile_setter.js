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
          $("#prof_price").append("$ "+val.rprice);

        });

      });
    }

});
