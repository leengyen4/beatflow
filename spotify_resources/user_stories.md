User Stories -- Spotify Clone

--Login
1. Upload Button on Login
2. Profile Button on Login
3. Following/Follower other Users (BONUS)
4. Users: See all personal Albums, Playlists, Songs, Liked Songs
5. Error Handling: Success/Failure message
6. Edit songs, playlists, albums, profile
7. Play button footer should show up.

--SignUp
1. Username, Name, email, password, DOB,
2. Signup Page instead of multiple
3. Email + Password field
4. Ask for name, DOB, gender
5. When signup finished, redirect to homepage
6. unregistered users cannot upload, like, create playlist.
"7. Choose to be an artist or listener"
    - different signup for artist vs listener
    - listeners cannot upload songs
    -


--Homepage
1. Navbar: LogoHomeButton, Homebutton,"Searchbar", "What's New button(when new song is uploaded, bell will have number of notifications on it)", profile button
2. Footer1: Have links to tech we used (python, etc)
3. Popular Artists
4. RightClicking has features
5. Queue on right:

--AllPages
1. 3 Columns(left, middle, right)
2. Change size by dragging
3. LEFT: Your library
4. RIGHT: Artist info/queue
5. MIDDLE: Focus (top artists, albumn info, etc)


-- User
1. All will have:
    - Profile Page
        *Picture
        *"Monthly Listeners"
        *owner Popular songs: monthly listeners, songLength
        *FOLLOW button
        *Description
    - list all liked songs
    - personal albums
    - playlists
    - uploaded songs
2. Can edit on owner page.
3. Cannot follow yourself
4. Can change Name, picture
5. Clicking on song, takes you to album


-- Footer2: media player, pops up when logged in.
1. left: Has songname, artist, album cover, LIKE BUTTON
2. middle: Shuffle button, previous, PLAY, NEXT, REPEAT(1click: loops playlist, 2ndClick: loops same song)
3. right: Volume, "Queue",

3. Left Library SideBar:
    - Navbar: Playlists, By You
    - Liked songs
    - albums added to library
    - created playlists
    - "Following artists changes sidebar to artist"
    - Clicking library changes middle to "My Playlists" page
    - Can PIN "Liked Songs"
        *if multiple, pinned in alphabetical order
        *else in not pinned, sorted by recently played
    -

4. Hover overing an album/song, shows PLAY button

--Queue
1. Now Playing,
2. Next 10 songs in que

--AlbumPage
1. Top Header:
    -"Album":AlbumName,
    -Picture,
    -Artist,
    -Release year,(on hover:shows release date)
    -num of songs,
    -total length of all songs added up
2. BUTTONS:
    -Play,
    -add to library(change when clicked),
    -Options(3 dots)(same options as right clicking)
        *Add to Library (if added to library, can be removed)
        *Add to Queue
        *"Share"
3. Main
    - Song List
        *Number in the album
        *Title
        *Artist
        *Length of song
        *Release date at bottom


--Album (every)
1. Artist picture
2. Album cover picture
3. Album information
4. Song list

--RightCLick Song
1. Add to playlist
    -(can also create new playlist to add into)
    - ask which playlist you want to add to
2. Add to liked songs
3. "add to queue"
4. Go to artist
5. Go to Album
6. "Share"

--RightClick Album/Playlist
1. Add to Library
2. Add to Queue
3. "Share"
4. Add to playlist
    -(can also create new playlist to add into)
    - ask which playlist you want to add to

--RightClick on Artist
1. "Follow"
2. Go to artist page
3. "Share"



--Searchbar (BONUS)

USER STORIES:
Authentication
Login
As a user, I want to log into my account using my credentials, so that I can access my music and playlists.
As a user, I want to see an error message if my login fails, so that I know what went wrong.
As a user, I want a profile button visible upon login, so I can easily access my profile.
As a user, I want to see my personal albums, playlists, songs, and liked songs immediately after logging in.
Sign-Up
As a new user, I want to create an account with a username, email, password, and DOB, so that I can start using the service.
As a user, I want to choose between an artist or listener account, so that I get the correct permissions.
As an artist, I want to upload my songs, so that they are available to other users.
As a listener, I want to create playlists but not upload songs.
As a user, I want to be redirected to the homepage after signing up.
Homepage & Navigation
As a user, I want a navbar with a logo, home button, search bar, and notification bell, so that I can navigate easily.
As a user, I want a footer that displays the technologies used in the app (e.g., Python), so that I can learn about its tech stack.
As a user, I want to see a list of popular artists on the homepage, so that I can discover new music.
As a user, I want a right-click menu with useful options for songs, albums, and playlists.
User Profiles & Social Features
As a user, I want a profile page with my profile picture, playlists, and liked songs, so that I can personalize my experience.
As an artist, I want to display my monthly listeners and popular songs, so that others can see my reach.
As a user, I want to follow other users and see my followers.
As a user, I cannot follow myself.
As a user, I want to edit my profile details (name, picture, description).
Library & Organization
As a user, I want a sidebar with my liked songs, albums, and playlists for quick access.
As a user, I want the ability to pin my "Liked Songs" so that they appear at the top.
As a user, I want my library sorted by recently played if nothing is pinned.
Playback & Queue
As a user, I want a footer media player that pops up when logged in, so I can control playback.
As a user, I want play, shuffle, repeat, and volume controls in the media player.
As a user, I want a queue on the right side that shows the next 10 songs.
Albums & Songs
Album Page
As a user, I want an album page that shows album name, cover art, artist, release date, song list, and total length.
As a user, I want a play button to play the entire album.
As a user, I want options to add an album to my library, queue, or share it.
Song Interactions
As a user, I want to right-click a song to add it to a playlist, queue, or liked songs.
As a user, I want to go to an artist's page by clicking their name.
Search & Discovery (BONUS)
As a user, I want a search bar to find artists, albums, songs, and playlists.
As a user, I want search results categorized by type (e.g., artist, album, song).
