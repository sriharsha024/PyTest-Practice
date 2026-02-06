@bddparam
Feature: Parameterizing tests in PyTest BDD

  Scenario: Check varieties of fruit
    Given There are 3 varities of fruits
    When We add a same variety of fruit
    Then There is a same count of varieties
    When if we add a different variety of fruit
    Then The count of varities increases to 4

  Scenario: Parameterize benefits
    Given There are 5 fruits
    When I eat 3 fruits
    And I eat 2 fruits
    Then I should have 0 fruits
