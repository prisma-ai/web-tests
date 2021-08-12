import config
from pages.signin import SignIn
from pages.welcome_overlay import WelcomeOverlay


def test_click_continue_button_without_email_return_error(page):
    """ Clicking continue button with empty email should return error. """

    page.goto(config.url_stage)
    overlay = WelcomeOverlay(page)
    sign_in = SignIn(page)

    overlay.check_elements()
    overlay.close_overlay()
    sign_in.open_sign_in_modal()
    sign_in.click_continue()
    sign_in.check_error_message_displayed()


