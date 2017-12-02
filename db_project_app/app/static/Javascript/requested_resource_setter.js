// When the document has finished loading:
  $(document).ready(function(){
    $.getJSON( "requested/all", function( data ) {
      var resources = [];
      var style="\"text-decoration: none; color : black;\""
      $.each( data, function( key, val ) {
        if(val.length==0)
        {
            $("<h1>No requests at the moment.</h1>").appendTo(".resources");
        }
        else {
          $.each( val, function( index, val ) {
            var url="resource_profile";
            var link_id=val.rid;
            resources.push( "<div id='res'>"
            + "<a id="+link_id+" style=" +style+" href="+url+" onclick='send_id("+link_id+")'>"
            + "<h2 id=rname>"+ val.rname + "</h2>"
            + "<div id=rid>"
            + "<label><b>Resource ID: </b>"+ val.rid + "</label>"
            + "</div> <div id=rquantity>"
            + "<label><b>Quantity: </b>"+ val.rquantity + "</label>"
            + "</div><div id=rprice>"
            + "<label><b>Price: </b>"+ val.rprice + "</label>"
            + "</a></div></div>" );
          });

        $( resources.join( "" )).appendTo( ".resources" );
        $(res).css({
          "display": "inline-block",
          "padding-left": "10px",
          "width": "20%",
          "height": "30%",
          "background-color": "#F0F8FF",
          "margin-left": "10px",
          "margin-top" : "10px",
          "border": "2px solid #89CFF0",
          "padding-bottom": "20px"
        });
        $(rname).css({
          "text-align" : "center"
        });
      }
    });
  });
});


function send_id(id)
{
  sessionStorage.setItem("req",1);
  sessionStorage.setItem("rid",id);
}
