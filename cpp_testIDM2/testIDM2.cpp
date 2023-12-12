// testIDM2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#import "IDManTypeInfo.tlb" 
#include "IDManTypeInfo.h"		
#include "IDManTypeInfo_i.c"	

#include <atlbase.h>	//for CComBSTR class

int main(int argc, char* argv[])
{
	int nItems = 2;
	CComBSTR referer = L"http://www.internetdownloadmanager.com/";

	CComBSTR href1 = L"http://www.internetdownloadmanager.com/trans_kit.zip";
	CComBSTR cookie1 = L"cookie1=aaa";
	CComBSTR descr1 = L"Link 1";

	CComBSTR href2 = L"http://www.internetdownloadmanager.com/idman404.exe";
	CComBSTR cookie2 = L"cookie2=bbb";
	CComBSTR descr2 = L"Link 2";

	CComBSTR userAgent = L"User-Agent test2";
	
	CoInitialize(NULL);

	ICIDMLinkTransmitter2* pIDM;
	HRESULT hr = CoCreateInstance(CLSID_CIDMLinkTransmitter, NULL, CLSCTX_LOCAL_SERVER, IID_ICIDMLinkTransmitter2, (void**)&pIDM);
	if (S_OK == hr)
	{
		SAFEARRAY *pSA = NULL;
		SAFEARRAYBOUND bound[3];
		bound[0].lLbound = 0;
		bound[0].cElements = nItems;
		bound[1].lLbound = 0;
		bound[1].cElements = 4;
		pSA = SafeArrayCreate(VT_BSTR, 2, bound);
		if (NULL != pSA)
		{
			long index[2];
			int iItem = 0;

			index[0] = iItem;
			index[1] = 0;
			SafeArrayPutElement(pSA, index, href1);

			index[1] = 1;
			SafeArrayPutElement(pSA, index, cookie1);

			index[1] = 2;
			SafeArrayPutElement(pSA, index, descr1);

			index[1] = 3;
			SafeArrayPutElement(pSA, index, ((0 == iItem) ? userAgent : NULL));


			iItem++;

			index[0] = iItem;
			index[1] = 0;
			SafeArrayPutElement(pSA, index, href2);

			index[1] = 1;
			SafeArrayPutElement(pSA, index, cookie2);

			index[1] = 2;
			SafeArrayPutElement(pSA, index, descr2);

			index[1] = 3;
			SafeArrayPutElement(pSA, index, ((0 == iItem) ? userAgent : NULL));


			VARIANT var;
			VariantInit(&var);
			var.vt = VT_ARRAY | VT_BSTR;
			var.parray = pSA;
			hr = pIDM->SendLinksArray(referer, &var);

			if (S_OK != hr)
			{
				//.........
			}

			SafeArrayDestroy(pSA);
		}

		pIDM->Release();
	}

	CoUninitialize();

	return 0;
}

