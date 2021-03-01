*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123
    Output Should Contain  Error, username is less than 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle
    Output Should Contain  Error, password is less than 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekal
    Output Should Contain  Error, password contains only characters




*** Keywords ***
Input New Command And Create User
    Input New Command