$(document).on("ready", inicio);
function inicio()
{
    $("article").on("mouseover", mostrar);
    $("article").on("mouseout", esconder);
    $(".login").on("click", login);
    $(".x_cerrar").on("click", nav);
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
	$("nav form").show();
	$(".x_cerrar").show();
}
function nav()
{
	$("nav ul").show();
	$("nav form").hide();
	$(".x_cerrar").hide();
}