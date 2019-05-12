Links: 
- https://nandn.herokuapp.com/
- https://github.com/NeilJain56/prinProg

Description: 
- This project focuses on implementing popular and custom encryptions and decryptions. There are four sections each with a different encryption and decryption pair. Simply type in a string and watch it get encrypted or decrypted in live time!

How to use:
- First enter the website https://nandn.herokuapp.com when the entire project is live and running. On this website the top left box of each section is where the string you wish to be encrypted can be typed. As you type your encrypted string will output on the box below it. Then in order to decrypt the encrypted string put it in the top right box and watch the string get decrypted. 

Subtle but important things to remember when using this site: 
- After typing in your desired string, add a space or click enter so the last letter can be rendered 
- Do not use special characters and try your best to avoid capital letters because these can cause errors such as in the last encryption


How it was made:
- The creation of this site first started with fiddling with react.js to create a good looking front-end that would serve its purpose. We made sure the data was accessible so when needed we could send it to the python server. Next we created the python server using Flask. Though we had both the server and the front end made, the connection between the two was missing so we spent several hours trying to get them to connect. After successfully passing the data through we had to write all the encryptions which was also difficult. Finally after having tested on our local machine we put it on the internet which required a lot of extra packages and even files to get it successfully hosted.  


Errors along the way/ things learned 
- There were a plethora of errors from the very beggining of this project. Both learning react.js along with Flask to create a fully functional web application caused several errors. Some big errors included incorporating Flask with the front end so the python code could be run on the user input. Another large problem was styling a responsive and effective front-end that served its purpose. Lastly, a large error included actually hosting the website for the public to use because heroku requires several objects in order to do so. In order to overcome these errors we used several websites such as StackOverflow and several articles. Furthermore, we watched hours of youtube videos including a 3 hour crash course on react.js which taught all the basics and Flask tutorials as well. 



