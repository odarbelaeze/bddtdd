Feature: homepage
    I should have a homepage

    Scenario:
        When i visit the homepage
        Then i should see "TaskBuster" in the title

    Scenario:
        When i visit the homepage
        Then i should see a pink title
