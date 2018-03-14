from __future__ import absolute_import
from __future__ import print_function
import os
import sys

from dxlbootstrap.util import MessageUtils
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxlciscopxgridclient.client import CiscoPxGridClient
from dxlciscopxgridclient.constants import EpsAction

# Import common logging and configuration
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# MAC address of the endpoint for which to send the mitigation action
HOST_MAC = "<SPECIFY_MAC_ADDRESS>"

# Create the client
with DxlClient(config) as dxl_client:

    # Connect to the fabric
    dxl_client.connect()

    logger.info("Connected to DXL fabric.")

    # Create client wrapper
    client = CiscoPxGridClient(dxl_client)

    # Invoke 'send mitigation action by MAC' method on service
    resp_dict = client.eps.send_mitigation_action_by_mac(
        HOST_MAC,
        EpsAction.QUARANTINE)

    # Print out the response (convert dictionary to JSON for pretty
    # printing)
    print("Response:\n{0}".format(
        MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
