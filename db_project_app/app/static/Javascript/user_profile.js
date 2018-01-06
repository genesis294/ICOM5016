// When the document has finished loading:
  $(document).ready(function(){
    
    var cur_id = sessionStorage.getItem("current_userid");
    if(cur_id == 0 || cur_id == null){
      setCurrentUserID($(".profile").attr("id"));
    }
});
