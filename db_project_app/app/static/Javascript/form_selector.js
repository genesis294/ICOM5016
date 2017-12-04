var prev_open_form = document.getElementById("water_form");
//Shows the form depending on the selected product type
function showRestOfForm(input){
  //Hid previous elements
  prev_open_form.style.display = "none";
  //Get the selected element. Used to determine which form to show.
  var selected_value = input.options[input.selectedIndex].value;
  //Variable holds the forms name
  var form_name = selected_value+"_form";
  //Variable that holds the elements that must be shown
  var show = document.getElementById(form_name);
  //Save new previous form
  prev_open_form=show;
  //Shows the appropriate element
  show.style.display = "block";
}
