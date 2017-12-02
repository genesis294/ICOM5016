// When the document has finished loading:
  $(document).ready(function(){
    $.getJSON( "available/all", function( data ) {
      alert("I actually got here.")
      var resources = [];
      $.each( data, function( key, val ) {
        resources.push( "<li id='" + key + "'>"
        + val + "</li>" );
      });

      $( "<ul/>", {
        "class": "my-new-list",
        html: resources.join( "" )
      }).appendTo( ".resources" );
    });
});
