import facebook
from keys import keys
#x = post id such that it is posted on your wall on your birthday
post = graph.get_objects(id='post_id')
q = ['Happy Birthday!',
	 'Happy Birthday', 
	  'Happy Bday!',
	  'HBD!',
	  'HBD',
	  'Happy Bday'
	  ]

for i in q:
if post.message == q:
graph.put_object(parent_object='post_id', connection_name='comments', message='Thank You!')
graph.put_like(object_id='post_id')	  