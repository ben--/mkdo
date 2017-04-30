Feature: Showing off behave

    Background: A machine with mkdo installed
        Given a fresh machine with mkdo installed

    Scenario: Run a simple test
        Given an empty source directory
        When the user runs "mkdo create build"
        Then a "do/build" script is created
