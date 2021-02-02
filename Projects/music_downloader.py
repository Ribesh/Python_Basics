import urllib.request

def obtain_data(remotefile):
    with urllib.request.urlopen(remotefile) as handler:
        return handler.read()
    


def save_to_disk(data,filename,extention=".mp3"):  # default arguments
    with open(filename + extention,"wb") as handler:      # same as handler=open("Data.txt","w") the only diff is it will auto close
        handler.write(data) 

filename = input("Enter the file name for the song")
mp3 = input("Enter the URL to download MP3")     
data = obtain_data(mp3)
save_to_disk(data,filename)