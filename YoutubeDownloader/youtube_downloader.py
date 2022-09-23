# from pytube import YouTube

# link = input("Youtube Link:")
# yt = YouTube(link)

# # details of the video streams

# # print("Video titile is"+yt.title)
# # print("Video Views : +"+yt.views)
# # print("Length of video:", yt.length, "seconds")
# # print("Video Description :"+yt.description)
# # print("Rating :"+yt.rating)

# # ys = yt.streams.get_highest_resolution()
# ys = yt.streams.first()
# # ys = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# print("Downloading...")
# ys.download('./')
# print("Download completed!!")

from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)


#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

#Getting the highest resolution possible

# ys = yt.streams.first()  returns first low res video
print(yt.streams.all()) # returns all aviliable streams
# print(yt.channel_url) returns the channel youtube link
# print(yt.publish_date) returns the publish date 

# print(yt.thumbnail_url) returns the thumbnail image url



#Starting download
# print("Downloading...")

# ys.download()
# print("Download completed!!")
