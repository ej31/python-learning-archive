import webbrowser

from bs4 import BeautifulSoup, FeatureNotFound
import pandas as pd
import urllib.request as req


class RTMSService:
    def __init__(self):
        self.__apikey = '6lO8Aosdue50f2MUKPk8aBNG1OAUsnxwJTEo3UiereoYuszDO%2FM5cz26NxRuHnaiL1W63PE2rRY%2Bh8DA6w1iJw%3D%3D'

    def do(self):
        try:
            self.getRTMSDataSvcAptTrade('41117', '202201', self.__apikey)
            self.getRTMSDataSvcAptTrade('41117', '202202', self.__apikey)
            file = "법정동코드 전체자료.txt"
            code = pd.read_csv(file, sep='\t')
            code = code[code['폐지여부'] == '존재']

            gu = '영통구'  # 구 이름 입력
            gu_code = code[code['법정동명'].str.contains(gu)]  # '법정동명'에 '영통구'가 포함된 데이터 찾기
            gu_code = gu_code['법정동코드'].reset_index(drop=True)[0]  # '법정동코드' index를 reset후 첫번째 index선택
            gu_code = gu_code[0:5]  # '법정동코드' 10자리 중 앞 5자리만 사용

            year = [str("%04d" % y) for y in range(2011, 2023)]
            month = [str("%02d" % m) for m in range(1, 13)]
            yyyymm_list = ["%s%s" % (y, m) for y in year for m in month]

            Your_Key = self.__apikey

            aptTrade2 = pd.DataFrame()
            for yyyymm in yyyymm_list:
                temp2 = self.getRTMSDataSvcAptTrade(gu_code, yyyymm, Your_Key)
                aptTrade2 = pd.concat([aptTrade2, temp2]).reset_index(drop=True)
        except FeatureNotFound as e:
            print(e)
            print("API KEY가 없는 경우일 확률이 큼")

    @staticmethod
    def getRTMSDataSvcAptTrade(gu_code, yyyymm, serviceKey):
        url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev"
        url = url + "?&LAWD_CD=" + gu_code
        url = url + "&DEAL_YMD=" + yyyymm
        url = url + "&serviceKey=" + serviceKey
        webbrowser.open(url)
        return

    @staticmethod
    def getRTMSDataSvcAptTrade(gu_code, yyyymm, serviceKey):
        url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev"
        url = url + "?&LAWD_CD=" + gu_code
        url = url + "&DEAL_YMD=" + yyyymm
        url = url + "&serviceKey=" + serviceKey

        xml = req.urlopen(url)
        result = xml.read()
        soup = BeautifulSoup(result, 'lxml-xml')

        items = soup.findAll("item")
        aptTrade = pd.DataFrame()

        for item in items:
            거래일자 = int(item.find("년").text) * 10000 + int(item.find('월').text) * 100 + int(item.find('일').text)
            법정동 = item.find("법정동").text
            전용면적 = float(item.find("전용면적").text)
            아파트 = item.find("아파트").text
            층 = int(item.find("층").text)
            거래금액 = int(item.find("거래금액").text.replace(',', ''))

            도로명 = item.find("도로명").text
            도로명건물본번호코드 = int(item.find('도로명건물본번호코드').text)
            도로명건물부번호코드 = int(item.find("도로명건물부번호코드").text)
            도로명시군구코드 = int(item.find("도로명시군구코드").text)
            도로명일련번호코드 = int(item.find("도로명일련번호코드").text)
            도로명코드 = int(item.find("도로명코드").text)

            법정동부번코드 = int(item.find("법정동부번코드").text)
            법정동시군구코드 = int(item.find("법정동시군구코드").text)
            법정동읍면동코드 = int(item.find("법정동읍면동코드").text)
            법정동지번코드 = int(item.find("법정동지번코드").text)

            지번 = item.find("지번").text
            지역코드 = int(item.find("지역코드").text)
            건축년도 = int(item.find("건축년도").text)

            temp = pd.DataFrame(([[거래일자, 법정동, 전용면적, 아파트, 층, 거래금액,
                                   도로명, 도로명건물본번호코드, 도로명건물부번호코드, 도로명시군구코드, 도로명일련번호코드, 도로명코드,
                                   법정동부번코드, 법정동시군구코드, 법정동읍면동코드, 법정동지번코드,
                                   지번, 지역코드, 건축년도]]),
                                columns=["거래일자", "법정동", "전용면적", "아파트", "층", "거래금액",
                                         "도로명", "도로명건물본번호코드", "도로명건물부번호코드", "도로명시군구코드", "도로명일련번호코드", "도로명코드",
                                         "법정동부번코드", "법정동시군구코드", "법정동읍면동코드", "법정동지번코드",
                                         "지번", "지역코드", "건축년도"])
            aptTrade = pd.concat([aptTrade, temp])

        aptTrade = aptTrade.reset_index(drop=True)
        return aptTrade


if __name__ == '__main__':
    RTMSService().do()
