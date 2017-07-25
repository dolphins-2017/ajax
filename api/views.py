from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
import random

insults = [
	"If laughter is the best medicine, your face must be curing the world.",
	"You're so ugly, you scared the crap out of the toilet.",
	"Your family tree must be a cactus because everybody on it is a prick.",
	"No I'm not insulting you, I'm describing you.",
	"It's better to let someone think you are an Idiot than to open your mouth and prove it.",
	"If I had a face like yours, I'd sue my parents.",
	"Your birth certificate is an apology letter from the condom factory.",
	"I guess you prove that even god makes mistakes sometimes.",
	"The only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
	"You're so fake, Barbie is jealous.",
	"I’m jealous of people that don’t know you!",
	"My psychiatrist told me I was crazy and I said I want a second opinion. He said okay, you're ugly too.",
	"You're so ugly, when your mom dropped you off at school she got a fine for littering.",
	"If I wanted to kill myself I'd climb your ego and jump to your IQ.",
	"You must have been born on a highway because that's where most accidents happen.",
	"Brains aren't everything. In your case they're nothing.",
	"I don't know what makes you so stupid, but it really works.",
	"I can explain it to you, but I can’t understand it for you.",
	"Roses are red violets are blue, God made me pretty, what happened to you?",
	"Behind every fat woman there is a beautiful woman. No seriously, your in the way.",
	"Calling you an idiot would be an insult to all the stupid people.",
	"You, sir, are an oxygen thief!",
	"Some babies were dropped on their heads but you were clearly thrown at a wall.",
	"Don't like my sarcasm, well I don't like your stupid.",
	"Why don't you go play in traffic.",
	"Please shut your mouth when you’re talking to me.",
	"I'd slap you, but that would be animal abuse.",
	"They say opposites attract. I hope you meet someone who is good-looking, intelligent, and cultured.",
	"Stop trying to be a smart ass, you're just an ass.",
	"The last time I saw something like you, I flushed it.",
	"'m busy now. Can I ignore you some other time?",
	"You have Diarrhea of the mouth; constipation of the ideas.",
	"If ugly were a crime, you'd get a life sentence.",
	"Your mind is on vacation but your mouth is working overtime.",
	"I can lose weight, but you’ll always be ugly.",
	"Why don't you slip into something more comfortable... like a coma.",
	"Shock me, say something intelligent.",
	"If your gonna be two faced, honey at least make one of them pretty.",
	"Keep rolling your eyes, perhaps you'll find a brain back there.",
]

class Index(View):
	def get(self, request):
		res = {
			'count': len(insults),
			'insults': insults
		}

		return JsonResponse(res)

	def post(self, request):
		data = json.loads(request.body.decode())
		if data['say'].isupper():
			res = {
				'says': random.choice(insults)
			}
		else:
			res = {
				'says': 'I cant hear you!'
			}

		return JsonResponse(res)
