import pytest
from playwright.async_api import Page

from pages.sauce.inventory import SauceInventoryPage
from pages.sauce.login import SauceLoginPage


@pytest.fixture
def login_page(page: Page) -> SauceLoginPage:
    return SauceLoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> SauceInventoryPage:
    return SauceInventoryPage(page)