Feature: Showing off behave

  Scenario: Run a simple test
    Given an empty source directory
     When the user runs "mkdo create build"
     Then a "do/build" script is created
