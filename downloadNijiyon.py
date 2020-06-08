import os
from ImageDownloader import download_file, download_file_to_dir

# Path to download images
dstPath = "data/LoveLive/nijiyon/"

ImageFileExt = ".png"
NumOfImages = 111

nijiyonDict = {}

for i in range(1, NumOfImages):
    if i < 10:
        key = format(i, '02')
    else:
        key = str(i)

    if i < 7:
        value = "2018/" + "12/" + key + ImageFileExt
    elif i < 15:
        value = "2019/" + "01/" + key + ImageFileExt
    elif i < 23:
        value = "2019/" + "02/" + key + ImageFileExt
    elif i < 31:
        value = "2019/" + "03/" + key + ImageFileExt
    elif i < 39:
        value = "2019/" + "04/" + key + ImageFileExt
    elif i < 47:
        value = "2019/" + "05/" + key + ImageFileExt
    elif i < 55:
        value = "2019/" + "06/" + key + ImageFileExt
    elif i < 61:
        value = "2019/" + "07/" + key + ImageFileExt
    elif i < 75:
        value = "2019/" + "11/" + key + ImageFileExt
    elif i < 81:
        value = "2019/" + "10/" + key + ImageFileExt
    elif i < 103:
        value = "2019/" + "12/" + key + ImageFileExt
    elif i < 111:
        value = "2020/" + "12/" + key + ImageFileExt
    nijiyonDict[key] = value

# Outliars
nijiyonDict["01"] = "2018/12/manga_1.png"
nijiyonDict["02"] = "2018/12/manga_2.png"
nijiyonDict["03"] = "2018/12/03-1.png"
nijiyonDict["04"] = "2018/12/04-1.png"
nijiyonDict["18"] = "2019/02/18a.png"
nijiyonDict["23"] = "2019/03/a5fe479560a03d7ab1f1ec0c181e1e0e.png"
nijiyonDict["33"] = "2019/04/33ss.png"
nijiyonDict["56"] = "2019/07/e50fc97545c7e47640fdab9c85874d09.png"
nijiyonDict["61"] = "2019/11/61r.png"
nijiyonDict["62"] = "2019/10/62.png"
nijiyonDict["63"] = "2019/10/63.png"
nijiyonDict["64"] = "2019/07/64_r.png"
nijiyonDict["65"] = "2019/08/748f489e6bf55272b34c8f0e80e4d138.png"
nijiyonDict["66"] = "2019/10/66.png"
nijiyonDict["71"] = "2019/11/71r.png"
nijiyonDict["72"] = "2019/11/72r.png"
nijiyonDict["92"] = "2019/11/92r.png"
nijiyonDict["99"] = "2019/11/99r.png"
nijiyonDict["100"] = "2019/11/100r.png"
nijiyonDict["101"] = "2019/12/101r.png"

os.makedirs(dstPath, exist_ok=True)

for k, v in nijiyonDict.items():
    if int(k) < 61:
        BaseUrl = "https://s3-ap-northeast-1.amazonaws.com/lovelive-as.bushimo.jp/wp-content/uploads/"
    else:
        BaseUrl = "http://gs.dengeki.com/ss/gs/uploads/"
    NijiyonUrl = BaseUrl + v
    download_file(NijiyonUrl, os.path.join(dstPath, k+ImageFileExt))
