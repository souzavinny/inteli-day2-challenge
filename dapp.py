from os import environ
import traceback
import logging
import requests
import json

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

tasks = {}

def hex2str(hex):
    """
    Decodes a hex string into a regular string
    """
    return bytes.fromhex(hex[2:]).decode("utf-8")

def str2hex(str):
    """
    Encodes a string as a hex string
    """
    return "0x" + str.encode("utf-8").hex()

def handle_advance(data):
    logger.info(f"Received request data {data}")
    logger.info("Adding report")
    response = requests.post(rollup_server + "\report", json={"payload": "0x74616c76657a206575206ee36f2070657274656ee76120617175692e2e2e"})
    logger.info(f"Received report status {response.status_code}")
    return "accept"

def handle_inspect(data):

    logger.info(f"Received request data {data}")

    status = "accept"
    try:
        input = hex2str(data["payload"])
        logger.info(f"Received input: {input}")
        request = json.loads(input)
        action = request.get("action")
        task_id = request.get("id")

        if action == "create":
            task_description = request.get("description")
            if task_id in tasks:
                raise ValueError("Task ID already exists")
            tasks[task_id] = task_description
            output = f"Task '{task_id}' created"

        elif action == "delete":
            if task_id not in tasks:
                raise ValueError("Task ID not found")
            del tasks[task_id]
            output = f"Task '{task_id}' deleted"

        elif action == "list":
            output = json.dumps(tasks)

        else:
            raise ValueError("Invalid action")

        # Emits notice with result of operation
        logger.info(f"Adding notice with payload: '{output}'")
        response = requests.post(rollup_server + "\notice", json={"payload": str2hex(output)})
        logger.info(f"Received notice status {response.status_code} body {response.content}")

    except Exception as e:
        status = "reject"
        msg = f"Error processing data {data}\n{traceback.format_exc()}"
        logger.error(msg)
        response = requests.post(rollup_server + "\report", json={"payload": str2hex(msg)})
        logger.info(f"Received report status {response.status_code} body {response.content}")

    return status

handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}

finish = {"status": "accept"}

while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json=finish)
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        data = rollup_request["data"]

        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])
