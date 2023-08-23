# """
# document.listForm.captchaCheck.value = true;fn_csv();
# """
# from sample.sele import Browser
#
# _browser = Browser(False)
# _browser.get("http://rtdown.molit.go.kr/")
# js_code = "document.listForm.captchaCheck.value = true;fn_csv();"
#
# _browser.execute_script(js_code)


import requests
import calendar


def main():
    for year in range(2020, 2024):
        for month in range(1, 13):
            # 매월 초일 말일 구하기
            first_day, last_day = calendar.monthrange(year, month)

            formdata = {
                "cal_url": "/sym/cmm/EgovNormalCalPopup.do",
                "totCnt": "0",
                "exlTotCnt": "0",
                "searchBungi1": "",
                "searchBungi2": "",
                "captchaCheck": "true",
                "sidoNm": "전체",
                "sigunguNm": "전체",
                "umdNm": "전체",
                "areaNm": "전체",
                "loadNm": "도로명",
                "searchFromDt": f"{year}{month}{first_day}",
                "searchToDt": f"{year}{month}{last_day}",
                "fileType": "CSV",
                "searchRtGubunCd": "AT",
                "gubunRadio2": "1",
                "searchSidoCd": "ALL",
                "searchGugunCd": "ALL",
                "searchDongCd": "ALL",
                "searchChosung": "ALL",
                "searchLoad": "ALL",
                "searchDanjiCd": "ALL",
                "bungiSn": "ALL",
                "searchArea": "ALL",
                "searchGb": "2",
                "searchFromAmount": "",
                "searchToAmount": ""
            }
            resp = requests.post(
                url="http://rtdown.molit.go.kr/rtms/rqs/rtAptTrCSV.do",
                data=formdata
            )

            print(resp)
