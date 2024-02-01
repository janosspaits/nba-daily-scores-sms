import requests
from datetime import date, timedelta
from twilio.rest import Client


def read_keys_from_file(filepath):
    with open(filepath, "r") as secret_key:
        return secret_key.readline().strip()


def get_yesterdays_date():
    yesterday = date.today() - timedelta(days=1)
    yesterday = yesterday.strftime("%Y/%m/%d")
    return yesterday


def make_api_call(api_key):
    yesterday = get_yesterdays_date()
    daily_scores_endpoint = f"https://api.sportradar.com/nba/trial/v8/en/games/{yesterday}/schedule.json?api_key={api_key}"
    response = requests.get(daily_scores_endpoint)
    response.raise_for_status()
    scores = response.json()
    return scores


def initialize_twilio_client(account_sid, auth_token):
    client = Client(account_sid, auth_token)
    return client


def create_message_body(yesterday, scores):
    message_body = f"{yesterday}\n\n"
    for game in scores["games"]:
        if (
            game["home"]["alias"] == "BOS" and game["home_points"] > game["away_points"]
        ) or (
            game["away"]["alias"] == "BOS" and game["home_points"] < game["away_points"]
        ):
            game_score = f"{game['home']['alias']}-{game['away']['alias']} : {game['home_points']}-{game['away_points']} 🍀\n\n"
        elif (
            game["home"]["alias"] == "LAL" and game["home_points"] < game["away_points"]
        ) or (
            game["away"]["alias"] == "LAL" and game["home_points"] > game["away_points"]
        ):
            game_score = f"{game['home']['alias']}-{game['away']['alias']} : {game['home_points']}-{game['away_points']} 😂\n\n"
        else:
            game_score = f"{game['home']['alias']}-{game['away']['alias']} : {game['home_points']}-{game['away_points']}\n\n"
        message_body += game_score

    print(message_body)
    return message_body


# This function uses whatsapp sending, this needs setup on the twilio website and might use a different "from number"
# If you use SMS, simply remove "whatsapp:" from the phone number strings
# If you use SMS, the from number should be the number you get on twilio website
def send_message_from_twilio(client, message_body, phone_number):
    message = client.messages.create(
        body=message_body,
        from_="whatsapp:+14155238886",
        to=f"whatsapp:{phone_number}",
    )
    print(message.status)
    return message


def main():
    api_key = read_keys_from_file("apikey.txt")
    phone_number = read_keys_from_file("phone_number.txt")
    account_sid = read_keys_from_file("twilio_sid.txt")
    auth_token = read_keys_from_file("twilio_auth_token.txt")
    yesterday = get_yesterdays_date()
    scores = make_api_call(api_key=api_key)
    client = initialize_twilio_client(account_sid, auth_token=auth_token)
    message_body = create_message_body(yesterday, scores)
    send_message_from_twilio(client, message_body, phone_number)


if __name__ == "__main__":
    main()
