function getCategory(resource_type, category) {
  // Clear screen so we can display the new list with the results of the search
  $(".resources").empty();
  // Get and extract the JSON
  if(category == "all"){
    extractJSON("/" + resource_type);
  }
  else {
      extractJSON("/" + resource_type + "/" + category);
  }

}
