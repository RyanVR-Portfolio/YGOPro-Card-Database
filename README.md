# YGOPro-Card-Database
The following documentation will introduce you to the implementation structure and the strategy used to build a complete E2E UI test. As well as extending into API automation to build tests to confirm the API and the UI behave is parallel. 

## Intent
To create a series of automated tests for the [Yu-Gi-Oh! Card Database](https://ygoprodeck.com/card-database/). 

This is an independent project to help build a portfolio for my documentation and automation code skills using [Playwright](https://playwright.dev/python/), PyTest, and Python.

The Yu-Gi-Oh! Card Database has a free API which I will be utilizing as well.

## Strategy
For the UI portion of testing I begin with the playwright codegen tool. I clicked each UI element which I perceived as relating to this project's scope. 

This builds individual locators which I then clean up manually. I also find additional elements which I add manually.

Secondary to the locators are our baseline test commands. Essentially just the result of taking the click action to generate locators. I examine each of these structures to modify them for actual functionality. 

These will be used to create tests easily from assembled commands.

Those tests will include both grid and panel view, with and without fuzzy search.

After the UI portion has been completed, API will be automated as well to run tests in parralel to the UI testing. 

The results from the API and the results from the UI can then be collected and compared to confirm parity.

Once the "happy path" has been completed, I will advance to negative testing.

This strategy is fluid, or AGILE, as well. If a time comes when creating a negative test immediately is a better plan I can move to it immediately, for example. 

# File Structure
WIP

# Test Commands
WIP
