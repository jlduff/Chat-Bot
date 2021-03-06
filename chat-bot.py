from random import choice
def get_bot_langsuggestion(response):
    bot_langsuggestion_indoeuro = ["I recommend that you study about the Indo-European language family, the family of languages ranging from Western Europe to Northern India"]
    bot_langsuggestion_sinotibet = ["I recommend that you study about the Sino-Tibetan language family, a cluster of languages centered in much of Eastern and Southern Asia, and Oceania"]
    bot_langsuggestion_bantu = ["I recommend that you study about the Bantu language family, the group of languages spoken by the Bantu peoples, who inhabit much of Africa"]
    bot_langsuggestion_algonquin = ["I recommend that you study about the Algonquin language family, a language family with origins in the indigenous peoples of Eastern and Southern North America"]

 if response in ["European", "United States", "Roman", "Greek", "Indian", "Hindi", "Middle Eastern", "French", "Berber", "British", "Polish", "Italian"]:
        return choice(bot_langsuggestion_indoeuro)
    elif response in ["Tibetan", "Han Chinese", "Cantonese", "Thai", "Vietnamese", "Mandarin", "Burmese", "Siamese", "Mondzish", "Kathu"]:
        return choice(bot_langsuggestion_sinotibet)
    elif response in ["Swahili", "Congolese", "Xhosa", "Zulu", "Swami", "Khoi-San", "South Africa", "Mozambique", "Lesotho", "Swaziland"]:
        return choice(bot_langsuggestion_bantu)
    elif response in ["American", "Native American", "Indigenous American", "First Nations", "Iroquois", "Powhatan", "Ojibwe", "Potawatomi"]: 
        return choice(bot_langsuggestion_algonquin)
    else:
        return "Hmm, I don't seem to have a language family which corresponds with that particular historical period. Perhaps another idea?"

print("This program is to help history lovers choose a language or language family to learn or research based on a historical period they take interest in!")
print("There are a wide array of historical periods to match languages with, and cultures to fall in love with!")
print("Simply type 'done' when you're finished with this exploration (which, why would you be? :)!)")

response = input("What is a historical period or historical group or nation that you're interested in?  ")

if response == "done":
        break

print(f"So, you like the history of {response}?")

bot_langsuggestion = get_bot_langsuggestion(response)
print(bot_reccommend)