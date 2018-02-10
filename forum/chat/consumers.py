import json
from urllib import parse

from channels import Group
from channels.seesion import channel_session

@channel_session
def ws_echo(message):
    if 'username' not in message.channel_session:
        return
    room = message.channel_session['room']
    Group('chat-%s' % room).send({
        'text': json.dumps({
            'message': message.content['text'],
            'username': message.channel_session['username']
        }),
    })


@channel_session
def ws_add(message,room):
	query=parse.parse_qs(message['query_string'])
	if 'username' not in query:
		return
	Group('chat-%s'%room).add(message.reply_channel)
	message.channel_session['room']=room
	message.channel_session['username']=query['username'][0]
	
