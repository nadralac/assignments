cities = [ "Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver","New Orleans" ]
print (cities)
nba_players = ["M. Jordan","S. Curry","D. Green","L. James", "D. Wayde", "I. Shumpert", "M. Ellis", "K. Thompson","J. Poole","K. Bryant"]
print (nba_players)


print (cities [1], cities [4], cities [-2])
print (nba_players[-3], nba_players[1], nba_players[0])

first_three_cities= cities [0:3]
print (first_three_cities)
last_three_nba_players= nba_players [-3:10]
print (last_three_nba_players)

cities [0]= "San Francisco"
cities[2] = "Brooklyn"
cities [-3]= "Hollywood"
cities [-5]= "Tampa"
print (cities)

cities.append ("Oakland")
cities.extend (["New York City","Los Angeles"])
cities.insert (0, "Miami")
print cities


