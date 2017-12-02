// When the document has finished loading:
  $(document).ready(function(){
    $.getJSON( "available/all", function( data ) {
      var resources = [];
      $.each( data, function( key, val ) {
          console.log(key)
        $.each( val, function( index, val ) {
          console.log(index, val)
          resources.push( "<div id='res'>"
          + "<h2>"+ val.rname + "</h2>"
          + "<div id=rid>"
          + "<label><b>Resource ID: <b>"+ val.rid + "</label>"
          + "</div> <div id=rquantity>"
          + "<label><b>Quantity: <b>"+ val.rquantity + "</label>"
          + "</div><div id=rprice>"
          + "<label><b>Price: <b>"+ val.rprice + "</label>"
          + "</div></div>" );
        });
      });

      $( "<ul/>", {
        "class": "my-new-list",
        html: resources.join( "" )
      }).appendTo( ".resources" );
      $(res).css({
        "padding":"5px",
        "padding-left": "10px",
        "width": "90%",
        "height": "10%",
        "background-color": "	#F0F8FF",
        "margin": "auto, 5px",
        "margin-top" : "10px",
        "border": "2px solid #89CFF0"
      });
    
    });
});
