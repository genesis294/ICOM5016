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
//Show or hide address input text
function showAddress(input){
  //Get the selected value
  var x = input.options[input.selectedIndex].value;
  //Get the element with the location info
  var y = document.getElementById("location_info");
  //If user is a administrator then address is not needed.
  if(x === "2")
  {
    y.style.display = "none";

  }
  //If user is person in need or supplier then ask for address
  else{
    y.style.display = "block";

  }
}
