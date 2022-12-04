import os
from dotenv import load_dotenv
from transitions.extensions import GraphMachine

from utils import *

class TocMachine(GraphMachine):
    # Query for search
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.query = {
            'Name'      : "",
            'Album'     : "",
            'Artist'    : "",
            'Year'      : "",
            'Genre'    : "",
        }
        self.searchLimit = 5
        self.score = 0
        self.maxScore = 0
        
    def resetQuery(self):
        for key in self.query:
            self.query[key] = ""
    
    def is_going_to_stateMainMenu(self, event):
        return True
        
    def on_enter_stateMainMenu(self, event):
        reply_token = event.reply_token
        send_MainMenu_message(reply_token)
    
    def is_going_to_stateSearch(self, event):
        text = event.message.text
        return text == "搜尋"
    
    def on_enter_stateSearch(self, event):
        reply_token = event.reply_token
        send_SearchMenu_message(reply_token, self.query)
        
    '''
        Name
    '''
    def is_going_to_stateEnterName(self, event):
        text = event.message.text
        return text == "關鍵字輸入"
    
    def on_enter_stateEnterName(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Name']) != 0:
            quickReplyList.append(self.query['Name'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的歌曲關鍵字", quickReplyList)
        
    def on_exit_stateEnterName(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Name'] = text
        else:
            self.query['Name'] = ""

    def on_enter_stateEnterName_Random(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Name']) != 0:
            quickReplyList.append(self.query['Name'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的歌曲關鍵字", quickReplyList)
        
    def on_exit_stateEnterName_Random(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Name'] = text
        else:
            self.query['Name'] = ""
            
    '''
        Album
    '''
    def is_going_to_stateEnterAlbum(self, event):
        text = event.message.text
        return text == "專輯輸入"
    
    def on_enter_stateEnterAlbum(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Album']) != 0:
            quickReplyList.append(self.query['Album'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的專輯名字", quickReplyList)
        
    def on_exit_stateEnterAlbum(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Album'] = text
        else:
            self.query['Album'] = ""
    
    def on_enter_stateEnterAlbum_Random(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Album']) != 0:
            quickReplyList.append(self.query['Album'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的專輯名字", quickReplyList)
        
    def on_exit_stateEnterAlbum_Random(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Album'] = text
        else:
            self.query['Album'] = ""
    
    '''
        Artist
    '''
    def is_going_to_stateEnterArtist(self, event):
        text = event.message.text
        return text == "作者輸入"
    
    def on_enter_stateEnterArtist(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Artist']) != 0:
            quickReplyList.append(self.query['Artist'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的作者名字", quickReplyList)
        
    def on_exit_stateEnterArtist(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Artist'] = text
        else:
            self.query['Artist'] = ""
    
    def on_enter_stateEnterArtist_Random(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Artist']) != 0:
            quickReplyList.append(self.query['Artist'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的作者名字", quickReplyList)
        
    def on_exit_stateEnterArtist_Random(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Artist'] = text
        else:
            self.query['Artist'] = ""
    
    '''
        Year
    '''
    def is_going_to_stateEnterYear(self, event):
        text = event.message.text
        return text == "年份輸入"
    
    def on_enter_stateEnterYear(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Year']) != 0:
            quickReplyList.append(self.query['Year'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的年份", quickReplyList)
        
    def on_exit_stateEnterYear(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Year'] = text
        else:
            self.query['Year'] = ""
    
    def on_enter_stateEnterYear_Random(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Year']) != 0:
            quickReplyList.append(self.query['Year'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的年份", quickReplyList)
        
    def on_exit_stateEnterYear_Random(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Year'] = text
        else:
            self.query['Year'] = ""
    
    '''
        Genre
    '''
    def is_going_to_stateEnterGenre(self, event):
        text = event.message.text
        return text == "風格輸入"
    
    def on_enter_stateEnterGenre(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件']
        if len(self.query['Genre']) != 0:
            quickReplyList.append(self.query['Genre'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的風格", quickReplyList)
        
    def on_exit_stateEnterGenre(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Genre'] = text
        else:
            self.query['Genre'] = ""

    def on_enter_stateEnterGenre_Random(self, event):
        reply_token = event.reply_token
        quickReplyList = ['清除條件','pop', 'rap', 'k-pop', 'k-pop-girl-group', 'taiwan-pop','taiwan-hip-hop', 'mandopop', 'j-pop', 'anime']
        if len(self.query['Genre']) != 0:
            quickReplyList.append(self.query['Genre'])
        send_text_message_with_QuickReply(reply_token, "請輸入所要搜尋的風格", quickReplyList)
        
    def on_exit_stateEnterGenre_Random(self, event):
        text = event.message.text
        if text != "清除條件":
            self.query['Genre'] = text
        else:
            self.query['Genre'] = ""

    
    def is_going_to_stateSearchCall(self, event):
        text = event.message.text
        flag = False
        for key in self.query:
            if len(self.query[key]) != 0:
                flag = True
                break
        return text == "開始搜尋" and flag
    
    def on_enter_stateSearchCall(self, event):
        reply_token = event.reply_token
        send_searchedResults_message(reply_token, self.query, self.searchLimit)
        user_id = event.source.user_id
        send_SearchFinishedMenu_message(user_id)
        self.go_stateWaitPreview()
            
    def on_enter_stateSendPreview(self, event):
        text = event.message.text
        reply_token = event.reply_token
        try:
            track_id = int(text)
            sendPreviewMessage(reply_token, track_id)
        except:
            send_text_message(reply_token, "請輸入範圍內整數")
        self.go_stateWaitPreview()
    
    def isIndex(self, event):
        text = event.message.text
        try:
            track_id = int(text)
            return True
        except:
            return False

    def isQueryEmpty(self, event):
        text = event.message.text
        if text == "清除所有條件":
            return False
        user_id = event.source.user_id
        flag = False
        for key in self.query:
            if len(self.query[key]) != 0:
                flag = True
                break
        if flag is False:
            push_text_message(user_id, "請輸入至少一項條件")
            return True
        return False
    
    def clearAll(self, event):
        flag = False
        text = event.message.text
        if text == "清除所有條件":
            flag = True
            for key in self.query:
                self.query[key] = ""
        return flag
        
    def goSearchMenu(self, event):
        text = event.message.text
        return text == "返回搜尋選單"
    
    def goMainMenu(self, event):
        text = event.message.text
        return text == "返回主選單"
    
    def goRandomMenu(self, event):
        text = event.message.text
        return text == "返回隨機選單"
    
    def is_going_to_stateRandom(self, event):
        text = event.message.text
        return text == "隨機歌曲"
    
    def on_enter_stateRandom(self, event):
        self.maxScore = max(self.maxScore, self.score)
        self.score = 0
        reply_token = event.reply_token
        send_RandomMenu_message(reply_token, self.query, self.maxScore)
        
    def is_going_to_statePickCall(self, event):
        text = event.message.text
        flag = False
        for key in self.query:
            if len(self.query[key]) != 0:
                flag = True
                break
        return text == "抽歌" and flag
        
    def on_enter_statePickCall(self, event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        send_searchedResults_message(reply_token, self.query, 50, 1)
        send_PickFinishedMenu_message(user_id)
        self.go_stateWaitPreview()
        
    def is_going_to_stateGuessSong(self, event):
        text = event.message.text
        flag = False
        for key in self.query:
            if len(self.query[key]) != 0:
                flag = True
                break
        if send_searchedResults_message("", self.query, 1, 3) == "ERROR":
            flag = False
        return text == "猜歌" and flag
    
    def on_enter_stateGuessSong(self, event):
        reply_token = event.reply_token
        send_searchedResults_message(reply_token, self.query, 50, 2)
        
    def guessRight(self, event):
        text = event.message.text
        if checkAnswer(text) is True:
            self.score += 1
            return True
        return False
    
    def guessWrong(self, event):
        user_id = event.source.user_id
        text = event.message.text
        if checkAnswer(text) is False:
            push_WrongAnswer_text_message(user_id, self.score)
            return True
        return False