from pages.base import BasePage


class WelcomeOverlay(BasePage):

    def _overlay_title(self):
        return self.page.wait_for_selector('.sc-gsDJrp.dWtYYw.sc-faUofl')

    def _overlay_description(self):
        return self.page.wait_for_selector('.sc-gsDJrp.iWPFkv.sc-GamvQ')

    def _overlay_button(self):
        return self.page.wait_for_selector('.gnliEL.GjNLh')

    def check_elements(self):
        self._overlay_title()
        self._overlay_description()
        self._overlay_button()

    def close_overlay(self):
        self._overlay_button().click()
