import requests
import allure

class Altaivita:
    
    def __init__(self):
        self.base_url = 'https://altaivita.ru/'
        self.params_for_cart = 'LANG_key=ru&S_hint_code=&S_cur_code=rub&S_CID=dc6a4317ab8b83658b9b8e9a15a35f11'
        self.params_for_add = 'product_id=703&this_listId=product_cart&parent_product=703&LANG_key=ru&S_wh=1&S_CID=dc6a4317ab8b83658b9b8e9a15a35f11&S_cur_code=rub&S_koef=1&quantity=1&S_hint_code=&S_customerID='
        self.delete_params = 'product_id=703&LANG_key=ru&S_wh=1&S_CID=dc6a4317ab8b83658b9b8e9a15a35f11&S_cur_code=rub&S_koef=1&S_hint_code=&S_customerID='
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'CID=dc6a4317ab8b83658b9b8e9a15a35f11; site_countryID=247; site_country_name=%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F; _userGUID=0:mb84zo4c:~QlZRVv4Vam40OtGf2k8cQ66lLQRtlhl; _userGUID=0:mb84zo4c:~QlZRVv4Vam40OtGf2k8cQ66lLQRtlhl; _ym_uid=174844833441562895; _ym_d=1748448334; PHPSESSID=om40qv82nii77pscalv3emrcg1; _ym_isad=2; _dvs=0:mb9gi32e:juoM1RR9a6ghMX~VJ8vH1SCaFmd01p9a; digi_uc=|v:174851:2028!174852:703|s:174844:2028; DIGI_CARTID=38044432635; dSesn=c72604f6-6727-fc1e-0b78-fe1dc1392fc2',
            'Host': 'altaivita.ru',
            'Origin': 'https://altaivita.ru',
            'Referer': 'https://altaivita.ru/cart/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "YaBrowser";v="25.4", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
            }
    
    def enter_cart(self) -> any:
        with allure.step("заходим в корзину"):
            url = 'engine/cart/ajax_get_cart_contents.php'
            return requests.post(self.base_url+url, headers=self.headers, params=self.params_for_cart)
        
    
    def add_good_in_cart(self) -> any:
        with allure.step("добавление товара в корзину"):
            url ='engine/cart/add_products_to_cart_from_preview.php'
            return requests.post(self.base_url+url, headers=self.headers, params=self.params_for_add)
    

    def delete_dood_from_cart(self):
        with allure.step("удаление товара из корзины"):
            url = 'engine/cart/delete_products_from_cart_preview.php'
            resp = requests.post(self.base_url+url, headers=self.headers, params=self.delete_params)
            return resp


