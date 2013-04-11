$(document).on("ready", inicio);
function inicio()
{
    $("article").on("mouseover", mostrar);
    $("article").on("mouseout", esconder);
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
