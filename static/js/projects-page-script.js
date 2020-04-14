$(document).ready(function(){

    $(".open-image").click(function(){
        $("#image-popup-modal").show();
        var source_root = $(this).attr('src');
        $(".image-open-modal-content").attr("src",".."+source_root);
    });

    $(".image-open-close").click(function(){
        $("#image-popup-modal").hide();
    });

});
