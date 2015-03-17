import fresh_tomatoes
import movie
import show

#Create some movies

#Bird Man Movie
bird_man_title = "Bird Man"
bird_man_story_line = "A washed-up actor, who once played an iconic superhero, battles his ego and attempts to recover \
                      his glory."
bird_man_poster_image = "http://pixel.nymag.com/content/dam/daily/vulture/2014/09/25/birdman-click.jpg"
bird_man_trailer_url = "https://www.youtube.com/watch?v=uJfLoE6hanc"
bird_man_rating = 8

bird_man = movie.Movie(bird_man_title, bird_man_story_line, bird_man_poster_image, bird_man_trailer_url,
                       bird_man_rating)

#Whiplash Movie
whiplash_title = "Whiplash"
whiplash_story_line = "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of \
                      greatness are mentored by an instructor who will stop at nothing to realize a student's \
                      potential."
whiplash_poster_image = "http://upload.wikimedia.org/wikipedia/en/0/01/Whiplash_poster.jpg"
whiplash_trailer_url= "https://www.youtube.com/watch?v=7d_jQycdQGo"
whiplash_rating = 8.6

whiplash = movie.Movie(whiplash_title, whiplash_story_line, whiplash_poster_image, whiplash_trailer_url,
                       whiplash_rating)

#Boxtrolls Movie
box_trolls_title = "The Boxtrolls"
box_trolls_story_line = "A young orphaned boy raised by underground cave-dwelling trash collectors tries to save his \
                        friends from an evil exterminator. Based on the children's novel 'Here Be Monsters' by Alan \
                        Snow."
box_trolls_poster_image = "http://www.cartoonbrew.com/wp-content/uploads/2013/07/boxtrolls-poster.jpg"
box_trolls_trailer_url = "https://www.youtube.com/watch?v=Q2dFVnp5K0o"
box_trolls_rating = 6.9

box_trolls = movie.Movie(box_trolls_title, box_trolls_story_line, box_trolls_poster_image, box_trolls_trailer_url,
                         box_trolls_rating)

#Create some shows

#Ugly Betty Show
ugly_betty_title = "Ugly Betty Season 3"
ugly_betty_story_line = "A young, smart and wise woman named Betty Suarez goes on a journey to find her inner beauty."
ugly_betty_poster_image = "http://www.impawards.com/tv/posters/ugly_betty_ver3_xlg.jpg"
ugly_betty_trailer_url = "https://www.youtube.com/watch?v=Fzp06MEsghI"
ugly_betty_tv_station = "CBS"
ugly_betty_rating = 6.2

ugly_betty = show.Show(ugly_betty_title, ugly_betty_story_line, ugly_betty_poster_image, ugly_betty_trailer_url,
                       ugly_betty_rating, ugly_betty_tv_station)

#Firends Show
friends_title = "Friends"
friends_story_line = "Follows the lives of six 20-something friends living in Manhattan."
friends_poster_image = "http://stuffpoint.com/friends/image/84658-friends-friends-poster.jpg"
friends_trailer_url = "https://www.youtube.com/watch?v=hDNNmeeJs1Q"
friends_tv_station = "TBS"
friends_rating = 7

friends = show.Show(friends_title, friends_story_line, friends_poster_image, friends_trailer_url, friends_rating,
                    friends_tv_station)

#CSI Miami
csi_miami_title = "CSI Miami"
csi_miami_story_line = "The cases of the Miami-Dade, Florida police department's Crime Scene Investigations unit."
csi_miami_poster_image = "http://www.impawards.com/tv/posters/csi_miami_ver2.jpg"
csi_miami_trailer_url = "https://www.youtube.com/watch?v=2uZL9OVdQkI"
csi_miami_tv_station = "AETV"
csi_miami_rating = 6.4

csi_miami = show.Show(csi_miami_title, csi_miami_story_line, csi_miami_poster_image, csi_miami_trailer_url,
                      csi_miami_rating, csi_miami_tv_station)

videos = [bird_man, whiplash, box_trolls, ugly_betty, friends, csi_miami]

fresh_tomatoes.open_movies_page(videos)