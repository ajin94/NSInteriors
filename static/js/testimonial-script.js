$(document).ready(function(){
     $("#submit_query_button").click(function(){
        if (is_valid_inputs()){
             $.ajax({
                type:'post',
                url:$SCRIPT_ROOT + '/_add_query',
                data:$('#query_form').serialize(),
                dataType:'json',
                success:function(response){
                    if (response.status == "OK"){
                        $("#query_form").trigger("reset");
                        $("#query_send_modal").modal();
                    }else{
                        $("#query_form").trigger("reset");
                        location.reload();
                    }
                },
                error:function(response){
                  console.log("Error ! Try again after a while.");
                }
            });
        }
     });
});


function is_valid_inputs(){
    var is_valid_form = true;
    var name = $("#name").val();
    var email = $("#email").val();
    var query = $("#query").val();
    var email_regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

    if (name.trim() == "" || /\d/.test(name) ){
        is_valid_form = false;
        $('#invalid_name').show();
    }else{
        $('#invalid_name').hide();
    }

    if (email.trim() == "" || ! email_regex.test(email) ){
        is_valid_form = false;
        $('#invalid_email').show();
    }else{
        $('#invalid_email').hide();
    }

    if (query.trim() == ""){
        is_valid_form = false;
        $('#invalid_query').show();
    }else if (query.length < 20){
        is_valid_form = false;
        $('#invalid_query').text("Query should contain minimum 20 characters");
        $('#invalid_query').show();
    }else{
        $('#invalid_query').hide();
    }
    return is_valid_form;
}