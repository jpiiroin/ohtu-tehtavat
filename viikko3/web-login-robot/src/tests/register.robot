*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalleaaa
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Register Credentials
    Page Should Contain  Error, username is less than 3 characters

Register With Valid Username And Too Short Password 
    Set Username  kallebee
    Set Password  ka
    Set Password Confirmation  ka
    Register Credentials
    Page Should Contain  Error, password is less than 8 characters

Register With Nonmatching Password And Password Confirmation
     Set Username  kallecee
     Set Password  kalle123
     Set Password Confirmation  kalle223
     Register Credentials
     Page Should Contain  Error, passwords do not match

*** Keywords ***
Register Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}