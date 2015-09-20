$(document).ready(function(){
    $("#coursedetails").hide();
    $("#courses").change(function(){
        $("#coursedetails").show();
    });
    
    $("a.learn.btn.register").click(function(){
        $(".9mon").append("CSC236"); 
        $(".9tue").append("CSC236"); 
        $(".9wed").append("CSC236"); 
        $(".9thu").append("CSC236"); 
        $(".9fri").append("CSC236"); 
    });
    
});