class TestBaiDu(unittest.TestCase):
    URL = "http://www.baidu.com"
    base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
    driver_path = os.path.abspath(base_path+'\drivers\chromedriver.exe')

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.URL)