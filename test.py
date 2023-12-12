import numpy as np
import array
from comtypes import npsupport

from IDMInterface import IDMInterface


# 单文件下载
# url = "http://www.internetdownloadmanager.com/trans_kit.zip"
# IDMInterface().SendLinkToIDM2(url, bstrLocalFileName="test.zip")

arr = np.array([
        ["aaa", "bbb", "ccc", "ddd"],
        ["aaa", "bbb", "ccc", None]
    ])
arr = ["http://www.internetdownloadmanager.com/trans_kit.zip","cookie","description","user-agent"]
# arr = array.array("h", [1, 2, 3, 4])




# 使用数组发送多个链接
npsupport.enable()
referer = "https://google.com"
IDMInterface().SendLinksArray(referer, arr)

