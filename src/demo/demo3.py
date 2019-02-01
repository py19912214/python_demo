from urllib import parse,request
while True:
    header_dict = {'x-ag-decryption': 'true'}
    url='http://localhost:8080/app/activity/query-app-card-info?_sid_=3366813017&_vn_=6.12.0.5&walletType=TRUCK_WALLET&_t_=1547627719472&platform=ANDROID&_pvc_=21100&_pn_=com.xiwei.logistics&_m_=OPPO%20R9m&uid=1_7628034&_lat_=28.111735&_no_=CHINA_UNICOM&_lng_=113.130717&_ov_=5.1&requestId=1547627719344&_ch_=DirectDownload&_dfp_=b3c3309f-c3e9-4a52-8acc-c748c19ddf7f&_pvn_=2.11.0&walletVersion=21100&_nw_=4G&_vc_=6120005&_ppn_=com.wlqq.phantom.plugin.wallet'
    req = request.Request(url,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    print(res.decode(encoding='utf-8'))