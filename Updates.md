The following enahncements were made to the previous code by team 64
# 1. Revamped UI - A complete UI update was made to improve the style and user experience.
Why was most of the UI changed?

- Firstly, to improve the design and style of the application, as it was a bit dull, focused on basic functionality and was not a very good user experience.
- Secondly, most of the UI was written using class based React and we wanted to modernize and make it easier for the dev community to make changes by upgrading to functional React. So now beginners can make changes quickly and can use most of the modern libraries like Material UI, Recharts, etc that provide top quality, reusable components based on functional react.

Here are some screenshots of the UI upgrades:

A. Applications Page

The previous UI required a number of button clicks to move an application from one column to another. Now all you have to do is drag and drop the application and it states gets updated! We implemented this using the DragNDrop react library!


B. Resume Page

C. Login Page

D. Signup Page

# 2. Add Notes to Jobs and Email Job Details
We now support adding notes to your saved job applications so you don't forget it! Also job details can now be shared to any email id.

# 3. Statistics Page
We added a new page that displays metrics for the users job search. It shows graphs of the number of jobs created over the past 6 months, a ob search funnel graph of the number of jobs saved (wishlisted), number of applications submitted, number of interviews given, etc. We also show the user their latest activity, which is the applications that were recently created or updated.


# 4. Network Page
The network page allows users to quickly save contacts and grow their network so its easy to reach out when applying for jobs. They can also export their contacts to a CSV file!


# 5. Resume Viewer
The resume page now allows users to view their resume in the browser itself, instead of needing to download it to view it. They can also directly print teir resume from this tab!


# 6. Repo Quality

### A. Documentation

##### API Documentation
We have generated API documentation using pydoc3 and hosted it on github pages. Previously the API docs were incomplete and stored in a readme file.

##### Tutorials
We have added mini tutorial GIFs to make it easier for new users to follow and understand how the application works.

##### Troublesooting guides
We have updated the troubleshooting guides and added solutions to issues we identified and resolved while developing the application.

### B. Testing
We added unit tests to increase the coverage score from 30% to 60% and have atleast one unit test for each endpoint. We also configured the pytest_ci.yml github action to run tese tests whenever a commit is made and to push the coverage report to codecov.

### C. Readme
We've added a lot of badges and updated most of the readme to make it easy to uderstand whats going on for someone new and so that you can quickly setup and use the project.

