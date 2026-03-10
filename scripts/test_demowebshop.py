from POM.homepage import HomePage
from POM.loginpage import LoginPage
from POM.desktop_page import DesktopPage
from POM.simp_comp_page import SimpleComputerPage
from POM.cartpage import CartPage

from generic_utilities.excel_utility import read_excel

data = read_excel()
## {'valid_email': 'steve.jobs123@gmail.com', 'valid_pwd': 'stevejobs', 'country': 'India', 'pincode': 5632014.0, 'sortby': 'Price: Low to High', 'viewas': 'List'}


def test_case1(setup):
    hp = HomePage(setup)
    lp = LoginPage(setup)
    dp = DesktopPage(setup)
    sp = SimpleComputerPage(setup)
    cp = CartPage(setup)

    hp.click_on_login_link()
    lp.enter_email(data['valid_email'])
    lp.enter_pwd(data['valid_pwd'])
    lp.click_on_login_btn()
    hp.verify_logout_btn()
    hp.hover_to_computers()
    hp.click_on_desktops()
    dp.select_sortby(data['sortby'])
    dp.select_viewas(data['viewas'])
    dp.scroll_pagedown()
    dp.click_on_simp_com()
    sp.select_processor()
    sp.click_on_addtocart()
    sp.scroll_to_home()
    sp.click_on_shoppingcart()
    cp.select_country(data['country'])
    cp.clear_pincode_textbox()
    cp.enter_pincode(data['pincode'])
    cp.click_on_terms_service()
    cp.click_on_checkout()























































































