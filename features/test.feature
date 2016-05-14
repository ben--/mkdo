Feature: Showing off behave

  Scenario: Run a simple test
    Given a prompt in a source directory
     When the user runs "mkdo create build"
     Then a "do/build" script is created
