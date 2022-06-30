# ArtworkReverseSearch
A tool for searching the source of an artwork just by using the downloaded file name. You need to know where the file was downloaded first. Since this is searching with the filename or post id, unlike saucenao, it doesn't work with something like unknown.png or IMG_XXXX.jpg.
This was inspired after I accidentally corrupted my files. I only have the file name left with me.
## How to use
Simply download ReverseSearch.py and run it with any version of python3. It's just a single file. To exit the program, hit ctrl+c on keyboard.
### Twitter
You only need the filename, not even the file extension as images on Twitter seems to be only using jpg.
### Pixiv
When you download an artwork on the website or mobile app, you can see the artwork id on the file name.
### Danbooru
There are 2 options on danbooru avaliable. You can search the artwork by artist name, or by file name. Both information is avaliable on the default filename.
### Yande.re
The post id is the digits after yande.re in the filename.
### Konachan.com
The post id is the digits after Konachan.com - in the filename.
### Sankaku Channel
The filename itself is a MD5 hash. The search bar in Sankaku Channel website has a built in decrypter so we can find the file with md5:(filename). The only thing required is the hash/filename.
### Flying Milk Tea
The filename doesn't contain any id or hash that can be searched. Remember to add the id to the filename when you save the artwork. Good luck.
## Screenshots
![Screenshot 1](https://cdn.discordapp.com/attachments/744149045114568704/992158541903302816/unknown.png)
## Future of this repo
There is not much we can do with just a filename, expecially when you receive them from other person. Except Twitter and Sankaku, you can easily search the artwork just by the name of the artist and the tags. Rather than a "Reverse Search", this repo is more like a tool that save your time on typing the url. As I said, this repo was inspired by an accident that corrupts my collection of artworks. Remember to make a back up of your files/data as frequent as possible to minimize any chance of data loss.
