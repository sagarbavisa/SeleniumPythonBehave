Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I Launch chrome browser
    When I open orange hrm Homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must sucessfully login to the Dashboard page

  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given I Launch chrome browser
    When I open orange hrm Homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must sucessfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | admin    | adminxyz |