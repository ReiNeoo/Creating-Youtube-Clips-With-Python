import pandas as pd

import get_rid_of_akrostish as grod
from clip_list import get_clips

video_url = "https://www.youtube.com/watch?v=JugxpebuS_E" # indirelecek videonun url'si

# indirilen videonun açılan video klasöründeki dosya yolu
# bu dosya yolunu elde etmek için download_the_video() fonksiyonun bir kere çalıştırılması gerekiyor.
# bir kere çalıştırıldıktan sonra oluşan dosya yolunu aşağıya yapıştırıyoruz
video_path = "video\ELDEN RING Shadow of the Erdtree – Official Launch Trailer\ELDEN RING Shadow of the Erdtree – Official Launch Trailer.mp4" 

excel_path = "acrostish.xlsx" # alınacak kesitlerin bilgilerinin tutulduğu excel dosyasının yolu. dosya yüklendikten sonra değiştirilecek.

df = pd.read_excel(excel_path)
df["baslangic"] = df["baslangic"].astype(str)
df["bitis"] = df["bitis"].astype(str)

object = grod.akrostish(video_url, "video", "clips", download_res= "360p") # indirecek sınıfı çağırıyoruz
object.download_the_video() # indirme işlemini yapan fonksiyon çağırılıyor
print(video_path)

get_clips(dataframe= df, input_path= video_path) # Kliplerin kesitlerini alan fonksiyon.