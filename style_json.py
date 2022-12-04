from linebot.models import FlexSendMessage, BoxComponent, SeparatorComponent, TextComponent

def trackListTitle():
    message = FlexSendMessage(
        alt_text='Music Found',
        contents=
        {
            "type": "bubble",
            "size": "giga",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/ILoVtlG.png",
                    "size": "sm",
                    "aspectRatio": "2:1",
                    "align": "center"
                },
                {
                    "type": "separator"
                }
                ],
                "paddingAll": "none"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "paddingAll": "none"
            },
            "styles": {
                "header": {
                "backgroundColor": "#191414"
                },
                "body": {
                "backgroundColor": "#191414"
                }
            }
        }
    )
    return message

def addTrack(message, idx, img_url, track_name, artist, year, track_uri):
    message.contents.body.contents.append(
        {
            "type": "box",
            "layout": "horizontal",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": img_url,
                    "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": track_uri
                    }
                }
                ],
                "paddingAll": "none",
                "width": "100px",
                "height": "100px",
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": track_name,
                    "size": "xxl",
                    "weight": "bold",
                    "color": "#1DB954",
                    "adjustMode": "shrink-to-fit"
                },
                {
                    "type": "text",
                    "text": artist,
                    "color": "#00ffff",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": year,
                    "offsetTop": "lg"
                }
                ],
                "margin": "md"
            },
            {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "image",
                    "url": "https://i.imgur.com/T8AikEh.png",
                    "action": {
                    "type": "message",
                    "label": str(idx),
                    "text": str(idx)
                    },
                    "aspectMode": "fit",
                    "aspectRatio": "1:1"
                }
                ],
                "paddingAll": "none",
                "width": "70px",
                "height": "70px",
                "offsetTop": "xl"
            }
            ],
            "margin": "lg",
            "paddingStart": "xs"
        },
    )
    message.contents.body.contents.append(
        {
            "type": "separator",
            "margin": "lg"
        } 
    )
    
    return message

def createSearchMenu():
    message = FlexSendMessage(
        alt_text="搜尋選單",
        contents=
        {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                    "size": "full",
                    "aspectRatio": "20:13"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "搜尋",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "text",
                        "text": "請選擇要開始搜尋或是返回主選單"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "關鍵字:",
                                "weight": "bold",
                                "flex": 2
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 7
                            }
                            ],
                            "paddingStart": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "專輯:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 5
                            }
                            ],
                            "paddingStart": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "作者:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 5
                            }
                            ],
                            "paddingStart": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "年份:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 5
                            }
                            ],
                            "paddingStart": "xxl"
                        },
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "text",
                                "text": "風格:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "無",
                                "flex": 5
                            }
                            ],
                            "paddingStart": "xxl"
                        }
                        ],
                        "paddingTop": "md"
                    }
                    ],
                    "paddingAll": "md"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "開始搜尋",
                        "text": "開始搜尋"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "清除所有條件",
                        "text": "清除所有條件"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "返回主選單",
                        "text": "返回主選單"
                        }
                    }
                    ],
                    "paddingAll": "none"
                }
                },
                {
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                    "size": "full",
                    "aspectRatio": "20:13"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "條件",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "text",
                        "text": "更改條件"
                    }
                    ],
                    "paddingAll": "md"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "關鍵字",
                        "text": "關鍵字輸入"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "專輯",
                        "text": "專輯輸入"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "作者",
                        "text": "作者輸入"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "年份",
                        "text": "年份輸入"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "風格",
                        "text": "風格輸入"
                        }
                    }
                    ],
                    "paddingAll": "none"
                }
                }
            ]
        }
    )
    return message

def updateSearchMenu(message, query):
    item = message.contents.contents[0].body.contents[2]
    name = query['Name']
    item.contents[0].contents[1].text = name
    if name == "":
        item.contents[0].contents[1].text = "無"

    album = query['Album']
    item.contents[1].contents[1].text = album
    if album == "":
        item.contents[1].contents[1].text = "無"

    artist = query['Artist']
    item.contents[2].contents[1].text = artist
    if artist == "":
        item.contents[2].contents[1].text = "無"

    year = query['Year']
    item.contents[3].contents[1].text = year
    if year == "":
        item.contents[3].contents[1].text = "無"

    genre = query['Genre']
    item.contents[4].contents[1].text = genre
    if genre == "":
        item.contents[4].contents[1].text = "無"

    return message 

def updateScore(message, score):
    item = message.contents.contents[0].body.contents[2]
    item.contents[5].contents[1].text = str(score)
    
    return message

def createSearchFinishedMenu():
    message = FlexSendMessage(
        alt_text='搜尋完畢',
        contents=
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "搜尋",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "請選擇要繼續搜尋或是返回主選單"
                }
                ],
                "paddingAll": "md"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "繼續搜尋",
                    "text": "返回搜尋選單"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "返回主選單",
                    "text": "返回主選單"
                    }
                }
                ],
                "paddingAll": "none"
            }
        }
    )
    return message
def createMainMenu():
    message = FlexSendMessage(
        alt_text='主選單',
        contents=
        {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "功能選擇",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "請選擇要搜尋歌曲或是提供隨機歌曲"
                }
                ],
                "paddingAll": "md"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "搜尋",
                    "text": "搜尋"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "隨機歌曲",
                    "text": "隨機歌曲"
                    }
                }
                ],
                "paddingAll": "none"
            }
        }
    )
    return message
    
def createRandomMenu():
    message = FlexSendMessage(
        alt_text="隨機主選單",
        contents=
        {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "隨機歌曲",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "請選擇要抽/猜歌或是返回主選單"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "關鍵字:",
                            "weight": "bold",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": "無",
                            "flex": 7
                        }
                        ],
                        "paddingStart": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "專輯:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "無",
                            "flex": 5
                        }
                        ],
                        "paddingStart": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "作者:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "無",
                            "flex": 5
                        }
                        ],
                        "paddingStart": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "年份:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "無",
                            "flex": 5
                        }
                        ],
                        "paddingStart": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "風格:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "無",
                            "flex": 5
                        }
                        ],
                        "paddingStart": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "text",
                            "text": "最高分數:",
                            "weight": "bold",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": "0",
                            "flex": 5
                        }
                        ],
                        "paddingStart": "xxl"
                    }
                    ],
                    "paddingTop": "md"
                }
                ],
                "paddingAll": "md"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "抽歌",
                    "text": "抽歌"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "猜歌",
                    "text": "猜歌"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "清除所有條件",
                    "text": "清除所有條件"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "返回主選單",
                    "text": "返回主選單"
                    }
                }
                ],
                "paddingAll": "none"
            }
            },
            {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                "size": "full",
                "aspectRatio": "20:13"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "條件",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "更改條件"
                }
                ],
                "paddingAll": "md"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "關鍵字",
                    "text": "關鍵字輸入"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "專輯",
                    "text": "專輯輸入"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "作者",
                    "text": "作者輸入"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "年份",
                    "text": "年份輸入"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "風格",
                    "text": "風格輸入"
                    }
                }
                ],
                "paddingAll": "none"
            }
            }
        ]
        }
    )
    return message