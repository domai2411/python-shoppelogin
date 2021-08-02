import requests
import json
from PIL import Image
from PIL import ImageSequence
import matplotlib.pyplot as plt
import base64
import random
import http.client
import hashlib
from requests_toolbelt.utils import dump
import getpass
# data = dump.dump_all(response)
# print(data)
session = requests.session()
http.client._MAXHEADERS = 10000





def ranspc():
    x=""
    a8=str('%08x' % random.randrange(16**8))
    x=a8
    i=0
    while i<3:
        a4=str('%04x' % random.randrange(16**4))
        x=x+'-'+a4
        i+=1
    a12=str('%04x' % random.randrange(16**12))
    x=x+'-'+a12
    return x

def capchashowing(capcha):
    imgdata = base64.b64decode(capcha)
    filename = 'test.gif'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

    im = Image.open('test.gif')
    i=1
    while i<5:
        index = 1
        for frame in ImageSequence.Iterator(im):
            # frame.save("frame%d.png" % index)
            index += 1
            plt.imshow(frame)
            plt.pause(.1)
            plt.title('BẠN KHÔNG THỂ TẮT CỬA SỔ NÀY. HÃY GHI CHÚ LẠI CAPCHA VÀ CHỜ CỬA SỔ NÀY TỰ ĐÓNG LẠI')
            plt.draw()
        i+=1
        plt.clf() #will make the plot window empty
    plt.close()   
def capchag():
    captcha_id=False
    burp0_url = "https://banhang.shopee.vn:443/api/selleraccount/v2/get_captcha_info/?region=VN&SPC_CDS=6067cad0-344a-491a-ae4c-c50f817514c7&SPC_CDS_VER=2"
    burp0_cookies = {"SPC_F": "opM4pxVXH3gWhfTB94mCf4BtAfePA8Ri", "_gcl_au": "1.1.533318112.1620713928", "_med": "refer", "_fbp": "fb.1.1620713928877.1392768770", "_hjid": "8fa83faf-b25c-4531-a78b-1a2febd43bae", "G_ENABLED_IDPS": "google", "SPC_CDS": "6067cad0-344a-491a-ae4c-c50f817514c7", "SPC_SC_SA_TK": "", "UYOMAPJWEMDGJ": "", "SPC_IVS": "", "SPC_SC_SA_UD": "", "SPC_SI": "mall.dNJWQJUYvHD2Aknn5pVYt5Cp2qAXUbpW", "_gid": "GA1.2.10610415.1620872346", "SPC_CLIENTID": "b3BNNHB4VlhIM2dXrakdksczbxuutony", "_ga": "GA1.1.153903412.1620713929", "SPC_R_T_ID": "\"5vEl8kAm/m6P8sW6RUcP3jYRMXF0ZOM/JPcOiNBcHyV9NgvY4gY/yf8ULm6DcmMAe7c8mISNwrwm2CdvJyPtrLeMVzZ30WXN/kENvvBM3XE=\"", "SPC_R_T_IV": "\"ofCNzcP5BiPaeFuoFQjr+A==\"", "_ga_M32T05RVZT": "GS1.1.1620872344.2.1.1620872531.9", "RO_T": "\"pRCtRQ2UZGQ/fPTsNYsZy1sGxugOy3DM9eI5IuGZbAige/yMUUSo+qNO0UXQ4wSW\"", "SC_SSO_U": "-", "SC_SSO": "-", "SPC_WST": "\"A+so0DB4AhaCJcroE+BnGN8JAXq+IFkKVsPHGWiYpQTvfWLNDdVs3sRX+a8xrm9bFURFjJAa4IgeUyEMxwigtWPEKy24DfIaekBIkRyJUD47DcBNJ9t8P+cswI9jpYv9yzA4HctEXgsSuqBnVaSC5JUx003s7A7wRUZ0RPMdzhs=\"", "SPC_SC_UD": "", "SPC_STK": "-", "SPC_U": "-", "SPC_EC": "-", "SPC_SC_TK": "", "SC_DFP": "Ac0uSGFt1prEKAQCGO12bUFA6zRbgI58"}
    burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Accept": "application/json, text/plain, */*", "Sc-Fe-Session": "c05e5a36-3090-4c7f-a93e-8d9cfda3d027", "Sc-Fe-Ver": "25941", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/account/signin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    response =session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    
    response = response.content
    response = response.decode("utf-8")
    aj = json.loads(response)
    # print(aj)
    capcha=aj['data']['captcha_body']['bg_img']
    captcha_id=aj['data']['captcha_id']
    capcha=capcha.split(",")[1]
    input("Shoppe yêu cầu nhập CAPCHA, bạn hãy đọc và ghi chú lại mã CAPCHA, nhấn phím bất kỳ để bắt đầu đọc CAPCHA...")
    capchashowing(capcha)
    while True:
        print("Vui lòng chọn:\n1.Bạn đã đọc được và ghi chú lại CAPCHA\n2.Bạn cần xem lại CAPCHA")
        val2 = input("Nhập lựa chọn của bạn:")
        if val2==str(1):
            break
        elif val2==str(2):
            capchashowing(capcha)
        else:
            print("Vui lòng nhập đúng 1,2 hoặc 0")
    return captcha_id

def startlogin():
    burp0_url = "https://banhang.shopee.vn:443/account/signin"
    burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Sec-Ch-Ua-Mobile": "?0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://banhang.shopee.vn/account/signin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    session.get(burp0_url, headers=burp0_headers)
    
    burp0_url = "https://seller.shopee.sg:443/api/pap/sdkConfig/8/?env=live"
    burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Accept": "*/*", "Origin": "https://banhang.shopee.vn", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    session.get(burp0_url, headers=burp0_headers)
    
    
    burp0_url = "https://seller.shopee.sg:443/api/pap/sdkConfig/70/?env=live"
    burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Accept": "*/*", "Origin": "https://banhang.shopee.vn", "Sec-Fetch-Site": "cross-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    session.get(burp0_url, headers=burp0_headers)

    
    # spc="e1f45d5f-1e48-45c4-87f7-ae68e99c6796"
    burp0_url = "https://banhang.shopee.vn:443/api/v2/login/?SPC_CDS="+spc+"&SPC_CDS_VER=2"
    burp0_cookies = {"SPC_CDS": spc}
    burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Accept": "application/json, text/plain, */*", "Sc-Fe-Session": "cd684db9-1ebe-4202-b08e-c8637f86a423", "Sc-Fe-Ver": "25941", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/account/signin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    response =session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    # az = response.content
    # az = az.decode("utf-8")
    # aj = json.loads(az)
    # errcode=aj['errcode']
    # print(errcode)
def logf(ltype):   
    if ltype=='fisrtlog':
        global phone
        global password_hash
        print("Nhập thông tin login, nếu bạn quên password hãy sử dụng website shoppe để lấy lại password, API này không hỗ trợ lấy lại password.")
        phone = input("Nhập số điện thoại/username : +84")
        phone="84"+phone
        password = input("Nhập Password: ")
        # password = getpass.getpass('Password:')
        # phone="84909004535"
        # password="MiaMia@24112209"
        passwordhash = hashlib.md5(password.encode('utf-8'))
        passwordh = hashlib.sha256((passwordhash.hexdigest()).encode('utf-8'))
        password_hash=passwordh.hexdigest()
        burp0_url = "https://banhang.shopee.vn:443/api/v2/login/?SPC_CDS="+spc+"&SPC_CDS_VER=2"
        # burp0_cookies = {"SPC_CDS": "e1f45d5f-1e48-45c4-87f7-ae68e99c6796", "UYOMAPJWEMDGJ": "", "SPC_IVS": "", "SPC_SC_SA_TK": "", "SPC_SC_SA_UD": "", "SPC_SC_UD": "", "SPC_SC_TK": "", "SC_DFP": "KEjMZPVRSdUL7vVniBPY3ytWmv0Zd2oi"}
        burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Accept": "application/json, text/plain, */*", "Sc-Fe-Session": "2cfc92fb-152c-4a17-87ce-0b7f06ff76dc", "Sc-Fe-Ver": "26002", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8", "Origin": "https://banhang.shopee.vn", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/account/signin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        burp0_data = {"phone": phone, "password_hash": password_hash, "remember": "false"}
        response=session.post(burp0_url, headers=burp0_headers, data=burp0_data)
        az = response.content
        az = az.decode("utf-8")
        aj = json.loads(az)
        # print(aj)
        if "message" in aj:
            message=aj['message']
        elif "username" in aj:
            message='login_ok'
        else:
            message='unknow_error_firstlog'
        return message
    if ltype=='capchalog':
 
        captcha_id=capchag()
        c = input("Nhập CAPCHA mà bạn đã đọc được:")
        burp0_url = "https://banhang.shopee.vn:443/api/v2/login/?SPC_CDS="+spc+"&SPC_CDS_VER=2"
        # burp0_cookies = {"SPC_CDS": "e1f45d5f-1e48-45c4-87f7-ae68e99c6796", "UYOMAPJWEMDGJ": "", "SPC_IVS": "", "SPC_SC_SA_TK": "", "SPC_SC_SA_UD": "", "SPC_SC_UD": "", "SPC_SC_TK": "", "SC_DFP": "KEjMZPVRSdUL7vVniBPY3ytWmv0Zd2oi", "SPC_F": "j0NdjegCPCotUbdSDUMOrYdWB9LNP9zV"}
        burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Accept": "application/json, text/plain, */*", "Sc-Fe-Session": "2cfc92fb-152c-4a17-87ce-0b7f06ff76dc", "Sc-Fe-Ver": "26002", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8", "Origin": "https://banhang.shopee.vn", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/account/signin", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        burp0_data = {"phone": phone, "password_hash": password_hash, "remember": "false", "captcha": c, "captcha_id": captcha_id}
        response=session.post(burp0_url, headers=burp0_headers, data=burp0_data)
        az = response.content
        az = az.decode("utf-8")
        aj = json.loads(az) 
        # print(aj)
        if "message" in aj:
            message=aj['message']
        elif "username" in aj:
            message='login_ok'
        else:
            message='unknow_error_capcha'
        return message
    if ltype=='optlog':    
        otp = input("Shoppe yêu cầu OTP. Bạn hãy kiểm tra điện thoại và nhập OTP vừa nhận được từ Shoppe:")
        burp0_url = "https://banhang.shopee.vn:443/api/v2/login/?SPC_CDS="+spc+"&SPC_CDS_VER=2"
        # burp0_cookies = {"SPC_EC": "-", "SPC_F": "opM4pxVXH3gWhfTB94mCf4BtAfePA8Ri", "SPC_U": "-", "_gcl_au": "1.1.533318112.1620713928", "_med": "refer", "_fbp": "fb.1.1620713928877.1392768770", "_hjid": "8fa83faf-b25c-4531-a78b-1a2febd43bae", "G_ENABLED_IDPS": "google", "SPC_CDS": "6067cad0-344a-491a-ae4c-c50f817514c7", "SPC_SC_SA_TK": "", "SPC_SC_UD": "", "UYOMAPJWEMDGJ": "", "SPC_IVS": "", "SPC_SC_TK": "", "SPC_SC_SA_UD": "", "SPC_SI": "mall.dNJWQJUYvHD2Aknn5pVYt5Cp2qAXUbpW", "AMP_TOKEN": "%24NOT_FOUND", "_gid": "GA1.2.10610415.1620872346", "SPC_CLIENTID": "b3BNNHB4VlhIM2dXrakdksczbxuutony", "_ga": "GA1.1.153903412.1620713929", "SPC_R_T_ID": "\"5vEl8kAm/m6P8sW6RUcP3jYRMXF0ZOM/JPcOiNBcHyV9NgvY4gY/yf8ULm6DcmMAe7c8mISNwrwm2CdvJyPtrLeMVzZ30WXN/kENvvBM3XE=\"", "SPC_R_T_IV": "\"ofCNzcP5BiPaeFuoFQjr+A==\"", "_ga_M32T05RVZT": "GS1.1.1620872344.2.1.1620872531.9", "SC_DFP": "8rOW0eArvspCBxZlLhlLt6ZnFLvfGeeh", "RO_T": "\"pRCtRQ2UZGQ/fPTsNYsZy1sGxugOy3DM9eI5IuGZbAige/yMUUSo+qNO0UXQ4wSW\""}
        burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Accept": "application/json, text/plain, */*", "Sc-Fe-Session": "1367ba70-94bf-4126-a660-11f2057fbff7", "Sc-Fe-Ver": "25941", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8", "Origin": "https://banhang.shopee.vn", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/account/signin?next=%2F", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        burp0_data = {"phone": phone, "password_hash": password_hash, "remember": "false", "vcode": otp}
        response=session.post(burp0_url, headers=burp0_headers, data=burp0_data)
        az = response.content
        az = az.decode("utf-8")
        # print(az)
        aj = json.loads(az)
        # print(aj)
        if "message" in aj:
            message=aj['message']
        elif "username" in aj:
            message='login_ok'
        else:
            message='unknow_error_optlog'
        return message
def loginmain(message):
    while True:
        if message=="":
            m=logf('fisrtlog')
        elif message=="error_require_captcha":
            m=logf('capchalog')
        elif message=="error_need_otp":
            m=logf('optlog')
        elif message=="error_perm":
            print("Nhập sai user hoặc password, vui lòng kiểm tra lại.")
            m=logf('fisrtlog')
        elif message=="error_otp":
            print("Nhập sai OTP, vui lòng kiểm tra lại.")
            m=logf('optlog')
        elif message=='login_ok':
            m="OK"
            break
        else:
            m='unknow'
            print("Gặp lỗi không xác định:"+message+". Vui lòng liên hệ VTMSoft dể được hỗ trợ.")
            break
        message=m
    return message
def logout():
    burp0_url = "https://banhang.shopee.vn:443/api/v1/logout/?SPC_CDS="+spc+"&SPC_CDS_VER=2"
    burp0_headers = {"Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"", "Accept": "application/json, text/plain, */*", "Sc-Fe-Session": "ec38e23d-fbc7-44e5-bc00-ca034be7c7df", "Sc-Fe-Ver": "26002", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://banhang.shopee.vn/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    response=session.get(burp0_url, headers=burp0_headers)
    az = response.headers
    # print(az)
def login():
    print("Bạn đang login Shoppe từ API của VTMSoft.")
    print("Thông tin bạn nhập sẽ được gửi thẳng đến shoppe từ máy tính của bạn.Chúng tôi hoàn toàn không đọc hoặc lưu trữ các thông tin này của bạn.")
    print("Shoppe không khuyến khích các bạn sử dụng API tự phát triển. Bạn chấp nhận rủi ro khi sử dụng API này.")

    global spc
    spc=ranspc() 
    startlogin()
    message=""
    r=loginmain(message)
    return r  
def main():
    r=login()
    logout()
if __name__ == "__main__":
    main()