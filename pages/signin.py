from pages.base import BasePage


class SignIn(BasePage):

	def _sign_in_button(self):
		return self.page.wait_for_selector('//*[text()="Sign In"]')

	def _email(self):
		return self.page.wait_for_selector('.bZHjKd.iXyzRG')

	def _continue_button(self):
		return self.page.wait_for_selector('.gnliEL.jWCFlK')

	def _error_message(self):
		return self.page.wait_for_selector('//*[text()="Enter an email address"]')

	def open_sign_in_modal(self):
		self._sign_in_button().click()

	def set_email(self, email: str):
		self._email().fill(email)

	def click_continue(self):
		self._continue_button().click()

	def check_error_message_displayed(self):
		self._error_message()
