# note_app_wi

##Notes app using django
**Curl for sign up**
<sub> curl --header "Content-Type: application/json" \ --request POST \ --data "{\"username\":\"newuser\",\"password\":\"newpass\"}" \ http://127.0.0.1:8000/noteapi/signup/ </sub>

**Curl for log in**
<sub> curl --header "Content-Type: application/json" \ --request POST \ --data "{\"username\":\"newuser\",\"password\":\"newpass\"}" \ http://127.0.0.1:8000/noteapi/login/ </sub>
Signup Functionality
![signup](https://user-images.githubusercontent.com/39771769/224467200-2f997ade-97f6-4d45-a22e-b394fc6dae9d.JPG)

Login Functionality
![image](https://user-images.githubusercontent.com/39771769/224467228-ffba0d05-2ecd-42df-a7b8-6d42eb3c3b29.png)

Add a new note

![image](https://user-images.githubusercontent.com/39771769/224467313-a661a58d-4af2-43cf-b6ff-3ef90514bd3b.png)

**SuperUser functionalities**

User groups are divided into **allowed users** and only **only read allowed users**, superuser can allow a user to login through admin and either add note or only view note by putting them in group,

For allowing a user to login through admin, superuser should grant staff status to the particular user to allow him to login and view their notes
