import os
import sys

import openai

openai.organization = "org-HkHW0tt2dotYG3m12RMlt8gQ"
openai.api_key = "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"
model_list = openai.Model.list()
print(model_list)
