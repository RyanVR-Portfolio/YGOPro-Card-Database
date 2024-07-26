# page_objects/ygo_card_db_page.py

from playwright.sync_api import *

class YGOCardDBPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://ygoprodeck.com/card-database/"
        self.heading = page.get_by_role("heading", name="Card Database")
        # self.home_link = page.get_by_role("link", name="Home")
        self.breadcrumb = page.get_by_label("breadcrumb").get_by_text("Card Database")
        
#   Page Navigation Objects
#       Search        
        self.searchbox = page.locator('input[type="search"][name="deckName"][placeholder="Search Yu-Gi-Oh! Cards..."]')
        # self.description_text = page.get_by_text("description/text")
        # self.halve_atk_text = page.get_by_text("*halve the atk")
        self.use_description_text = page.get_by_text("Use * to give description/")
        self.fuzzy_search_toggle = page.locator('#fuzzySearch')
        self.fuzzy_search_label = page.locator('label[for="fuzzySearch"]')

#       View Adjustments
        self.filter_button = page.locator('button[data-target="#toggleSearchFilters"]')
        self.filter_limit = page.locator("#filter-limit")
        self.grid_view = page.get_by_title("Grid View")
        self.list_view = page.get_by_title("List View")

#       Results
        self.prev_page = page.locator("#prevPage")
        self.next_page = page.locator("#nextPage")
        # self.page_info = page.get_by_text("Page 2/557 of 13,354 total").first # Needs to be split into page #/total and total individual results
        # self.api_area_results = page.locator("#api-area-results") # Realized YGO Pro has a free API. Look into combining that with the field for testing.
        self.card_result_area = page.locator(f'div.item-area[title="{card_name}"]') # Variable unset for now. Thinking how to best handle it.

#   Filter Panel Objects
        self.filter_by_type = page.locator("#filter-type")
        self.filter_by_attr = page.locator("#filter-attribute")
        self.filter_by_race = page.locator("#filter-race")
        self.filter_by_archetype = page.locator("#filter-archetype")
        self.filter_by_rarity = page.locator("#filter-rarity")
        self.filter_by_format = page.locator("#filter-format")
        self.filter_by_effect = page.locator("#filter-effect")
        self.select_tcg_set = page.get_by_placeholder("Select TCG Set...") #See documentation for options
        self.select_ocg_set = page.get_by_placeholder("Select OCG Set...") #See documentation for options
        self.filter_by_atk = page.locator("#atkLabel") #Filter by Attack = 0-5000 inclusive. Most often increments of 25, 50, 75, or 100. (1050, 1525, etc)
        self.filter_by_def = page.locator("#defLabel") #Filter by Defense = 0-5000 inclusive. Most often increments of 25, 50, 75, or 100. (1050, 1525, etc)
        self.filter_by_lvl = page.locator("#levelLabel") #Filter by level = 0-12 inclusive
        self.filter_by_links = page.locator("#linkLabel") #Filter by Link arrows = 0-6 inclusive
        self.filter_by_pdlmscale = page.locator("#scaleLabel") #Filter by Pendulum Scale = 0-13 inclusive
        self.filter_rls_date_from = page.get_by_label("Release Date From")
        self.filter_rls_date_to = page.get_by_label("Release Date To")
        self.filter_by_rls_lang = page.locator("#filter-language")
        self.filter_sort_by = page.locator("#filter-sort")
        self.filter_sort_dir = page.locator("#filter-sort-direction")
        self.reset_filter = page.get_by_role("button", name="Reset Filters")

    def open_dbhome(self):
        self.page.goto(self.url)
        expect(self.page).to_have_url(self.url)

    def confirm_heading(self):
        expect(self.heading).to_be_visible()
        expect(self.heading).to_have_text(self.heading)

    # def click_home_link(self):
    #     self.home_link.click()

    def confirm_breadcrumb(self):
        expect(self.breadcrumb).to_be_visible()
        expect(self.breadcrumb).to_have_text(self.breadcrumb)

    def enter_searchbox(self):
        self.searchbox.focus()
        expect(self.searchbox).to_be_visible
        expect(self.searchbox).to_be_focused

    def click_description_text(self):
        self.description_text.click()

    def click_halve_atk_text(self):
        self.halve_atk_text.click()

    def click_use_description_text(self):
        self.use_description_text.click()

    def click_fuzzy_search(self):
        self.fuzzy_search.click()

    def click_filter_button(self):
        self.filter_button.click()

    def select_filter_limit(self, value: str):
        self.filter_limit.select_option(value)

    def click_grid_view(self):
        self.grid_view.click()

    def click_list_view(self):
        self.list_view.click()

    def click_prev_page(self):
        self.prev_page.click()

    def click_next_page(self):
        self.next_page.click()

    def click_page_info(self):
        self.page_info.click()

    def click_api_area_results(self):
        self.api_area_results.click()
