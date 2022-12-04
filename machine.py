from fsm import TocMachine

def create_machine():
    machine = TocMachine(
        states=["user", "stateMainMenu", "stateSearch", 
                'stateEnterName', 'stateEnterAlbum', 'stateEnterArtist',
                'stateEnterYear', 'stateEnterGenre',
                'stateEnterName_Random', 'stateEnterAlbum_Random', 'stateEnterArtist_Random',
                'stateEnterYear_Random', 'stateEnterGenre_Random', 
                'stateSearchCall', 'stateEnterSearchLimit', 'stateWaitPreview', 'stateSendPreview', 
                'stateRandom', 'statePickCall', 'stateGuessSong'],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "stateMainMenu",
                "conditions": "is_going_to_stateMainMenu",
            },
            {
                "trigger": "advance",
                "source": "stateMainMenu",
                "dest": "stateSearch",
                "conditions": "is_going_to_stateSearch",
            },
            {
                "trigger": "advance",
                "source": "stateSearch",
                "dest": "stateEnterName",
                "conditions": "is_going_to_stateEnterName",
            },
            {
                "trigger": "advance",
                "source": "stateSearch",
                "dest": "stateEnterAlbum",
                "conditions": "is_going_to_stateEnterAlbum",
            },
            {
                "trigger": "advance",
                "source": "stateSearch",
                "dest": "stateEnterArtist",
                "conditions": "is_going_to_stateEnterArtist",
            },
            {
                "trigger": "advance",
                "source": "stateSearch",
                "dest": "stateEnterYear",
                "conditions": "is_going_to_stateEnterYear",
            },
            {
                "trigger": "advance",
                "source": "stateSearch",
                "dest": "stateEnterGenre",
                "conditions": "is_going_to_stateEnterGenre",
            },
            {
                "trigger": "advance",
                "source": "stateRandom",
                "dest": "stateEnterName_Random",
                "conditions": "is_going_to_stateEnterName",
            },
            {
                "trigger": "advance",
                "source": "stateRandom",
                "dest": "stateEnterAlbum_Random",
                "conditions": "is_going_to_stateEnterAlbum",
            },
            {
                "trigger": "advance",
                "source": "stateRandom",
                "dest": "stateEnterArtist_Random",
                "conditions": "is_going_to_stateEnterArtist",
            },
            {
                "trigger": "advance",
                "source": "stateRandom",
                "dest": "stateEnterYear_Random",
                "conditions": "is_going_to_stateEnterYear",
            },
            {
                "trigger": "advance",
                "source": "stateRandom",
                "dest": "stateEnterGenre_Random",
                "conditions": "is_going_to_stateEnterGenre",
            },
            {
                "trigger": "advance",
                "source": "stateSearch",
                "dest": "stateEnterSearchLimit",
                "conditions": "is_going_to_stateEnterSearchLimit",
            },
            {
                "trigger": "advance",
                "source": "stateSearch",
                "dest": "stateSearchCall",
                "conditions": "is_going_to_stateSearchCall",
            },
            {
                "trigger": "go_stateWaitPreview",
                "source": ["stateSearchCall", "statePickCall", "stateSendPreview"],
                "dest": "stateWaitPreview",
            },
            {
                "trigger": "advance",
                "source": "stateWaitPreview",
                "dest": "stateSendPreview",
                "conditions": "isIndex",
            },
            {
                "trigger": "advance",
                "source": ["stateSearch", "stateSearchCall", "stateWaitPreview", "stateRandom"],
                "dest": "stateMainMenu",
                "conditions": "goMainMenu",
            },
            {
                "trigger": "advance",
                "source": ["stateSearchCall", "stateWaitPreview"],
                "dest": "stateSearch",
                "conditions": "goSearchMenu",
            },
            {
                "trigger": "advance",
                "source": ["statePickCall", "stateWaitPreview"],
                "dest": "stateRandom",
                "conditions": "goRandomMenu",
            },
            {
                "trigger": "advance",
                "source": 'stateSearch',
                "dest": "stateSearch",
                "conditions": "isQueryEmpty",
            },
            {
                "trigger": "advance",
                "source": 'stateRandom',
                "dest": "stateRandom",
                "conditions": "isQueryEmpty",
            },
            {
                "trigger": "advance",
                "source": 'stateSearch',
                "dest": "stateSearch",
                "conditions": "clearAll",
            },
            {
                "trigger": "advance",
                "source": 'stateRandom',
                "dest": "stateRandom",
                "conditions": "clearAll",
            },
            {
                "trigger": "advance",
                "source": "stateMainMenu",
                "dest": "stateRandom",
                "conditions": "is_going_to_stateRandom",
            },
            {
                "trigger": "advance",
                "source": "stateRandom",
                "dest": "statePickCall",
                "conditions": "is_going_to_statePickCall",
            },
            {
                "trigger": "advance",
                "source": "stateRandom",
                "dest": "stateGuessSong",
                "conditions": "is_going_to_stateGuessSong",
            },
            {
                "trigger": "advance",
                "source": "stateGuessSong",
                "dest": "stateGuessSong",
                "conditions": "guessRight",
            },
            {
                "trigger": "advance",
                "source": "stateGuessSong",
                "dest": "stateRandom",
                "conditions": "guessWrong",
            },
            {
                "trigger": "advance",
                "source": ['stateEnterName','stateEnterAlbum', 'stateEnterArtist','stateEnterYear', 'stateEnterGenre'],
                "dest": "stateSearch",
            },
            {
                "trigger": "advance",
                "source": ['stateEnterName_Random','stateEnterAlbum_Random', 'stateEnterArtist_Random','stateEnterYear_Random', 'stateEnterGenre_Random'],
                "dest": "stateRandom",
            },
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    
    return machine

