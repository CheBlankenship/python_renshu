import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


user_handle = "@sundarpichai"
celebrity_handle = "@elonmusk"

# def analyze(handle):
#     # Access keys
#     twitter_consumer_key = 'fUsUxkx9MgobZhpSJi2qZii60'
#     twitter_consumer_secret = 'atzAGdDGycm7K5R6odlIwxX1Ohv04tGGkenL4Lf4jarg1PMwUm'
#     twitter_access_token = '2431135844-LqVC9YhOjvaapOpAaFWs3X1mhU3G243nCBsZzkw'
#     twitter_access_secret = 'FXM5d6o8Xf6WiE9ihfdwYkdjgAjojYVNifYwnaKcBx5Lh'
#     twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
#     statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)
#     # print("Status >> ", statuses)
#     text = ""
#     for status in statuses:
#         if(status.lang == 'en'):
#             text += str(status.text.encode('utf-8'))
#
#     # The IBM credentials for PI
#     pi_username = '61f9c969-a1bb-4146-bb72-ea56291d03c6',
#     pi_password = 'iX1ojC5layN5'
#     personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
#     pi_result = personality_insights.profile(handle)
#     print("PI result >>> ", pi_result)
#     return pi_results


# # Access the response object
# def flatten(orig):
#     data = {}
#     for c in orig['tree']['children']:
#         if 'children' in c:
#             for c2 in c['children']:
#                 if 'children' in c2:
#                     for c3 in c2['children']:
#                         if 'children' in c3:
#                             for c4 in c3['children']:
#                                 if (c4['category'] == 'personality'):
#                                     data[c4['id']] = c4['percentage']
#                                     if 'children' not in c3:
#                                         if (c3['category'] == 'personality'):
#                                             data[c3['id']] = c3['percentage']
#
#     return data
#
#
# def compare(dict1, dict2):
#     compared_data = {}
#     for keys in dict1:
#         if dict1[keys] != dict2[keys]:
#             compared_data[keys]=abs(dict1[keys] - dict2[keys])
#
#     return compared_data
#
#
# # Analyze the input account via IBM PI API
# user_result = analyze(user_handle)
# celebrity_result = analyze(celebrity_handle)
#
# # Call flatten() to access the required data
# user = flatten(user_result)
# celebrity = flatten(celebrity_result)
#
# # Compare two accounts tweets
# compared_results = compare(user, celebrity)
#
#
# sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))
#
# for keys, value in sorted_result[:5]:
#     print(keys),
#     print(user[keys]),
#     print ('->'),
#     print (celebrity[keys]),
#     print ('->'),
#     print (compared_results[keys])
