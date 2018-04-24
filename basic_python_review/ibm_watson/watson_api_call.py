import json
import os, sys
from watson_developer_cloud import PersonalityInsightsV3



personality_insights = PersonalityInsightsV3(
    version='2018-4-11',
    username='60bd1b02-073c-4031-a26f-754cd342a648',
    password='yoZUnMFj2o7p'
    # x-watson-learning-opt-out=True
)

print("Res >>> ",  personality_insights)
