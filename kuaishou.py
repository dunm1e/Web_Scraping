import requests

url = 'https://v1.kwaicdn.com/ksc2/0BxaMRmeJNiX66iwlqFXTmzs1pYw4ByI5Rs_Mwj_y1sWlcRMhKH-vwFDRbR0Bc5JC4ctHsgdH5k0IMqs0zB6nUx-6fTTcUHZllkVqiGGpsLFpmRp_e0vETNpDaNcin6VXf2FFGGRrzl4M9BIlCHMVEPcBl-HIpZn2g2m8N5wyCLRdCa7Nel46cgw22FSOu4b.mp4?pkey=AAU9dAHkuKkGD4dTXZHL68C8K6xkhvJoDW64szttk9AIEoFJ7W9e-Bl-7MWC8NJRmDaAhP0K6GhlrsGiJlhMRDgcP0OcTO6HDkg7q5agbZl_5f7Zvi70yktkdTlGAvaXYuY&tag=1-1709477378-unknown-0-cc7orycaiv-901c5fd9da343d12&clientCacheKey=3xqzcg5x5992rvi_b.mp4&di=JAiGVgZYED2mEAXWqJ8Zjw==&bp=10004&tt=b&ss=vp'
res = requests.get(url)
open('好东西.mp4','wb').write(res.content)