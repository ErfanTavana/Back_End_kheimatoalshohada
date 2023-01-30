from medianasms import Client
# you api key that generated from panel
api_key = "UDt2HeodeXayUtOpK7ZXFQKso3jpWpY6sqDGtLMqVpo="
# create client instance
sms = Client(api_key)
# send bulk message
bulk_id = sms.send(
"+9810001", # originator
["989033483116"], # recipients
"mediana is awesome" # message
)