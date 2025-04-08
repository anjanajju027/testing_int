from pages.home_page import HomePage

def test_string_result(driver):
    driver.get("https://agrichain.com")  # Use correct URL
    home = HomePage(driver)

    home.enter_input("abcabcbb")
    home.click_submit()
    result = home.get_result()

    assert result == "abc", f"Expected 'abc', but got '{result}'"
    