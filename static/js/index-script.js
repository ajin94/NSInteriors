$(document).ready(function(){
     $("#submit_comment_button").click(function(){
        if (is_valid_inputs()){
             $.ajax({
                type:'post',
                url:$SCRIPT_ROOT + '/_add_comment',
                data:$('#comment_form').serialize(),
                dataType:'json',
                success:function(response){
                    if (response.status == "OK"){
                        $("#comment_form").trigger("reset");
                        $("#comment_send_modal").modal();
                    }else{
                        $("#comment_form").trigger("reset");
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
    var comment = $("#comment").val();
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

    if (comment.trim() == ""){
        is_valid_form = false;
        $('#invalid_comment').show();
    }else if (comment.length < 30){
        is_valid_form = false;
        $('#invalid_comment').text("Comment should contain minimum 30 characters");
        $('#invalid_comment').show();
    }else{
        $('#invalid_comment').hide();
    }
    return is_valid_form;
}