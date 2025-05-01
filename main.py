from tiktokdownloader import TikTokDownloader
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1ZZUYfa6j-V9g6Ckv2yl30YsyHf5dMhzlGaR0ni3LGWY/export?gid=84674231&format=csv"

data = pd.read_csv(url)

print(data)

# Initialize downloader
downloader = TikTokDownloader()

for video_url in list(set(data["contentLink"].to_list()[0:3])):

    downloader.download_video(video_url)