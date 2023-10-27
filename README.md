```markdown
# Travel Chatbot

A simple travel chatbot built using Rasa, capable of providing travel recommendations and handling user preferences.

## Description

This chatbot is designed to assist users in finding travel destinations and activities based on their preferences and budget. It can handle various user inputs, provide recommendations, and respond to user feedback.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/travel-chatbot.git
   ```

2. Install the necessary dependencies:

   ```bash
   cd travel-chatbot
   pip install rasa
   npm install rasa-webchat
   ```

## Usage

1. Train the Rasa chatbot:

   ```bash
   rasa train
   ```

2. Start the Rasa server:

   ```bash
   rasa run --enable-api --cors "*" --debug
   ```

3. Integrate the chatbot into a web application:

   - Add the following script tag to the HTML file of your web application:

     ```html
     <script src="https://cdn.jsdelivr.net/npm/rasa-webchat/lib/index.min.js"></script>
     ```

   - Configure the Rasa Webchat component by adding the following script:

     ```html
     <script>
       WebChat.default.init({
         selector: "#webchat",
         initPayload: "/get_started",
         customData: {"language": "en"},
         socketUrl: "http://localhost:5005",
       });
     </script>
     ```

   - Add the chat widget to your web application HTML:

     ```html
     <div id="webchat"></div>
     ```

4. Open your web application in a browser to test the integrated chatbot.

## Files

- `nlu.yml`: Contains the training data for the NLU model.
- `domain.yml`: Defines the domain of the chatbot, including intents, actions, and slots.
- `rules.yml`: Contains the rules for handling different user inputs and triggering appropriate actions.
- `stories.yml`: Contains sample conversational flows for the chatbot.
- `actions.py`: Includes custom action code for the chatbot.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
