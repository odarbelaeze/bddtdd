Feature: homepage
    I should have a homepage

    Scenario: It worked
        When i visit the homepage
        Then i should see "Welcome to Django" in the title
