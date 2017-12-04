// Receives the url where to get the JSON
// Displays a list of the resources
function extractJSON(url){
  // Gets the JSON
  $.getJSON( url, function( data ) {
    // List to store the resource list
    var resources = [];
    // Styling for the links that will be added to the HTML
    var style="\"text-decoration: none; color : black;\""

    $.each( data, function( key, val ) {
      // If list is empty then no resources are available
      if(val.length==0)
      {
          $("<h1>No resource found.</h1>").appendTo(".resources");
      }
      else {
        // Loop through each resource in the JSON
        $.each( val, function( index, val ) {
          // URL to go to if a resource is clicked on
          var url="resource_profile";
          // ID of the link clicked. Also the id of the resource.
          var link_id=val.rid;
          // Add to the resource list each item in the JSON as an HTML code
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
        // JOin the pushed items from the list and add them to the resources div
      $( resources.join( "" )).appendTo( ".resources" );
      // Add CSS styling to the appended HTML
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
      // Place the name of the
      $(rname).css({
        "text-align" : "center"
      });
    }
  });
  }).fail(function(){
    // If the JSON failed to appear then no resource was found
      $("<h1>No resource found.</h1>").appendTo(".resources");
  });
}
// Sends the clicked recources id to JS function that displays resources profile
function send_id(id)
{
  // If requested send a 1 to profile so it knows which list to look though
  if($(".resources").attr("id")=="requested")
  {
    // Save in local data which type of resource is being asked for
    sessionStorage.setItem("req",1);
  }
  else {
    sessionStorage.setItem("req",0);
  }
  // Save in local data id of the resource
  sessionStorage.setItem("rid",id);
}