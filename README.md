# PA Messenger

## A simple flask app to help run a text loop 

Use Twilio to create SMS notifications to keep your subscribers in the loop.

## Local Development

1. You will need to configure Twilio to send requests to your application when SMS are received.

   You will need to provision at least one Twilio number with SMS capabilities
   so the application's users can join the loop. You can buy a
   number [right here](https://www.twilio.com/user/account/phone-numbers/search).
   Once you have a number you need to configure your number to work with your
   application.
   Open [the number management page](https://www.twilio.com/user/account/phone-numbers/incoming)
   and open a number's configuration by clicking on it.

   Remember that the number where you change the _SMS webhook_ must be the same one you set on the `TwilioPhoneNumber` setting.

   Keep in mind that our endpoint is:

    ```
    http://<your-url>/message
    ```

1. Clone this repository and `cd` into it.

    ```
    git clone git@github.com:polymerwitch/pa_messenger.git
    ```

1. Create a new virtual environment.

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

1. Install the requirements using [pip](https://pip.pypa.io/en/stable/installing/).

    ```
    pip install -r requirements.txt
    ```

1. Edit the config file (pa_messenger.cfg) inside the root of the project, and be sure to replace the place holders and connection string with real information.

    ```
  SECRET_KEY = 'your_authy_secret_key'

  TWILIO_ACCOUNT_SID = '[your_twilio_account_sid]'
  TWILIO_AUTH_TOKEN = '[your_twilio_auth_token]'
  TWILIO_NUMBER = '[your_twilio_phone_number]'

  SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ```

1. Run the migrations.

    ```
    python manage.py db upgrade
    ```

1. Start the development server.

    ```
    python manage.py runserver
    ```

That's it!

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

    ```
    $ coverage run test.py
    ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.

## Deploy to Heroku

For smaller loops you can run this on a free dyno from heroku

1. Get the Heroku cli [Heroku-Cli](https://devcenter.heroku.com/articles/heroku-cli)

1. cd into the cloned project directory

    ```
    $ cd pa_messenger
    ```

1. Login to Heroku

    ```
    $ heroku login
    ```

1. Create the heroku app

    ```
    $ heroku create my_text_app
    ```

1. Ensure pa_messenger.cfg is configured as outlined above and commit the changes. The database url can be gotten with:

    ```
    $ heroku config
    ```

1. Set heroku to be production

    ```
    $ heroku config:set ENV=production
    ```

1. Set heroku to read the config file

    ```
    $ heroku config:set PA_MESSENGER_CONFIG=../pa_messenger.cfg
    ```

1. Push the app to Heroku

    ```
    $ git push heroku master
    ```

1. Scale the dyno

    ```
    $ heroku ps:scale web=1
    ```

1. Setup the DB

    ```
    $ heroku run python manage.py db upgrade
    $ heroku run python manage.py db migrate
    ```

1. You should be set!

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
