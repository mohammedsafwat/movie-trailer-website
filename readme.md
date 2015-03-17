Python server-side code to store a list of favorite movies, including box art imagery and a movie trailer URL. Data is
served as a web page allowing visitors to review their movies and watch the trailers.

Steps to run the application:
- Run the __init__.py file, it's the main application file that calls the fresh_tomateos.py file that's
responsible for generating HTML and CSS from the input python code. after you run the __init__.py
you will find a generted file called fresh_tomateos.html, this is the generated html file for the website.

Classes:
- Video.py : The main class that includes the most common features between subtypes of "Video". Subtypes can be
"Show", "Movie", "Clip", or anything related.
- Movie.py : A sub-class of Video.py class that holds the properties and methods of a "Movie" type.
- Show.py : A sub-class of Show.py class that holds the properties and methods of a "Show" type. 
- __init__.py : The main class that's used to run the application and holds several instances from either the "Movie"
or "Show" classes.
