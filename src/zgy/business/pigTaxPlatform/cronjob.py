from src.zgy.business.pigTaxPlatform import BaseParent


class ProcessService(BaseParent):

    def zgyNotifyInvoicingFaceAuth(self):
        data = {
            "notifyType": "INVOICE_MAKE_OUT_FACE_SCAN",
            "notifyDataList": [{
                "id": 342700863225856,
                "data":'{"tpCompanyId": 342673248829442,"taxNo": "91350102MA2YCKU00T","userName": "userName","taxBureauAuthId": "taxBureauAuthId","taxBureauQrCode": "taxBureauQrCode","incomeTaxAuthId": "incomeTaxAuthId","incomeTaxQrCode": "incomeTaxQrCode"}'
            }]
        }
        response = self.post(
            "/nk-anon/internal/callback/v1/zgy_notify",
            data)
        print(response.text)


processService = ProcessService()
processService.zgyNotifyInvoicingFaceAuth()
