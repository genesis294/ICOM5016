// When the document has finished loading:
  $(document).ready(function(){
    // Get user to get JSON from for the whole list of resources
    var url = "/" + $(".resources").attr("id");
    extractJSON(url);
});
