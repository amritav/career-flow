The following enahncements were made to the previous code by team 64
# 1. Revamped UI - A complete UI update was made to improve the style and user experience.
Why was most of the UI changed?

- Firstly, to improve the design and style of the application, as it was a bit dull, focused on basic functionality and was not a very good user experience.
- Secondly, most of the UI was written using class based React and we wanted to modernize and make it easier for the dev community to make changes by upgrading to functional React. So now beginners can make changes quickly and can use most of the modern libraries like Material UI, Recharts, etc that provide top quality, reusable components based on functional react.

Here are some screenshots of the UI upgrades:

#### A. Applications Page

The previous UI required a number of button clicks to move an application from one column to another. Now all you have to do is drag and drop the application and it status gets updated! We implemented this using the DragNDrop react library!

Previous Home Page
![old_home_screen](https://github.com/adi-kiran/career-flow/assets/36990588/7548b336-4947-4245-8d4c-cc88aab37fe0)

Updated Home Page
![HomePage-NavClosed](https://github.com/adi-kiran/career-flow/assets/36990588/9e9e8628-9a5e-4b37-b7ea-f2c2f803ccf0) 

#### B. Resume Page

Previous Resume Page
![old_resume](https://github.com/adi-kiran/career-flow/assets/36990588/56b214de-1ec4-4afb-87fd-b087e9aada45)

Updated Resume Page
![ResumePage-NavClosed](https://github.com/adi-kiran/career-flow/assets/36990588/ea54e170-f822-4bb4-82f7-4ea7fa0b2225)

#### C. Login Page

Previous Login Page
![old_login](https://github.com/adi-kiran/career-flow/assets/36990588/f266bca6-c4f4-4e07-9317-b3bf77b0bcc1)

Updated Login Page
![LoginPage](https://github.com/adi-kiran/career-flow/assets/36990588/776ab398-f1cc-409a-9927-50e3ce99e489)

# 2. Add Notes to Jobs and Email Job Details
We now support adding notes to your saved job applications so you don't forget it! Also job details can now be shared to any email id. (GIF in [Tutorials.md](https://github.com/adi-kiran/career-flow/blob/main/Tutorials.md))

# 3. Statistics Page
We added a new page that displays metrics for the users job search. It shows graphs of the number of jobs created over the past 6 months, a ob search funnel graph of the number of jobs saved (wishlisted), number of applications submitted, number of interviews given, etc. We also show the user their latest activity, which is the applications that were recently created or updated. (GIF in [Tutorials.md](https://github.com/adi-kiran/career-flow/blob/main/Tutorials.md))

# 4. Network Page
The network page allows users to quickly save contacts and grow their network so its easy to reach out when applying for jobs. They can also export their contacts to a CSV file! (GIF in [Tutorials.md](https://github.com/adi-kiran/career-flow/blob/main/Tutorials.md))

# 5. Resume Viewer
The resume page now allows users to view their resume in the browser itself, instead of needing to download it to view it. They can also directly print teir resume from this tab! (GIF in [Tutorials.md](https://github.com/adi-kiran/career-flow/blob/main/Tutorials.md))

# 6. Repo Quality

### A. Documentation

##### API Documentation
We have generated API documentation using pydoc3 and hosted it on github pages. Previously the API docs were incomplete and stored in a readme file. [Documentaation](https://adi-kiran.github.io/career-flow/)

##### Tutorials
We have added mini tutorial GIFs to make it easier for new users to follow and understand how the application works. [Tutorials.md](https://github.com/adi-kiran/career-flow/blob/main/Tutorials.md)

##### Troublesooting guides
We have updated the troubleshooting guides and added solutions to issues we identified and resolved while developing the application. [Troubleshooting.md](https://github.com/adi-kiran/career-flow/blob/main/Troubleshooting.md)

### B. Testing
We added unit tests to increase the coverage score from 30% to 60% and have atleast one unit test for each endpoint. We also configured the pytest_ci.yml github action to run tese tests whenever a commit is made and to push the coverage report to codecov.

### C. Readme
We've added a lot of badges and updated most of the readme to make it easy to uderstand whats going on for someone new and so that you can quickly setup and use the project.

