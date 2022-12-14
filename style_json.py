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
        alt_text="????????????",
        contents=
        {
            "type": "carousel",
            "contents": [
                {
                "type": "bubble",
                # "hero": {
                #     "type": "image",
                #     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                #     "size": "full",
                #     "aspectRatio": "20:13"
                # },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "??????",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "text",
                        "text": "?????????????????????????????????????????????"
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
                                "text": "?????????:",
                                "weight": "bold",
                                "flex": 2
                            },
                            {
                                "type": "text",
                                "text": "???",
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
                                "text": "??????:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "???",
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
                                "text": "??????:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "???",
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
                                "text": "??????:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "???",
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
                                "text": "??????:",
                                "weight": "bold",
                                "flex": 1
                            },
                            {
                                "type": "text",
                                "text": "???",
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
                        "label": "????????????",
                        "text": "????????????"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "??????????????????",
                        "text": "??????????????????"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "???????????????",
                        "text": "???????????????"
                        }
                    }
                    ],
                    "paddingAll": "none"
                }
                },
                {
                "type": "bubble",
                # "hero": {
                #     "type": "image",
                #     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
                #     "size": "full",
                #     "aspectRatio": "20:13"
                # },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "??????",
                        "weight": "bold",
                        "size": "lg"
                    },
                    {
                        "type": "text",
                        "text": "????????????"
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
                        "label": "?????????",
                        "text": "???????????????"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "??????",
                        "text": "????????????"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "??????",
                        "text": "????????????"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "??????",
                        "text": "????????????"
                        }
                    },
                    {
                        "type": "separator"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "??????",
                        "text": "????????????"
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
        item.contents[0].contents[1].text = "???"

    album = query['Album']
    item.contents[1].contents[1].text = album
    if album == "":
        item.contents[1].contents[1].text = "???"

    artist = query['Artist']
    item.contents[2].contents[1].text = artist
    if artist == "":
        item.contents[2].contents[1].text = "???"

    year = query['Year']
    item.contents[3].contents[1].text = year
    if year == "":
        item.contents[3].contents[1].text = "???"

    genre = query['Genre']
    item.contents[4].contents[1].text = genre
    if genre == "":
        item.contents[4].contents[1].text = "???"

    return message 

def updateScore(message, score):
    item = message.contents.contents[0].body.contents[2]
    item.contents[5].contents[1].text = str(score)
    
    return message

def createSearchFinishedMenu():
    message = FlexSendMessage(
        alt_text='????????????',
        contents=
        {
            "type": "bubble",
            # "hero": {
            #     "type": "image",
            #     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            #     "size": "full",
            #     "aspectRatio": "20:13"
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "??????",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "?????????????????????????????????????????????"
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
                    "label": "????????????",
                    "text": "??????????????????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "???????????????",
                    "text": "???????????????"
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
        alt_text='?????????',
        contents=
        {
            "type": "bubble",
            # "hero": {
            #     "type": "image",
            #     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            #     "size": "full",
            #     "aspectRatio": "20:13"
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "????????????",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "????????????????????????????????????????????????"
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
                    "label": "??????",
                    "text": "??????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "????????????",
                    "text": "????????????"
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
        alt_text="???????????????",
        contents=
        {
        "type": "carousel",
        "contents": [
            {
            "type": "bubble",
            # "hero": {
            #     "type": "image",
            #     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            #     "size": "full",
            #     "aspectRatio": "20:13"
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "????????????",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "???????????????/???????????????????????????"
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
                            "text": "?????????:",
                            "weight": "bold",
                            "flex": 2
                        },
                        {
                            "type": "text",
                            "text": "???",
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
                            "text": "??????:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "???",
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
                            "text": "??????:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "???",
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
                            "text": "??????:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "???",
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
                            "text": "??????:",
                            "weight": "bold",
                            "flex": 1
                        },
                        {
                            "type": "text",
                            "text": "???",
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
                            "text": "????????????:",
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
                    "label": "??????",
                    "text": "??????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "??????",
                    "text": "??????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "??????????????????",
                    "text": "??????????????????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "???????????????",
                    "text": "???????????????"
                    }
                }
                ],
                "paddingAll": "none"
            }
            },
            {
            "type": "bubble",
            # "hero": {
            #     "type": "image",
            #     "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
            #     "size": "full",
            #     "aspectRatio": "20:13"
            # },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "??????",
                    "weight": "bold",
                    "size": "lg"
                },
                {
                    "type": "text",
                    "text": "????????????"
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
                    "label": "?????????",
                    "text": "???????????????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "??????",
                    "text": "????????????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "??????",
                    "text": "????????????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "??????",
                    "text": "????????????"
                    }
                },
                {
                    "type": "separator"
                },
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "??????",
                    "text": "????????????"
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