from comtypes import client
from comtypes.automation import VT_EMPTY
from typing import List, Any, Optional, Literal
from pathlib import Path


class IDMInterface:
    def __init__(self):
        tlb = r"D:\Tools\Internet Download Manager\idmantypeinfo.tlb"
        
        self.idm_module = client.GetModule(tlb)
        self.hr = client.CreateObject(
            progid='IDMan.CIDMLinkTransmitter',
            interface=self.idm_module.ICIDMLinkTransmitter2
        )
        
    def SendLinksArray(self, location: str, pLinksArray: List[List[str]]) -> None:
        """
        Location - the referrer of download, it’s assumed that the referrer is a single one
            for the entire array of internet links.
            
        pLinksArray – a pointer to 2 dimensional SAFEARRAY array of BSTR strings.
            For example, for N number of links, the size of the array will be (4 * N).
            For i changing from 0 to N-1 
            a[i,0] elements of the array are URLs to download,
            a[i,1] are cookies for corresponding a[i,0] URLs,
            a[i,2] are link descriptions for corresponding URLs,
            a[0,3] is the user agent, all others elements a[i,3] are not used and should be always NULL.
        """
        self.hr.SendLinksArray(location, pLinksArray)


    def SendLinkToIDM2(self, bstrUrl: str, bstrLocalFileName: str, bstrLocalPath: Path = ".", 
											 bstrReferer: str = "", bstrCookies: Optional[str] = None, 
											 bstrData: Optional[str] = None, bstrUser: Optional[str] = None, 
											 bstrPassword: Optional[str] = None,
                       lFlags: Literal[0, 1, 2] = 2,
                       reserved1: Any = VT_EMPTY, reserved2: Any = VT_EMPTY
                       ) -> None:
        """Transfers one link (URL) to IDM, brings Start Download dialog,
        or just adds the file to IDM download queue if a special flag is set.

        """

        self.hr.SendLinkToIDM2(bstrUrl=bstrUrl,
                               bstrReferer=bstrReferer,
                               bstrCookies=bstrCookies,
                               bstrData=bstrData,
                               bstrUser=bstrUser,
                               bstrPassword=bstrPassword,
                               bstrLocalPath=bstrLocalPath,
                               bstrLocalFileName=bstrLocalFileName,
                               lFlags=lFlags,
                               reserved1=reserved1 and reserved1 or VT_EMPTY,
                               reserved2=reserved2)

