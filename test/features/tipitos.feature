Feature: Tipitos

    Scenario: Create first tipito
        Given There are 0 tipitos
        When I create the tipito "mateo"
        Then The tipito "mateo" exists in the platform
