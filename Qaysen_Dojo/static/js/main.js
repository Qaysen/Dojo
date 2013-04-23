$(document).on("ready", inicio);
$(document).on("ready", setup);
function setup(){
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    function getCookie(name) {
      var cookieValue = null;
        if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
                }
            }
        }
    return cookieValue;
    }
    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
  // Only send the token to relative URLs i.e. locally.
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
  }
});
}
function inicio()
{
    $("article").on("mouseover", mostrar);
    $("article").on("mouseout", esconder);
    $(".login").on("click", login);
    $(".x_cerrar").on("click", nav);
    $(".inscribete").on("click", inscribete);
}
function mostrar()
{
    $(this).find("h3").addClass("slide_up");
    $(this).find("p").css("z-index", "75");
}
function esconder()
{
    $(this).find("h3").removeClass("slide_up");
    $(this).find("p").css("z-index","0");
}
function login()
{
	$("nav ul").hide();
	$("form").show();
	$(".x_cerrar").show();
}
function nav()
{
	$("nav ul").show();
	$("form").hide();
	$(".x_cerrar").hide();
}
function inscribete()
{
    id = $(this).parent().children('.span4').find('input').val();
    console.log(id);
    $.ajax(
    {
        data: {'id':id},
        type: "POST",
        url: "/inscribirse/",
        success: function(data)
        {
            console.log(data);
        }
    });
}