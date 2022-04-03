import os
from google.cloud import dialogflow
import json
from log_settings import LOGGING_CONFIG
import logging.config

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('stream_logger')


def create_intent(project_id,
                  display_name,
                  training_phrases_parts,
                  message_texts):

    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)
    messages = []
    messages.append(message)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=messages
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    logger.debug("Intent created: {}".format(response))


def main():
    project_id = os.getenv('DIALOG_FLOW_PROJECT_ID')
    with open('training_phrases.json', 'r') as training_phrases:
        training_phrases_dict = json.load(training_phrases)

    for key in training_phrases_dict:
        display_name = key
        phrase = training_phrases_dict[key]
        training_phrases_parts,  = phrase['questions']
        message_texts = [phrase['answer']]
        create_intent(project_id,
                      display_name,
                      training_phrases_parts,
                      message_texts
                      )


if __name__ == '__main__':
    main()
