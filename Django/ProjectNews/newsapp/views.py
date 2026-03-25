from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'newsapp/home.html')

def sports(request):
    news = {'msg1' : "South Africa secured a 3-2 T20I series win over New Zealand with a 33-run victory today. Meanwhile, the IPL reached new financial heights as RCB and Rajasthan Royals were sold in deals totaling over $3.4 billion",
            'msg2':"Coco Gauff battles into the semifinals after a 3-set win over Belinda Bencic. Jannik Sinner</strong> cruises into the quarterfinals to face Frances Tiafoe.",
            'msg3':"The Khelo India Tribal Games officially opened in Chhattisgarh, and Baranica Elangovan shattered the national pole vault record in Bhubaneswar.",
        "type" : 'sports'}
    context = {"news" : news}
    return render(request,'newsapp/news.html', context)

def business(request):
    news = {'msg1' : "South Africa secured a 3-2 T20I series win over New Zealand with a 33-run victory today. Meanwhile, the IPL reached new financial heights as RCB and Rajasthan Royals were sold in deals totaling over <>$3.4 billion",
            'msg2':"The Sensex surged over 1,200 points today, closing at 75,273, while the Nifty 50 reclaimed the 23,300 level. This 1.7 ally was fueled by easing geopolitical tensions in the Middle East.",
            'msg3': "Aditya Birla Group led a consortium to acquire the RCB IPL team for $1.8 billion. Meanwhile, L&T shares rose 4% following a major water management contract win in Assam.",
            "type" : 'business'}
    context = {"news" : news}
    return render(request,'newsapp/news.html', context)

def entertainment(request):
    news = {
        'msg1' : "The tragic connection between Obito Uchiha and Rin Nohara remains one of the most debated topics in Naruto Shippuden. Obito’s descent into darkness was triggered by witnessing Rin’s death at the hands of Kakashi, leading him to declare the world a 'hell' and initiate the <Rin>Infinite Tsukuyomi",
        'msg2': "The Sacrifice: Rin chose to die by Kakashi's Chidori to protect the Hidden Leaf from the Three-Tails (Isobu) sealed within her.",
        'msg3':"A popular theory suggests that Madara Uchiha specifically orchestrated Rin's death to manipulate Obito’s Rinnegan awakening and ensure his absolute loyalty to the Akatsuki’s true mission.",
        "type" : 'entertainment'}
    context = {"news" : news}
    return render(request,'newsapp/news.html', context)