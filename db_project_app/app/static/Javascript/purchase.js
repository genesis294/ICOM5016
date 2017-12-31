$(document).ready(function(){

  var id = sessionStorage.getItem("rid");

    $.getJSON( "available/"+id, function( data ) {
      $.each( data, function( key, val ) {
        $("#pname").append(val.rname);
        $("#pprice").append(val.rprice);
        $("#rname").append(val.rname);
        $("#rprice").append(val.sprice);
        $("#pavailable").append(val.rquantity);
        $(".hidden").val(val.rid);
    });
  });
});
