import webbrowser
import os
import platform

def clearConsole():
    print(platform.system())
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux" or "Darwin":
        os.system('clear')
    else:
        pass

def getFilename():
    filename = input("Input filename ")
    return filename

#def getFiletype():
    #filetype = input("Input filetype (all lower case) ")
    #return filetype

def getArtist():
    artist = input("Input artist name (use - for space) ")
    return artist

def getID():
    id = input("Input artwork / post id ")
    return id
    
def twitter():
    purl = "https://pbs.twimg.com/media/"
    aurl = "?format=jpg&name=large"
    furl = purl + getFilename() + aurl
    return furl

def pixiv():
    purl = "https://www.pixiv.net/artworks/"
    furl = purl + getID()
    return furl
    
def danboorua():
    purl = "https://danbooru.donmai.us/posts?tags="
    furl = purl + getArtist()
    return furl
    
def danbooruf():
    purl = "https://cdn.donmai.us/original/"
    file = getID()
    fname = file[:-32]
    fname1 = fname[:-2]
    fname2 = fname[-2:]
    furl = purl + fname1 + "/" + fname2 + "/" + file
    return furl
    
def yandere():
    purl = "https://yande.re/post/show/"
    furl = purl + getID()
    return furl

def konachan():
    purl = "https://konachan.com/post/show/"
    furl = purl + getID()
    return furl

def sankaku():
    purl = "https://chan.sankakucomplex.com/?tags=md5%3A"
    aurl = "&commit=Search"
    furl = purl + getFilename() + aurl
    return furl

def flyingmilktea():
    purl = "https://www.flyingmilktea.com/name-of-artwork/?id="
    furl = purl + getID()
    return furl

def help():
    clearConsole()
    print("How to use:\n1. twitter (filename, eg. FQ3NzFyaIAAwyDl.jpg -> FQ3NzFyaIAAwyDl)\n\n2. pixiv (post id, eg. 93491586_p0.jpg -> 93491586)\n\n3. danbooru (type artist name, use - for space)\n\n4. danbooru (post id + extension, eg. __original_dr...on__0398cf338db827ead53feef2021621dc.jpg -> 0398cf338db827ead53feef2021621dc.jpg)\n\n5. yande.re (post id, eg. yande.re 597438 ... -> 597438)\n\n6. konachan.com (post id, eg. Konachan.com - 329010 2gi...gs.jpg -> 329010)\n\n7. Sankaku Channel (filename, eg. 05c5963de7c558b62516d4c98ca1dac0.jpg -> 05c5963de7c558b62516d4c98ca1dac0)\n\n8. Flying Milk Tea (artwork ID, eg. 644896923)")
    waitForReturn = input("Hit Enter/Return to return to main menu")

def start():
    mode = input("\nMain Menu:\n1. Twitter\n\n2. Pixiv\n\n3. Danbooru (search by artist)\n\n4. Danbooru (post id + extension)\n\n5. yande.re\n\n6. konachan.com\n\n7. Sankaku Channel\n\n8. Flying Milk Tea (飛天奶茶)\n\n9. How to use\n\nInput Option: ")
    if mode == "1":
        webbrowser.open(twitter())
    elif mode == "2":
        webbrowser.open(pixiv())
    elif mode == "3":
        webbrowser.open(danboorua())
    elif mode == "4":
        webbrowser.open(danbooruf())
    elif mode == "5":
        webbrowser.open(yandere())
    elif mode == "6":
        webbrowser.open(konachan())
    elif mode == "7":
        webbrowser.open(sankaku())
    elif mode == "8":
        webbrowser.open(flyingmilktea())
    elif mode == "9":
        help()
    clearConsole()
    start()
        
start()
    