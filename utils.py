import difflib
import os
import random
import re

from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, FlexSendMessage, AudioSendMessage, QuickReplyButton, QuickReply, MessageAction

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from style_json import *

load_dotenv()
spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID", None)
spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET", None)
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret))


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

previewUrls = []
stateGuessSong_songName = ""

def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_text_message_with_QuickReply(reply_token, text, quickReplyList):
    quickReplyButtonList = []
    for replies in quickReplyList:
        quickReplyButtonList.append(QuickReplyButton(
                action=MessageAction(label=replies, text=replies)
            )
        )
    message = TextSendMessage(text=text, quick_reply=QuickReply(
        items=quickReplyButtonList
    ))
    line_bot_api.reply_message(reply_token, message)

    return "OK"

    
def push_text_message(id, text):
    line_bot_api.push_message(id, TextSendMessage(text=text))

def send_SearchMenu_message(id, query):
    message = createSearchMenu()
    message = updateSearchMenu(message, query)
    line_bot_api.reply_message(id, message)

    return "OK"

def send_SearchFinishedMenu_message(id):
    message = createSearchFinishedMenu()
    line_bot_api.push_message(id, message)
    
    return "OK"

def send_PickFinishedMenu_message(id):
    message = createSearchFinishedMenu()
    message.contents.body.contents[0].text = "抽取"
    message.contents.body.contents[1].text = "請選擇要繼續抽取或是返回主選單"
    message.contents.footer.contents[1].action.label = "繼續抽取"
    message.contents.footer.contents[1].action.text = "返回隨機選單"
    line_bot_api.push_message(id, message)
    
    return "OK"

def send_MainMenu_message(id):
    message = createMainMenu()
    line_bot_api.reply_message(id, message)
    
    return "OK"

def send_RandomMenu_message(id, query, score):
    message = createRandomMenu()
    message = updateSearchMenu(message, query)
    message = updateScore(message, score)
    line_bot_api.reply_message(id, message)

def send_image_url(id, img_url):
    message = ImageSendMessage(
        original_content_url = img_url,
        preview_image_url = img_url
    )
    line_bot_api.reply_message(id, message)
    
    return "OK"

def send_searchedResults_message(id, query, limit, searchType = 0):
    global previewUrls
    global stateGuessSong_songName
    q = query['Name']
    if len(query['Album'])!=0:  q+=" album:"+query['Album']
    if len(query['Artist'])!=0: q+=" artist:"+query['Artist']
    if len(query['Year'])!=0: q+=" year:"+query['Year']
    if len(query['Genre'])!=0: q+=" genre:"+query['Genre']

    results = {}
    
    results = sp.search(q,limit)

    if len(results['tracks']['items']) == 0:
        line_bot_api.reply_message(id, TextSendMessage(text='沒有找到相關結果，請更改條件再試一次'))
        return "ERROR"

    results_size = int(results['tracks']['total'])

    # Random
    if searchType == 1:
        results = sp.search(q, limit=1, offset=random.randrange(min(1000, results_size)))
    # Song-guessing game
    if searchType == 2:
        rand = random.randrange(min(300, results_size))
        results = sp.search(q, limit=1, offset=rand)
        stateGuessSong_songName = results['tracks']['items'][0]['name']
        previewUrls = [results['tracks']['items'][0]['preview_url']]
        print(rand,results['tracks']['items'][0]['artists'][0]['name'],stateGuessSong_songName)
        sendPreviewMessage(id, 0)
        return "OK"
    # Search conditions test
    if searchType == 3:
        return "OK"
        
    previewUrl = []
    img_urls = []
    track_names = []
    artists = []
    years = []
    track_uris = []

    for item in results['tracks']['items']:
        previewUrl = item['preview_url']
        img_url = item['album']['images'][0]['url'] 
        track_name = item['name']
        artist = [d['name'] for d in item['artists']]
        year = item['album']['release_date'][:4]
        track_uri = item['external_urls']['spotify']
        
        previewUrls.append(previewUrl)
        img_urls.append(img_url)
        track_names.append(track_name)
        artists.append(str(artist).replace("\'","").replace("[","").replace("]",""))
        years.append(year)
        track_uris.append(track_uri)
        
    tracks_message = trackListTitle()
    for (idx, img_url, track_name, artist, year, track_uri) in zip(range(1000), img_urls, track_names, artists, years, track_uris):
        tracks_message = addTrack(tracks_message, idx, img_url, track_name, artist, year, track_uri)
    
    line_bot_api.reply_message(id, tracks_message)
    
    return "OK"

def sendPreviewMessage(id, track_idx):
    line_bot_api.reply_message(id, AudioSendMessage(previewUrls[track_idx], 30000))
    
    return "OK"

def checkAnswer(text):
    text = re.sub(r'Version|Ver|ver|Live|[\(\)\ \']', '', text)
    ans = re.sub(r'Version|Ver|ver|Live|[\(\)\ \']', '', stateGuessSong_songName)
    text = text.lower()
    ans = ans.lower()
    seq = difflib.SequenceMatcher(None, text, ans)
    ratio = seq.ratio()
    seq = seq.find_longest_match(0, len(text), 0, len(ans))
    isAnswer = ratio>=0.8 or (ratio>=0.65 and seq.size == len(text) and seq.b == 0)
    if isAnswer:
        return True
    else:
        return False

def push_WrongAnswer_text_message(id, score):
    push_text_message(id, f'答錯了，答案是{stateGuessSong_songName}\n你的分數為:{score}')
    return "OK"
        
    
