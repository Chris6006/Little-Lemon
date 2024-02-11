# Little-Lemon

Hello! API views will depend on what user you are signed in as below. Please use one or both of the tokens below to see differences in how the API behaves
For full access to create/read/update/delete, please choose Manager but feel free to chose the User to compare authorization schemes:

Manager (This can see all bookings, create bookings with other names, as well as delete, update and create menu items)
598182b8dc9f00fc0ff942c0c2c6edc6d38521d8

User (This can see their own bookings, and can only create them for themselves. Can view all or individual menu items but cannot create, destroy or update them)
387870b6bdba9a80076b3ed14819ebd04a12ec77

Available API Views:
Create User: http://127.0.0.1:8000/auth/users/
Aquire Token: http://127.0.0.1:8000/auth/token/login
Static HTML Content: http://127.0.0.1:8000/restaurant/
Booking (All) View/Create: http://127.0.0.1:8000/restaurant/bookings/
Booking (Single) View/Update/Destroy: http://127.0.0.1:8000/restaurant/bookings/#
Menu (All) View/Create: http://127.0.0.1:8000/restaurant/menu/
Menu (Single) View/Update/Destroy: http://127.0.0.1:8000/restaurant/menu/#