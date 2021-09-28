class Login:
    def __init__(self):

        #ユーザー名を入力する
        self.USER = ""
        # パスワードを入力する
        self.PASS = ""

        self.url_login = "https://jra.flpjp.com/"
    
    def stratLogin(self):
        
        
        browser.get(self.url_login)
        print("アクセス完了")
        
        
        #正常ログインできるまでループ
        while True:
            
            try:
                #0.1秒待機
                time.sleep(0.01)
                
                #ユーザーid要素を取得して入力
                element = browser.find_element_by_id('userid')
                element.clear()
                element.send_keys(self.USER)
                
                #passwd要素を取得して入力
                element = browser.find_element_by_id('passwd')
                element.clear()
                element.send_keys(self.PASS)

                #ボタン要素を取得してクリック
                form = browser.find_element_by_id('btn_login')
                form.click()
                
                #正常ログインできるとお知らせのラベルがでるので要素を取得してクリックして終了
                #もしログインできなかったら要素を取得できないのでexceptに投げる
                form = browser.find_element_by_xpath('//*[@id="attention_window_notice"]/div[3]/label/input')  
                form.click()

                form = browser.find_element_by_xpath('//*[@id="attention_button_0"]')
                form.click() 
                
    
                
                
                
                
                break
                
            except:
                #ログインページに遷移してもう一度ログイン処理を繰り返す
                print("ログイン失敗")
                browser.get(self.url_login)
                
from selenium import webdriver
import  time
import pandas as pd


# chromedriver.exeのディレクトリを選択する
browser = webdriver.Chrome(executable_path = 'C:\LoginWar\chromedriver.exe')
browser.implicitly_wait(0.01)

login = Login() 
login.stratLogin()


