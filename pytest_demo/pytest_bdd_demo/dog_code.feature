Feature: Dog Code

  Scenario Outline: Dog Code
    Given I can access dog api
    When I do a GET request on dog api with status code <code>
    Then I should get a success response with status code <response_code>
      Examples:
        |code  | response_code |
        | 200  | 200           |
        | 100  | 200           |