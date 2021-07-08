#2. Tee funktio, joka luo uuden instanssin.
#1. https://github.com/GoogleCloudPlatform/python-docssamples/blob/46fa5a588858021ea32350584a4ee178cd7c1f33/compute/api/create_instance.py

#Method: instances.insert
#Creates an instance resource in the specified project using the data included in the request.

#BEFORE RUNNING:
#3. Install the Python client library for Google APIs by running:   `pip install --upgrade google-api-python-client`

from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'sekalaisten-toimien-projekti'  # TODO: Update placeholder value.

# The name of the zone for this request.
zone = 'us-central1-a'  # TODO: Update placeholder value.

#alla oleva instance_body kopsattu konsolista REST
instance_body = {
  "kind": "compute#instance",
  "name": "torstai-pyytton-instance-1",
  "zone": "projects/sekalaisten-toimien-projekti/zones/us-central1-a",
  "machineType": "projects/sekalaisten-toimien-projekti/zones/us-central1-a/machineTypes/f1-micro",
  "displayDevice": {
    "enableDisplay": False
  },
  "metadata": {
    "kind": "compute#metadata",
    "items": []
  },
  "tags": {
    "items": []
  },
  "disks": [
    {
      "kind": "compute#attachedDisk",
      "type": "PERSISTENT",
      "boot": True,
      "mode": "READ_WRITE",
      "autoDelete": True,
      "deviceName": "torstai-pyytton-instance-1",
      "initializeParams": {
        "sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20210701",
        "diskType": "projects/sekalaisten-toimien-projekti/zones/us-central1-a/diskTypes/pd-balanced",
        "diskSizeGb": "10",
        "labels": {}
      },
      "diskEncryptionKey": {}
    }
  ],
  "canIpForward": False,
  "networkInterfaces": [
    {
      "kind": "compute#networkInterface",
      "subnetwork": "projects/sekalaisten-toimien-projekti/regions/us-central1/subnetworks/default",
      "accessConfigs": [
        {
          "kind": "compute#accessConfig",
          "name": "External NAT",
          "type": "ONE_TO_ONE_NAT",
          "networkTier": "PREMIUM"
        }
      ],
      "aliasIpRanges": []
    }
  ],
  "description": "",
  "labels": {},
  "scheduling": {
    "preemptible": False,
    "onHostMaintenance": "MIGRATE",
    "automaticRestart": True,
    "nodeAffinities": []
  },
  "deletionProtection": False,
  "reservationAffinity": {
    "consumeReservationType": "ANY_RESERVATION"
  },
  "serviceAccounts": [
    {
      "email": "1090615713494-compute@developer.gserviceaccount.com",
      "scopes": [
        "https://www.googleapis.com/auth/devstorage.read_only",
        "https://www.googleapis.com/auth/logging.write",
        "https://www.googleapis.com/auth/monitoring.write",
        "https://www.googleapis.com/auth/servicecontrol",
        "https://www.googleapis.com/auth/service.management.readonly",
        "https://www.googleapis.com/auth/trace.append"
      ]
    }
  ],
  "shieldedInstanceConfig": {
    "enableSecureBoot": False,
    "enableVtpm": True,
    "enableIntegrityMonitoring": True
  },
  "confidentialInstanceConfig": {
    "enableConfidentialCompute": False
  }
}


request = service.instances().insert(project=project, zone=zone, body=instance_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)

