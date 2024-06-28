import json

# MOVIE_DATA_JSON = """"""
# def load_movie_data():
#     return json.loads(MOVIE_DATA_JSON)


def load_movie_data():
    with open('training_data.json', 'r') as json_file:
        return json.load(json_file)


def get_recommendations(movies, interests):
    recommendations = []
    for movie in movies:
        if any(interest.lower() in movie['genres'] for interest in interests):
            recommendations.append(movie)
    return recommendations

def display_recommendations(recommendations):
    if not recommendations:
        print("No recommendations found based on your interests.")
    else:
        print("Here are some movie recommendations based on your interests:")
        for movie in recommendations:
            print(f"Title: {movie['title']}, Platform: {movie['platform']}")

def main():
    movie_data = load_movie_data()
    movies = movie_data['movies']
    interests = []

    while True:
        user_interests = input("Enter your movie interests (genres), separated by commas: ").strip().split(',')
        interests.extend([interest.strip().lower() for interest in user_interests])

        recommendations = get_recommendations(movies, interests)
        display_recommendations(recommendations)

        more_interests = input("Would you like to add more interests? (yes/no): ").strip().lower()
        if more_interests != 'yes':
            break

main()