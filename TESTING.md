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

All custom javascript code has been run through [JSHint](https://jshint.com/ "js hint page").

![js hint](documentation/testing-images/js-hint.png "js hint image")

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

![CI Python Linter](documentation/testing-images/linter-no-errors.png "python linter image")

# Manaul Testing

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| -------- | ---------- | --------------- | -----------| ------- |


## Responsivness testing

| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** | **FIX** |
| -------- | ---------- | --------------- | -----------| ------- |
| -------- | ---------- | --------------- | -----------| ------- |

## Browser Compatibility

## User Testing

A user testing form was sent to friends and family to test the site on their devices and get real world feedback from people who had not been involved in the creation of the site.

You can view their responses here:

![user testing image](documentation/testing-images/user-testing-form.png "user testing form screenshot")

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




