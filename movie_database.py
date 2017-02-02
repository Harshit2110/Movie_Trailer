import movie_class
import movie_trailer 

fnf8 = movie_class.Movie("The Fate of the Furious",
                   "Now that Dom (Vin Diesel) and Letty (Michelle Rodriguez) are on their honeymoon, Brian and Mia have retired from the game, and the rest of the crew has been exonerated, the globetrotting team has found a semblance of a normal life. But when a mysterious woman seduces Dom back into a world of crime that he can't seem to escape, the crew will face trials that will test them as never before.",
                    "assets/TFOTF_Teaser_Poster.jpg",
                   "https://www.youtube.com/watch?v=2DMpqplvADQ",
                   "Vin Diesel",
                   "Dwayne Johnson",
                   "Jason Statham",
                   "F. Gary Gray")

jollyllb2 = movie_class.Movie("Jolly LLB2",
                        "Set in Lucknow, Jolly LLB 2 is the story of the blunt, abrasive and yet oddly compassionate Jagdishwar Mishra, aka Jolly, a small-time, struggling lawyer who has moved from Kanpur to the city of Nawabs to pursue his dream of becoming a big-time lawyer. A hustler by nature, Jolly survives by fighting petty cases and using every tactic under the sun to make a quick buck and earn a decent living. Having spent years in the chaotic and dingy court corridors Jolly is looking out for an opportunity that could turn the tide in his favour and help him achieve his dream of becoming a full-fledged Lawyer with a chamber. When faced with the glimpse of such an opportunity, Jolly jumps at the chance and in the bargain commits an innocent mistake with irreversible consequences that makes him ready for a big fight with the ruthless advocate Mathur.",
                        "assets/Jolly_LLB_2_first_look.jpg",
                        "https://www.youtube.com/watch?v=kvjxoBG5euo",
                        "Akshay Kumar, Huma Qureshi",
                        "Annu Kapoor, Sayani Gupta",
                        "Saurabh Shukla",
                        "Subhash Kapoor")

rangoon = movie_class.Movie("Rangoon",
                      "Rangoon is an upcoming Indian Hindi-language drama film, directed by Vishal Bhardwaj and produced by Sajid Nadiadwala and Viacom 18 Motion Pictures",
                      "assets/RangoonPoster.jpg",  
                      "https://www.youtube.com/watch?v=B-tC0wcIu24",
                      "Saif Ali Khan",
                      "Kangana Ranaut",
                      "Shahid Kapoor",
                      "Vishal Bhardwaj")

logan = movie_class.Movie("Logan",
                    "In the near future, a weary Logan cares for an ailing Professor X in a hide out on the Mexican border. But Logan's attempts to hide from the world and his legacy are up-ended when a young mutant arrives, being pursued by dark forces.",
                    "assets/Logan_2017_poster.jpg",
                    "https://www.youtube.com/watch?v=RH3OxVFvTeg",
                    "Hugh Jackman",
                    "Patrick Stewart",
                    "Boyd Holbrook",
                    "James Mangold")

passengers = movie_class.Movie("Passengers",
                         "On a routine journey through space to a new home, two passengers, sleeping in suspended animation, are awakened 90 years too early when their ship malfunctions. As Jim and Aurora face living the rest of their lives on board, with every luxury they could ever ask for, they begin to fall for each other, unable to deny their intense attraction... until they discover the ship is in grave danger. With the lives of 5000 sleeping passengers at stake, only Jim and Aurora can save them all.",
                         "assets/Passengers_2016_film_poster.jpg",
                         "https://www.youtube.com/watch?v=7BWWWQzTpNU",
                         "Jennifer Lawrence",
                         "Chris Pratt",
                         "Michael Sheen",
                         "Mortan Tyldum",)

raees = movie_class.Movie("Raees",
                    "RAEES is the fictitious story of a man named Raees, set in early 1980's to 1990's Gujarat, India. The film explores how Raees' relationships and meteoric rise helped him build an entire empire from scratch, to make him the single most powerful man in the state. Less of a gangster but more of an impresario, Raees gains popularity, a cult following and most importantly the public's trust by demonstrating entrepreneurial flair, unfettered determination to achieving his goals and ironically a heart of gold. His layered character traits encapsulate an inimitable blend of personas, making him revered, loved and feared. Always thinking ahead of the curve and using revolutionary ideas of management which were unheard of during his time, but are now doctrines for students, Raees eliminates every opposition that comes his way. However, his downfall will be crossing paths with the no-nonsense police officer Majumdar, whose sole reason for existence is the elimination of crime. What ensues next is a tumultuous battle between the two, which forms a key defining element of the film's narrative.",
                    "assets/Raees_Poster.jpg",
                    "https://www.youtube.com/watch?v=J7_1MU3gDk0",
                    "Shah Rukh Khan",
                    "Mahira Khan",
                    "Nawazuddin Siddiqui",
                    "Rahul Dholakia")

movies = [fnf8,jollyllb2,rangoon,logan,passengers,raees]
movie_trailer.open_movies_page(movies)

