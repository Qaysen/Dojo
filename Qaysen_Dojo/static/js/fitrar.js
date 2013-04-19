$(function(){

	filtro = {
		categorias: []
		lugares: []
	}
	$(".filtro").on("change"){
		if($(this).hasClass('filtro-cat'))
		{
			filtro.categorias.push($(this).)
		}
		else if($(this).hasClass('filtro-lugar'))
		{
			filtro.lugar.push('')
		}
	}

});