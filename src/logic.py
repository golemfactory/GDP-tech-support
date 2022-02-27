
import re
import json

from numpy import require, single


f = open("../faq.json", encoding="utf-8")
faq = json.load(f)


def DetectKeywords(userInput):
    # formatting the message / removing unnecessary characters and lowering letters
    userInput_formated = re.split(r"\s+|[,;?!.-]\s*", userInput.lower())

    # now we gotta check for keywords (response is what CheckKeywords returns us)
    response = CheckKeywords(userInput_formated)

    # returning response for this function
    return response 

def CheckKeywords(message):

    #print("CheckKeywords, message: ".join(message))

    highestProbabilityList = {}

    # simplifying creating of bot responses 
    def Response(index, botResponse, keywords, singleResponse=False, requiredKeywords=[]):
        nonlocal highestProbabilityList
        highestProbabilityList[index, botResponse] = CalculatingMessageProbability(message, keywords, singleResponse, requiredKeywords)
        

    #print(highestProbabilityList)

    # creating the responses for the bot

    # how to change wallet
    Response("001", faq["001"]["answer"], ["how", "to", "change", "wallet", "changing", "can", "I"], singleResponse=False, requiredKeywords=[""])
    
    # which is Golem github account
    Response("002", faq["002"]["answer"], ["golem's", "golem", "github", "which", "account", "is"], singleResponse=False)
    
    # when do I start receiving tasks
    Response("003", faq["003"]["answer"], ["when", "do", "i", "start", "receiving", "tasks", "will", "receive"], singleResponse=False)
    
    # where can I see golem network stats
    Response("004", faq["004"]["answer"], ["where", "can", "i", "see", "golem", "network", "stats", "statistics", "check"], singleResponse=False, requiredKeywords=[""])
    
    # how does cpu/h pricing work
    Response("005", faq["005"]["answer"], ["how", "does", "cpu/h", "pricing", "work", "mean", "what"], singleResponse=False, requiredKeywords=[""])
    
    # how are providers selected to compute a task
    Response("006", faq["006"]["answer"], ["how", "are", "providers", "selected", "to", "compute", "a", "task", "tasks", "choosen", "which"], singleResponse=False, requiredKeywords=[""])
    
    # what hardware requiremets are there to run a provider
    Response("007", faq["007"]["answer"], ["what", "hardware", "requirements", "are", "there", "to", "run", "a", "provider", "which"], singleResponse=False, requiredKeywords=[""])
    
    # what is layer 1 (L1) and Layer 2 (L2)
    Response("008", faq["008"]["answer"], ["what", "is", "layer 1", "and", "layer 2", "difference"], singleResponse=False, requiredKeywords=[""])
    
    # what difference is there between GLM and tGLM
    Response("009", faq["009"]["answer"], ["what", "difference", "is", "there", "between", "glm", "and", "tglm"], singleResponse=False, requiredKeywords=["difference", "GLM", "tGLM"])
    
    # does golem wipe/clean the task data
    Response("010", faq["010"]["answer"], ["does", "golem", "wipe", "clean", "erase", "the", "task", "data"])
    
    # is golem network centralized or decentralized
    Response("011", faq["011"]["answer"], ["is", "golem", "network", "centralized", "or", "decentralized"])
    
    # who are top requestors on this network
    Response("012", faq["012"]["answer"], ["who", "are", "top", "requestors", "on", "golem", "network", "this"])
    
    # can I run golem on hosting services like AWS/OVH
    Response("013", faq["013"]["answer"], ["can", "i", "run", "golem", "on", "hosting", "services", "like", "aws", "ovh"])
    
    # where do I find yagna logs
    Response("014", faq["014"]["answer"], ["where", "do", "i", "find", "yagna", "logs"])
    
    # would a windows provider version be coming anytime soon
    Response("015", faq["015"]["answer"], ["would", "a", "windows", "provider", "version", "be", "coming", "anytime", "soon"])
    
    # is golem a ERC20 token
    Response("016", faq["016"]["answer"], ["is", "golem", "a", "erc20", "token"])
    
    # what is ERC20
    Response("017", faq["017"]["answer"], ["what", "is", "erc20"])
    
    # why do people run nodes on the testnet
    Response("018", faq["018"]["answer"], ["why", "do", "people", "run", "nodes", "on", "the", "testnet"])
    
    # how do I update golem to the newest version
    Response("019", faq["019"]["answer"], ["how", "do", "i", "update", "golem", "to", "the", "newest", "version"])
    
    # what is thorg
    Response("020", faq["020"]["answer"], ["what", "is", "thorg"])

    # can I change price while executing tasks
    Response("021", faq["021"]["answer"], ["can", "i", "change", "price", "while", "executing", "tasks", "task"])
    

    # calcuating the best match for input message
    index, botResponse = max(highestProbabilityList, key=highestProbabilityList.get)
    #print("best match: " + bestMatch)

    #print(highestProbabilityList)
    #print(f"best match = {bestMatch} | score: {highestProbabilityList[bestMatch]}")

    print("here" + botResponse)
    print("INDEX " + index)
    return index

def CalculatingMessageProbability(message, keywords, singleResponse=False, requiredKeywords=[]):
    messageCertainty = 0
    includesRequiredWords = True

    # counts how many keywords are in each message
    print(message)
    print(keywords)
    for word in message:
        if word in keywords:
            messageCertainty += 1
    print(messageCertainty)

    # calculated a percentage based on how many keywords are in message and how many keywords there are
    percentage = float(messageCertainty) / float(len(keywords))

    print(percentage)

    return messageCertainty

    # checks if all keywords from requiredKeywords are in the message / sets includesRequiredWords = True
    #for keyword in requiredKeywords:
        #if keyword not in message:
            #includesRequiredWords = False
            #break

    #if includesRequiredWords or singleResponse:
    #    return int(percentage * 100)
    #else:
    #    return 0