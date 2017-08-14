get_comments = function() { 
	$.ajax({ 
		url: '/api/engagement/v1/comments/' + 'some id'  + '/', 
		success: function(response) { 
			$('comment-modal modal-content').html(response)
			$('comment-modal').modal('open');
		},
		failure: function() { 

		}
	});
};