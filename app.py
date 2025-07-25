#!/usr/bin/env python3

import aws_cdk as cdk

from linked_list_api.linked_list_api_stack import LinkedListApiStack


app = cdk.App()
LinkedListApiStack(app, "LinkedListApiStack")

app.synth()