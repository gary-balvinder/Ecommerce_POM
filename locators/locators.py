from selenium.webdriver.common.by import By


class LoginLocators:

    # LoginPage elements
    username_ = "._2IX_2-.VJZDxU"
    password_ = "._2IX_2-._3mctLh.VJZDxU"
    #login_button = "_.2KpZ6l._2HKlqd._3AWRsL"
    login_button = "// button[contains(., 'Login')]"
    message = "//span[contains(text(),'Your username or password is incorrect')]"

    # Search element
    search_bar = "q"
    search_results = "._1YokD2._3Mn1Gg"

    # Results page elements
    brand_ = "[title='HP'] ._3879cV"
    product_ = "//a[contains(text(),'HP')]"

    # Add to cart element
    add_to_cart = "._2KpZ6l._2U9uOA._3v1-ww"

    # cart element
    cart = "//span[contains(text(),'Cart')]"

    # Remove from cart element
    remove_from_cart = "//div[contains(text(),'Remove')]"
    remove = ".\\_1AtVbE:nth-child(2) .\\_3dsJAO:nth-child(2)"
    remove_button = "._3dsJAO._24d-qY.FhkMJZ"
