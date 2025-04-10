# HBNB Part 4 : Auth & API

## Version 1.0.0

## Disclaimer
For more information about this project, please refer to these README :
[Link to main README](../../README.md)
[Link to part1 README](../../part1/README.md)
[Link to part2 README](../../part2/README.md)
[Link to part3 README](../../part2/README.md)


## Intro  
After setting up the project structure in Part 1, implementing the business logic and RESTful API endpoints in Part 2, and enhancing the backend with authentication and database integration in Part 3, we now arrive at the final stage — Part 4.

Unlike the previous parts, this section was completed individually, giving us more creative freedom, especially in designing a visually appealing frontend.

For this reason, I decided to rebrand the project from **HBnB** to **Airbnbear**, giving it a fresh and personal touch.


### Explanation

#### HTML
The HTML file was provided as part of the exercise.
I made some slight adjustments to improve the design and layout.

It could still be improved — for example, by adding a "Go back" button or other interactive elements.

#### CSS
The CSS file was also provided.
I tweaked it a bit to enhance the design and added a few fun features, such as animated hover effects.

While it works, there’s definitely room for improvement in terms of responsiveness and structure.

#### Security, Scalability & Improvements
This project is a demo intended to showcase my skills. However, I’m aware that there are several limitations and areas for improvement:

- CORS is currently open to all origins, which isn’t secure for production.
- The app doesn’t use a proper frontend web server.
- Some features are missing (e.g., adding a rating in reviews, showing amenities, allowing users to create places).
- Flask is running with the built-in development server, which isn’t suitable for production.
- No real automated testing has been implemented — only manual/visual tests.
- And probably a few other things I forgot...

This project is a solid foundation but not production-ready — and that’s okay. It’s all part of the learning process.

#### JS


## Getting started
**Disclaimer : These explanations was tested on my Linux machine. So it's valid on a Linux system only.**

### Prerequisite
- `Linux system` (tested on Linux Mint 22.1 x86_64 with 6.8.0-52-generic kernel )
- `Python3` (version 3.12.3)
- `venv`
- `browser` (tested on Firefox 136.0.4 and GNOME Web 46.0)
Additional :
- `Postman` (for testing only)
- Somes SQL tools if you want to manipulate database

### Installation
1. Clone / download the repository
`git clone https://github.com/OursBlanc42/holbertonschool-hbnb`

2. Go to the right directory
`cd holbertonschool-hbnb/part4/hbnb`

3. Setup a virtual environnement 
`python3 -m venv venv`

4. Activate virtual env
`source venv/bin/activate`

5. Install the Python packages needed for the project. There are listed in requirements.txt as explained before.
`pip install -r requirements.txt`

6. From this virtual environnement you can now run the script (more detail below)
`./setup.sh`

7. If everything has gone well, the terminal should display something like : 
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
Admin user already exists. Check the README for default credentials.
 * Debugger is active!
 * Debugger PIN: 112-991-365

```

8. Now, you can open the `part4/index.html` in your favorite browser !

9. Optionnal : You can also try the API with cURL, Postman, Swagger web UI, or whatever... You can find more information about this in part 3 of the project.


### Testing 
For this part of the project, la plupart des tests ont été visuel dans le sens ou je naviguais sur le site web avec différents cas d'usage.
J'ai également fait quelques tests with a Postman collection. You can find the Postman file in the `hbnb/tests` directory.

Il est à noté que certains de ces tests échouent (surtout pour les cas particuliers et certains scénarios exotiques), certainement des erreurs à corriger entre le back et la DB.

### Script
Afin de faciliter l'installation j'ai créé un script en bash qui effectue les opérations suivantes :
- Créer la database
- Créer les tables dans la database
- Populer les tables de la database avec des données pour la démo
- Lancer le serveur back-end

### Données de démo
Le fichier SQL qui popule la db avec des données pour la démo crée trois utilisateurs, des places, des reviews, et des commodités (qui ne sont pas encore implémenté actuellement coté front-end)

#### Users
As mentioned earlier, three users have been created for testing purposes.
You can use the following credentials to log in:

##### John Doe  
- **Email:** `john@example.com`
- **Password:** `azerty123`
- **Role:** Regular user (not admin)

##### Jane Doe  
- **Email:** `jane@example.com`
- **Password:** `azerty123`
- **Role:** Regular user (not admin)

##### Admin  
- **Email:** `admin@example.com`
- **Password:** `admin123`
- **Role:** Administrator



