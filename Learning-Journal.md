# Slowed Playlist Project - Learning Journey

## Project Summary
Building a slowed playlist application to understand how the internet works.

**Tech Stack:** Spotipy, Google-API-Python-Client, DotENV, Rapidfuzz, YTMusicAPI,
**Goal:** Make an app that can retrieve your Spotify playlist and then makes an equivalent playlist on YouTube 

---

## What I'm Learning

### HTTP
Hypertext Transfer Protocol: Protocol for establishing 
connection between client and server, how two computers talk to each other

- Connectionless: client disconnect from the server, then when the response is ready the server re-establish the connection again and deliver the response
- HTTP is stateless: both computers forget about each other after connection closes

Request HTTP Methods: GET (retrieve data, no request body required), POST (store data in db, takes request body)

Response HTTP Method: 200: ok, 404: file not found 

### URI: Locate resource with both name and location

URL (most common): Locate resource with location 
URN: Locate resource with name

### O-Auth 2.0
Allows you to grant a third-party app access to protected resources without the need for user login

Redirects you to spotify access page where user must approve and when you do then spotify attaches an authentication code to the redirect uri (client) and then client makes a POST request back to Spotify's API with the authentication code, client credentials (client ID, client secret), and redirect URI, which then responds with the Access Token and other relevant info. Then, your app uses that Access Token to access certain features that you specify. 

Client approval → Spotify Access Page → Redirect URI back to Client (with auth code) → POST (auth code + client credentials (client_ID, client_secret) + redirect URI) → GET (access token) → Retrieve info

### Client Credentials Flow
Exchange of ClientID and Client Secret for access code (tied to app only not user)

Example: Client Credentials flow would access Spotify app features (ex: top hits), not user-specific items such as private playlists, liked songs, etc; thus no user login. 

### API URL Headers
- Query Parameters, defined as key-value pairs in the URL and separated by the '&' symbol. They are separated from path parameters with the ? operator
- Ex: https://api.example.com/v1/books?genre=fiction&limit=10. Genre and fiction are our query parameters while books is the path parameter

### PPrint
automatically adds indentation and line breaks, making deeply nested data structures easier to understand for example multidimensional arrays, dictionaries, tuples, etc. 

pprint.pprint() to pretty print

---

---

## Daily Progress

### Day 1 - [8/28/2025]
For today, we successfully implemented spotipy API and got it to successfully parse through my entire "crack" playlist and retrieve the track names. Today, I learned about how computers communicate via the HTTP Protocol, what is a URI, URL, and URN, OAuth 2.0 with authorization flow and client credentials flow, how to use the os module alongside the dotenv module to retrieve environment variables, and read through some of the documentation of the spotipy library. Finally, I learned about the pprint library to print higher-dimensional iterables in a clean easy-to-read format.

### Day 2 - [8/29/2025]
Today, we successfully implemented the create playlist feature inside of the YouTube data v3 API and made a sample test playlist. we learned about how to instantiate an OAuth object with the API and how to give it the correct permissions. Also, we learned that we can establish our client on a different port than 8080. Also we learned about the methods associated with each object such as .playlists.insert() where we learned what the "part" parameter does with controlling what should be returned. In our case, we returned the snippet and status of the playlist. Also, we learned about JSON response bodies and that POST requests take them as input but not GET requests as by essence, request bodies are data sent to the API. .playlists().insert() is a POST request that instructs the YouTube API to create a new playlist with the request body's JSON parameters. .execute() is what's responsible for making the request. 
