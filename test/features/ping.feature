Feature: Ping

    Scenario: Ping a la app
        Given La app esta iniciada
        When Realizo un Ping
        Then Recibo un mensaje "UP"
