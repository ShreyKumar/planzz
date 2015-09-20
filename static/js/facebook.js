$(document).ready(function(){
//global vars
var friends = [];

window.fbAsyncInit = function() {
    FB.init({
    appId      : '507349916095512',
    xfbml      : true,
    version    : 'v2.4'
    });

    FB.login(function(response) {
        // handle the response
        FB.api(
            "/me/taggable_friends",
            function (response) {
                if (response && !response.error) {
                    /* handle the result */
                    console.log(response.data);
                    friends = response.data;
                    for(var i = 0; i < friends.length; i++){
                        var extra = "";
                        if(i == 0){
                            extra = "In your CSC236 class";
                        } else if(i == 1){
                            extra = "In your CSC209 class";
                        } else if(i == 2){
                            extra = "In your CSC343, MAT235 and PHL100 class";
                        } else {
                            extra = "In none of your classes";   
                        }
                        var row = "<tr>" + 
                        "<td><img src='" + friends[i].picture.data.url + "' /></td>" + 
                        "<td>" + friends[i].name + "<br>" + extra + "</td>" +
                        "</tr>";
                        
                        $("#friendlist").append(row);
                    }
                }
            }
        );
    }, {scope: 'user_friends'});

};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));


});
