# Little-Lemon

Hello! API views will depend on what user you are signed in as below. Please use one or both of the tokens below to see differences in how the API behaves<br>
For full access to create/read/update/delete, please choose Manager but feel free to chose the User to compare authorization schemes:<br>

**Manager** (This can see all bookings, create bookings with other names, as well as delete, update and create menu items)<br>
598182b8dc9f00fc0ff942c0c2c6edc6d38521d8<br>

**User** (This can see their own bookings, and can only create them for themselves. Can view all or individual menu items but cannot create, destroy or update them)<br>
387870b6bdba9a80076b3ed14819ebd04a12ec77<br>

Note that any of the below links can be visited in brower or tested with Insomnia once the server is running.<br>
Insomnia is ideal if you wish to test the experience between Manger and User authentications<br>

## Available API Views:<br>
**Create User:** http://127.0.0.1:8000/auth/users/<br>
**Aquire Token:** http://127.0.0.1:8000/auth/token/login<br>
**Static HTML Content:** http://127.0.0.1:8000/restaurant/<br>
**Booking (All) View/Create:** http://127.0.0.1:8000/restaurant/bookings/<br>
**Booking (Single) View/Update/Destroy:** http://127.0.0.1:8000/restaurant/bookings/#<br>
**Menu (All) View/Create:** http://127.0.0.1:8000/restaurant/menu/<br>
**Menu (Single) View/Update/Destroy:** http://127.0.0.1:8000/restaurant/menu/#<br>

## Tests<br>
Currently there are two unit tests in place to ensure both the Booking and Menu models are functioning correclty. They can be run by running:<br>

**python .\manage.py test**<br>

In the project folder<br>