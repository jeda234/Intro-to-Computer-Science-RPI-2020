# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:45:55 2020

@author: cowarj
"""

import json

if __name__ == "__main__":
    
    min_y = int(input("Min year => "))
    print(min_y)
    max_y = int(input("Max year => "))
    print(max_y)
    w1 = input("Weight for IMDB => ")
    print(w1)
    w1 = float(w1)
    w2 = float(input("Weight for Twitter => "))
    print(w2)
    print("")

    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

    answer = input("What genre do you want to see? ")
    print(answer)
    answer = answer.lower()

    while(answer != "stop"):
        l = []
        for i in movies:
            if i not in ratings or len(ratings[i]) < 3:
                continue
            year = movies[i]['movie_year']
            if (year >= min_y and year <= max_y):
                avg = sum(ratings[i])/len(ratings[i])
                for j in movies[i]['genre']:
                    j = j.lower()
                    if (j == answer):
                        l.append((movies[i], avg))
                        
        if (len(l) == 0):
            print("") 
            answer = answer.capitalize()
            
            for i in range(0, len(answer)):
                if (answer[i].isalpha() == False):
                    x = answer[i+1].upper()
                    answer = answer[:i+1]+x+answer[i+2:]
                    
            print("No {} movie found in {} through {}".format(answer, min_y, max_y)) 
            print("")
            
        else:
            movie = []
            for y in l:
                rate = (((w1*(y[0]['rating']))+(w2*y[1]))/(w1+w2))
                movie.append((rate, y[0]['name'], y[0]['movie_year']))
        
            movie = sorted(movie) 
            print("")
            print("Best:")
            print("        Released in {}, {} has a rating of {:.2f}".format(movie[-1][2], movie[-1][1], movie[-1][0]))
            print("")
            print("Worst:")
            print("        Released in {}, {} has a rating of {:.2f}".format(movie[0][2], movie[0][1], movie[0][0]))
            print("")
            
        answer = input("What genre do you want to see? ")
        print(answer)
        answer = answer.lower()
