import json
import os

from sentry_sdk import capture_message, init, configure_scope
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

init(os.environ['SENTRY_URL'], environment='aws-error-logger', integrations=[AwsLambdaIntegration()])


def handler(event, context):
    print('event', event)
    source = event.get('source', '')
    source = source.replace('aws.', '').capitalize()

    # if you don't intend to use sentry, replace the next lines by your custom logic
    with configure_scope() as scope:
        for key, value in event.items():
            if isinstance(value, (list, dict)):
                value = json.dumps(value)
            scope.set_tag(key, value)
        new_message = f'Something went wrong in {source}'
        capture_message(new_message, scope=scope)
