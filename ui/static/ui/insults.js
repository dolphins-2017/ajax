var insultTemplate = '<li>{{insult}}</li>';

$(document).ready(function(){
	$.get('/api/', function(data){
		data['insults'].forEach(function(insult){
			$('#insultsList').append(Mustache.render(
				insultTemplate,
				{
					'insult': insult
				}
			));
		});
	});
});
