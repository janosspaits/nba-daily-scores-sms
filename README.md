# NBA Daily Scores SMS app

Gets the scores from the previous day and sends an SMS message to your phone

## Setup

### Sign up for a SportRadar API key
- https://developer.sportradar.com/docs/read/basketball/NBA_v8

### Create a twilio account to get your id and auth token<br>
- https://www.twilio.com/
- (For my own setup, only whatsapp messaging was  successful, you can set this up on the twilio website)

### Create local files for secret keys - these exact file names are git ignored
- apikey.txt - for SportRadar NBA API key
- phone_number.txt - for your phone number (+551234123123 format)
- twilio_sid.txt - for twilio account ID
- twilio_auth_token.txt - for twilio auth token (this is really important to be secret)

### (Optional) - host the code for automated daily running
- I have used https://www.pythonanywhere.com/ for this


## Plans for the developer
1. host the app somewhere so it could run once daily - ✅done - Pytonanywhere
2. gitignore keys before making repo public - ✅done
3. organize stuff into functions - ✅done
4. fill out requirements.txt with only relevant libraries
5. doc string functions
6. use Pydantic or dataclasses for data validation and structure
7. unit tests

## Developer

- github.com/janosspaits