from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading

def process_phone_numbers(phone_numbers, browser_index):
    # 创建 WebDriver 对象
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--disable-blink-features=AutomationControlled')
    edge_options.add_argument('--disable-extensions')
    edge_options.add_argument('--user-agent="Your Custom User Agent String"')
    
    wd = webdriver.Edge(options=edge_options)
    wd.get('your own webiste')

    # 等待页面加载
    wd.implicitly_wait(15)  # 可以根据网络情况调整时间

    for phone_number in phone_numbers:
        # 找到手机号输入框并输入手机号
        phone_input = wd.find_element(By.XPATH, '//*[@id="app"]/section[1]/section/main/div[1]/div/div[2]/form[2]/div[1]/div/div[1]/input')
        phone_input.clear()  # 清除输入框内容
        phone_input.send_keys(phone_number)

        # 定义按钮的 XPath
        button_xpath = '/html/body/div[1]/div/div/section[1]/section/main/div[1]/div/div[2]/form[2]/div[2]/div/button'
        
        while True:
            try:
                # 等待按钮出现
                button = WebDriverWait(wd, 10).until(
                    EC.presence_of_element_located((By.XPATH, button_xpath))
                )
                
                # 检查按钮文本内容
                button_text = button.text
                if button_text == "获取验证码":
                    button.click()
                    print(f"[Window {browser_index}] 已点击获取验证码按钮，手机号: {phone_number}")
                    break
                else:
                    print(f"[Window {browser_index}] 按钮文本不是“获取验证码”，而是“{button_text}”，继续等待。")
                    time.sleep(1)  # 等待一秒后重新检查
            except Exception as e:
                print(f"[Window {browser_index}] 处理手机号 {phone_number} 失败: {e}")
                break

        # 等待“重新发送”字样出现
        try:
            WebDriverWait(wd, 10).until(
                EC.text_to_be_present_in_element(
                    (By.XPATH, '//*[@id="app"]/section[1]/section/main/div[1]/div/div[2]/form[2]/div[2]/div/button/span'),
                    "重新发送"
                )
            )
            
            # 清除所有Cookies
            wd.delete_all_cookies()
            
            # 刷新网页
            wd.refresh()
        
        except Exception as e:
            print(f"[Window {browser_index}] 等待“重新发送”字样失败: {e}")

    # 关闭浏览器
    # wd.quit()  # 如果你不想关闭窗口，可以注释掉这一行

def main():
    # 生成手机号列表
    phone_numbers = [f"138{num:08d}" for num in range(0, 10000000)]
    
    # 分配给每个窗口的手机号列表
    num_threads = 3
    split_phone_numbers = [phone_numbers[i::num_threads] for i in range(num_threads)]
    
    # 创建和启动线程
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=process_phone_numbers, args=(split_phone_numbers[i], i+1))
        thread.start()
        threads.append(thread)
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
