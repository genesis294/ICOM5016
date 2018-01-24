//For showing password if user wants to see it.
function passwordToggle() {
  //Get password input element
  var x = document.getElementById("psw");
  //If the elements type is password then change it to text so it may be seen by the user.
  if (x.type === "password") {
    x.type = "text";
  }
  //If the input type is text, make it a password so it can be hidden.
  else {
    x.type = "password";
  }
}
//Show or hide business name input text
function showAddress_Business(input){
  //Get the selected value
  var x = input.options[input.selectedIndex].value;
  //Get the element with the location info
  var y = document.getElementById("location_info");
  //If user is a supplier, then business name is needed.
  if(x === "1")
  {
    y.style.display = "block";
  }
  else{
    y.style.display = "none";
  }
}

