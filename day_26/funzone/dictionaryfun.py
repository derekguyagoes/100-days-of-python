def words():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    # new_dict = {new_key:new_value for (key, value) in list}
    result = {word: len(word) for word in sentence.split()}
    print(result)


def cel_to_far():
    def c_f(temp_c):
        return (temp_c * 9 / 5) + 32

    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }

    weather_f = {day: c_f(temp_in_c) for (day, temp_in_c) in weather_c.items()}

    print(weather_f)

# cel_to_far()
