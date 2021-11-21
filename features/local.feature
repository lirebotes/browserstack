Feature: launch site and login
    Scenario: Site comes up
        #When I visit url "http://localhost:3000/"
        When I visit url "http://www.bstackdemo.com/"
        Then title is "StackDemo"
        Then the page contains "Offers"
    
    Scenario: Login
        Given my username is "demouser"
        And my password is "testingisfun99"
        #When I visit url "http://localhost:3000/"
        When I visit url "http://www.bstackdemo.com/"
        And I sign in
        Then the page contains "demouser"