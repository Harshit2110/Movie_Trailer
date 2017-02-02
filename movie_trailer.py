import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Movie_Trailers</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    
    <style type="text/css" media="screen">
        body {
            background-image: url("assets/maxresdefault (2).jpg");
            padding-top: 80px;
        }
        p {
            font-family: "Comic Sans MS";
            color: rgb(0,0,255);
        }
        h2 {
            color: rgb(255,255,255);
        }
        
        
        
        .hovereffect {
            width:80%;
            height:40%;
            float:left;
            overflow:hidden;
            position:relative;
            text-align:center;
            cursor:default;
        }

        .hovereffect .overlay {
            width:100%;
            height:100%;
            position:absolute;
            overflow:hidden;
            top:0;
            left:0;
            opacity:0;
            background-color:rgba(0,0,0,0.5);
            -webkit-transition:all .4s ease-in-out;
            transition:all .4s ease-in-out
        }

        .hovereffect img {
            display:block;
            position:relative;
            -webkit-transition:all .4s linear;
            transition:all .4s linear;
        }

        .hovereffect h2 {
            text-transform:uppercase;
            color:#fff;
            text-align:center;
            position:relative;
            font-size:17px;
            background:rgba(0,0,0,0.6);
            -webkit-transform:translatey(-100px);
            -ms-transform:translatey(-100px);
            transform:translatey(-100px);
            -webkit-transition:all .2s ease-in-out;
            transition:all .2s ease-in-out;
            padding:10px;
        }

        .hovereffect:hover img {
            -ms-transform:scale(1.2);
            -webkit-transform:scale(1.2);
            transform:scale(1.2);
        }
        .hovereffect a.info {
            text-decoration:none;
            display:inline-block;
            text-transform:uppercase;
            color:#fff;
            border:1px solid #fff;
            background-color:transparent;
            opacity:0;
            filter:alpha(opacity=0);
            -webkit-transition:all .2s ease-in-out;
            transition:all .2s ease-in-out;
            margin:50px 0 0;
            padding:7px 14px;
        }

        .hovereffect a.info:hover {
            box-shadow:0 0 5px #fff;
        }

        .hovereffect:hover .overlay {
            opacity:1;
            filter:alpha(opacity=100);
        }

        .hovereffect:hover h2,.hovereffect:hover a.info {
            opacity:1;
            filter:alpha(opacity=100);
            -ms-transform:translatey(0);
            -webkit-transform:translatey(0);
            transform:translatey(0);
        }

        .hovereffect:hover a.info {
            -webkit-transition-delay:.2s;
            transition-delay:.2s;
        }
        .description {
            color: #eee
        }
        .navbar {min-height: 80px;}
        .navbar-brand {padding: 0 15px; height: 80px; line-height: 80px;}
        #trailer .modal-dialog {
            margin-top: 100px;
            width: 800px;
            height: 480px;
            background-color: rgb(0,0,0);
        }
        .row {
            background-color: rgb(0,0,0);
        }
        
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 50px;
        }
        
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    
    <script type="text/javascript" charset="utf-8">

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));

            //Add movie information to the modal
            var title = $(this).attr('data-title')
            var lead_act_1 = $(this).attr('data-lead1')
            var lead_act_2 = $(this).attr('data-lead2')
            var lead_act_3 = $(this).attr('data-lead3')
            var director = $(this).attr('data-director')
            var storyline = $(this).attr('data-movie-storyline')
            $("#actor-info").empty().append($("<div> <p><b>Directed by:- </b>"+director+".</p><p><b>Staring:-</b>  "+lead_act_1+", "+lead_act_2+", "+lead_act_3+".</p>"+"</div>"));
            $("#this_title").empty().append($("<h2><b><i><u>"+title+"</u></i></b></h2>"));
            $("#story").empty().append($("<div> <p><b>Story:- </b>"+storyline+".</p>"+"</div>"));
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>

          <div class="row">
              <div class="col-md-11" id="this_title"></div>
              <div class="col-md-11" id="actor-info"></div>
          </div>

          <div class="row">
              <div class="col-md-11" id="story"></div>
          </div>
          
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
   
    

    <!-- Main Page Content -->
    <div class="container">
        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="#"><h1>MOVIE TRAILERS</h1></a>
                </div>
                
            </div>
        </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-title="{movie_title}" data-movie-storyline="{movie_storyline}" data-lead1="{lead_1}" data-lead2="{lead_2}" data-lead3="{lead_3}" data-director="{director}" data-toggle="modal" data-target="#trailer">
    <div class="hovereffect">
      <img src="{poster_image_url}" alt="Unable to show Poster" width="280" height="342">
        <div class="overlay">
          <h2><b><u><i> {movie_title} </i></u></b></h2>
        </div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            lead_1=movie.lead_1,
            lead_2=movie.lead_2,
            lead_3=movie.lead_3,
            director=movie.director
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('Movie_Trailers.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
