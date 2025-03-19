from playwright.sync_api import Page, expect
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        
    def navigate(self):
        self.page.goto("https://www.kiwi.com/en/")

        modal1 = self.page.locator("[data-test='ModalCloseButton']")
        modal2 = self.page.locator("[data-test='PlacePickerInputPlace-close']")
        if modal1.is_visible(timeout=5000):
            modal1.click()        
        if modal2.is_visible(timeout=5000):  
            modal2.click()

        #self.page.pause()           

        
    def select_one_way(self):
        #self.page.locator("[data-test=\"SearchFormModesPicker-active-return\"] div").filter(has_text="ReturnReturn").get_by_role("button").click()
        self.page.get_by_role("button", name="Return").nth(0).click() 
        self.page.locator("[data-test='ModePopupOption-oneWay']").click()
        

    def set_departure_rtm(self):
        self.page.locator("[data-test=\"SearchFieldItem-origin\"] div").first.click()
        self.page.locator("[data-test=\"PlacePickerInput-origin\"] [data-test=\"SearchField-input\"]").fill("rtm")
        self.page.get_by_role("button", name="Rotterdam, Netherlands Add").click()

    def set_arrival_mad(self):
        self.page.locator("[data-test=\"PlacePickerInput-destination\"] [data-test=\"SearchField-input\"]").click()
        self.page.locator("[data-test=\"PlacePickerInput-destination\"] [data-test=\"SearchField-input\"]").fill("mad")
        self.page.get_by_text("Madrid, Spain").click()

    def set_future_date(self):
        self.page.get_by_text("Departure").click()
        future_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        self.page.locator(f"[data-value=\"{future_date}\"]").click()
        self.page.locator("[data-test=\"SearchFormDoneButton\"]").click()

    def uncheck_accommodation(self):
        self.page.locator("[data-test=\"bookingCheckbox\"] svg").click()

    def search(self):
        self.page.locator("[data-test=\"LandingSearchButton\"]").click()