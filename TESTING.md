# Wild Swim Scotland Testing

Return to [README.md](README.md)

# Code Validation 

## W3C HTML Validation Results

All HTML code has been run through the [W3C HTML Validator](https://validator.w3.org/).

<details>
<summary> W3C HTML Errors Found and fixed</summary>

joined_swims.html

![joined_swmis errors](documentation/testing-images/join-swim-errors.png "join swim error image")

add_swim.html

![add_swim errors](documentation/testing-images/add-swim-errors.png "add swim error image")

![add_swim errors2](documentation/testing-images/add-swim2-error.png "add swim 2nd error image")

edit_swim.html

![edit_swim errors](documentation/testing-images/edit-swim-error.png "edit swim error image")

signup.html

![register errors](documentation/testing-images/register-errors.png "register swim error image")

</details>

After testing all errors were fixed and document checking complete was shown for all pages

![document checking complete](documentation/testing-images/document-ok.png "")

| **SOURCE CODE TEMPLATE** | **RUN THROUGH VALIDATOR** | **ANY ERRORS** | **ERRORS RESOLVED** |
| -------- | ---------- | --------------- | -----------|
| swim_posts.html | Yes | No | N/A |
| joined_swims.html | Yes | Yes - detailed image above | Yes, retested and all passed |
| edit_swims.html | Yes | Yes - detailed image above | No, moved to bug section |
| delete_swims.html | Yes | No | N/A |
| add_swim.html | Yes | Yes - detailed image above | No, moved to bug section |
| signup.html | Yes | Yes - detailed image above | Yes, retested and all passed |
| login.html | Yes | No | N/A |
| logout.html | Yes | No | N/A |

## W3C CSS Validation Results

All custom CSS has been run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "jigsaw w3 page")

No errors were found when running css through w3c validator

![css w3c](documentation/testing-images/css-errors.png "css validator image")

## JSHint Validation Results

No javascript was used for this project.

## CI Python Linter Validation Results

All python code that was written for this project by Sarah Goodwin was developed following PEP8 guidelines and was run through the [CI Python Linter](https://pep8ci.herokuapp.com/ "ci python linter page")

| **Python file** | **RUN THROUGH VALIDATOR** | **ANY ERRORS** | **ERRORS RESOLVED** |
| -------- | ---------- | --------------- | -----------|
| views.py | Yes | Some trailing white spaces | All clear, re-run and no error found |
| urls.py | Yes | All clear, no errors found | N/A |
| modles.py | Yes | 1 trailing white space | All clear, re-run and no error found |
| forms.py | Yes | Line too long (89 > 79 characters) | Added   # noqa and all clear |
| admin.py | Yes | All clear, no errors found | N/A |
| settings.py | Yes | 1 trailing white space | All clear, re-run and no error found |

Final testing showed:

![CI Python Linter](documentation/testing-images/linter-no-errors.png "python linter image")

# Manaul Testing

## Home Page

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Swim Cards | Opened site url | Swim cards are visable | Worked as expected | N/A |
| Nav Links | Opened site url | Only register and login nav links are visable | Worked as expected | N/A |
| Join Swim Buttons | Opened site url | Cannot see Join Swim Buttons | Worked as expected | N/A |

## Register Page

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Registration Form | Clicked on reigster nav link | Register form is displaying | Worked as expected | N/A |
| Username | Typed in @£$%^ as username | Warning will show | Warning showed 'Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.' | Worked as expected |
| Username | Typed in admin as username | Warning will show | Warning showed 'A user with that username already exists.' | Worked as expected |
| Password 1 | Typed in password same as username | Warning will show | Warning showed 'The password is too similar to the username.' | Worked as expected |
| Password 2 | Typed in password different to password1 | Warning will show | Warning showed 'You must type the same password each time.' | Worked as expected |
| Register Button | Click Register | Button takes user to logged in dashboard on homepage | Worked as expected | N/A |
| Login Button | Clicked on login link | Get taken to login page | Worked as expected | N/A |

## Login Page

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Username | Typed in random username | Warning will show | Warned showed 'The username and/or password you specified are not correct.' | Worked as expected |
| Password | Typed in incorrect password | Warning will show | Warned showed 'The username and/or password you specified are not correct.' | Worked as expected |
| Sign In | Typed in correct username and password, pressed sign up | Button takes user to logged in dashboard on homepage | Worked as expected | N/A |
| Sign Up | Clicked on Sign Up link | Get taken to register page | Worked as expected | N/A |

## Homepage as Logged in user

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Join Swim Button | Clicked Join Swim | Swim added to upcoming swims page | Worked as expected | N/A |
| Your Upcoming Swims | Left page and re-clicked on upcoming swims | Previous swims that had been added still there | Worked as expected | N/A |
| Logout | Logout button replaced login button | No login button | Worked as expected | N/A |
| Register | Register button no longer avaliable | No register button | Worked as expected | N/A |

## Upcoming Swims

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| No Swims Joined | Click on upcoming swims without joining a swim | Message 'No swims joined yet' will show | Worked as expected | N/A |
| Joined Swim | Click on join swim button | Swim will be put onto upcoming swim page and redirected | New message showed saying 'Thank you for joining us, we can't wait to see you there!' | Worked as expected |
| Remove Swim | Click remove swim button | Swim will disappear | Swim removed and stayed on upcoming swim page | Worked as expected |

## Logout

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Logout | Clicked logout from nav bar | Message asking 'Are you sure you want to sign out?' | Worked as expected | N/A |
| Sign Out button | Clicked sign out | Redirected to homepage as non logged in user | Worked as expected | N/A |

## Homepage as staff user

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Can see edit and delete buttons | As staff user I can see the edit and delete buttons for only swims I created | Edit and delete buttons appear | Worked as expected | N/A |


## Add Swim

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Add Swim | Clicked Add Swim nav link | Add swim form showed | -----------| ------- |
| Title | Tried to type title | --------------- | -----------| ------- |
| Description | ---------- | --------------- | -----------| ------- |
| Date | ---------- | --------------- | -----------| ------- |
| Time | ---------- | --------------- | -----------| ------- |
| Swim Difficulty | ---------- | --------------- | -----------| ------- |
| Location | ---------- | --------------- | -----------| ------- |
| With image | ---------- | --------------- | -----------| ------- |
| No image | ---------- | --------------- | -----------| ------- |
| Submit | ---------- | --------------- | -----------| ------- |
| New swim added to homepage | ---------- | --------------- | -----------| ------- |

## Edit Swim

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Data prefilled | ---------- | --------------- | -----------| ------- |
| Submit | ---------- | --------------- | -----------| ------- |
| Title | ---------- | --------------- | -----------| ------- |
| Description | ---------- | --------------- | -----------| ------- |
| Date | ---------- | --------------- | -----------| ------- |
| Time | ---------- | --------------- | -----------| ------- |
| Swim Difficulty | ---------- | --------------- | -----------| ------- |
| Location | ---------- | --------------- | -----------| ------- |
| With image | ---------- | --------------- | -----------| ------- |
| No image | ---------- | --------------- | -----------| ------- |
| Submit | ---------- | --------------- | -----------| ------- |
| New swim added to homepage | ---------- | --------------- | -----------| ------- |

## Delete Swim

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Delete Swim | ---------- | --------------- | -----------| ------- |
| -------- | ---------- | --------------- | -----------| ------- |
| -------- | ---------- | --------------- | -----------| ------- |

## Other Testing

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| 404 Error | ---------- | --------------- | -----------| ------- |
| URL Access | ---------- | --------------- | -----------| ------- |

## Responsivness testing

| **DEVICE** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| Samsung22 Ultra | ---------- | --------------- | -----------| ------- |
| iPhone 15 | ---------- | --------------- | -----------| ------- |
| Dev Tools for iPad | ---------- | --------------- | -----------| ------- |

## Browser Compatibility

The site was tested on the following browser types

* Google Chrome
* Microsoft Edge
* Safari

## User Testing

A user testing form was sent to friends and family to test the site on their devices and get real world feedback from people who had not been involved in the creation of the site.

Here is the form that was sent.

![user testing image](documentation/testing-images/user-testing-form.png "user testing form screenshot")

Feedback from the form

* Better responsivness for mobile - added media queries
* User testing did not throw any errors as users followed instructions
* Site was easy to use and user friendly 

# Automated Testing

# Accessibility Testing

## Lighthouse

# Known Bugs

## Resolved

- HTML

- Python

- Other

- Unresolved 

Return to [README.md](README.md)




