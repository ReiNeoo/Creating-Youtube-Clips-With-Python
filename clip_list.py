import pandas as pd
from get_rid_of_akrostish import akrostish

#video_url = "https://www.youtube.com/watch?v=JugxpebuS_E"
#video_path = "video\ELDEN RING Shadow of the Erdtree – Official Launch Trailer\ELDEN RING Shadow of the Erdtree – Official Launch Trailer.mp4"

video_url = "a"
obj = akrostish(video_url, "video", "clips", download_res= "360p")

def get_clips(dataframe, input_path):
    for index, row in dataframe.iterrows():
        obj.cut_clip_from_video(input_path= input_path,
                                clip_name= row["klip_adi"],
                                start_time= row["baslangic"],
                                end_time= row["bitis"])
        

