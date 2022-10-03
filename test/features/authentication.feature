
Feature: Authentication
    @wip
    Scenario: Authenticate user "mateo@mateo.com" with password "mateo"
        Given A user with email "mateo@mateo.com" and password "mateo" exists
        When I try to authenticate with email "mateo@mateo.com" and password "mateo"
        Then The authentication is successful for email "mateo@mateo.com"
