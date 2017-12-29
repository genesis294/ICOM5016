function search(resource_type)
{
  //Will hold search term for the url
  term="";
  // Name to search for
  s_name = $(".searchTerm1").val();
  if(resource_type == "available"){
    // Price to search for. Will look for prices <= to the one given.
    s_price = $(".searchTerm2").val();
  }
  else {
    s_price = ""
  }

  // Will search for items with >= the quantity given
  s_quantity = $(".searchTerm3").val();

  //If a name was given add it to the search term
  if(s_name!="")
  {
    term ="name="+s_name;
  }
  // If price given add it to term
  if(s_price!= "")
  {
    //If term empty this is the first parameter
    if(term=="")
    {
      term = "price="+s_price;
    }
    else {
      term = term+"&price="+s_price;
    }
  }
  //If quantity given add to term
  if(s_quantity!="")
  {
    //If term empty this is the first parameter
    if(term=="")
    {
      term = "quantity="+s_quantity;
    }
    else {
      term = term+"&quantity="+s_quantity;
    }
  }
  //If term empty then nothing then search bars were empty
  if(term=="")
  {
    return;
  }
  else {
    // Clear screen so we can display the new list with the results of the search
    $(".resources").empty();
    // Get and extract the JSON
    extractJSON("/"+resource_type+"?"+term);
  }
}
