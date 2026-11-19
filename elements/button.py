import allure
from playwright.sync_api import Page, expect, Locator
from elements.base_element import BaseElement
from elements.ui_coverage import tracker
from tools.logger import logger, get_logger
from ui_coverage_tool import ActionType, SelectorType

logger = get_logger("BUTTON")


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is enabled'

        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_enabled()

        self.track_coverage(ActionType.ENABLED, nth, **kwargs)

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disabled'

        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

        self.track_coverage(ActionType.DISABLED, nth, **kwargs)

    
