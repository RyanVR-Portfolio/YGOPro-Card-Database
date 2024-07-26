# tests/test_ygo_card_db_search.py

import pytest
from playwright.sync_api import sync_playwright
from page_objects.ygo_card_db_page import YGOCardDBPage

def test_ygo_card_db_search():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        ygo_page = YGOCardDBPage(page)
        ygo_page.open()
        #ygo_page.click_heading()
        #ygo_page.click_home_link()
        #ygo_page.click_breadcrumb()
        ygo_page.click_searchbox()
        ygo_page.click_description_text()
        ygo_page.click_halve_atk_text()
        ygo_page.click_use_description_text()
        ygo_page.click_fuzzy_search()
        ygo_page.click_filter_button()
        ygo_page.select_filter_limit("100") #options: 24, 30, 50, 100
        ygo_page.click_grid_view()
        ygo_page.click_list_view()
        ygo_page.click_prev_page()
        ygo_page.click_next_page()
        #ygo_page.click_page_info()
        ygo_page.click_api_area_results()

        browser.close()
