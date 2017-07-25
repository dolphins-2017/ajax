$(document).ready(function() {
	$('#grandpaForm').on('keyup', function(event){
		event.preventDefault()
		var sayed = $('input[name="sayToGrandpa"]').val();
""
		$.post({
			url: '/api/',
			data: JSON.stringify({
				'say': sayed
			}),
			success: function(data){
				$('#resGrandpa').text(data['says'])
			}
		});
	});
});
