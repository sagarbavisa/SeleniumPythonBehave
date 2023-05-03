Feature: Test Chick-fil-a application

    Scenario:Test create new region
        Given User is on STEP Login page
        When user Enters Username
        When user Enters Password
        When user click on Login button
        When user click on location user portal WebUi
        When after succesfull login user click on link Create New Region on widget
        When user enters Region Name and user clicks on next button
        When user navigates to "region details page"
        When user enters Start Date in Region Details page
        When user clicks on Create button
        Then confirmation pop-up is displayed

    Scenario:Create area support team
        Given User is on location user portal page
        When user click on link "Create New Area Support Team" on widget
        When user click on node in text field of "Parent Region Node" to select region names
        When user selects parent region node from search option
        When user enters <Area Support Team Name>
        When user click on "Next" button
        Then user should see successful message <pop-up>
        When user enters <Area Support Team Code> in general attributes tab
        When user enters <Area Support Team Type> in general attributes tab
        When user enters <Start Date> in general attributes tab
        When user enters <Assignment Start Date> in general attributes tab
        When user selects Active Area Support Team Roles tab
        When user click on "Add roles" select <Reference Type> and <Reference Target>
        When user selects "Assignment start date" for each role
        When user clicks on "Create" button
        Then user should see successful message <pop-up> on dashboard