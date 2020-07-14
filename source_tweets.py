from searchtweets import load_credentials
from searchtweets import gen_rule_payload
from searchtweets import ResultStream
import yaml
import json

def get_file(aname, cak, cask, etype, hashtag, keywords, fdate, tdate, ftime, ttime):
    
    label = aname
    consumer_key = cak
    consumer_secret = cask
    if etype == 'efa': extraction = 'fullarchive'
    
    
    endp = 'https://api.twitter.com/1.1/tweets/search/' + extraction + '/' + 'mobdata.json'
    print(endp)
    
    # Creating a yaml credentials file
    config = dict(
    search_tweets_api = dict(
        account_type = 'premium',
        endpoint = endp,
        consumer_key = cak,
        consumer_secret = cask
        )
    )

    with open('C:\\Users\\Samuktha\\Documents\\USC\\twitter\\proj\\cred.yaml', 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)
        
    # loading credentials
    premium_search_args = load_credentials('C:\\Users\\Samuktha\\Documents\\USC\\twitter\\proj\\cred.yaml',
                                       yaml_key = 'search_tweets_api',
                                       env_overwrite = True)
    print(premium_search_args)
    print(fdate)
    rule = gen_rule_payload(results_per_call = 100,
                            from_date = fdate + ' '+ ftime, #"2019-07-06 01:00",
                            to_date = tdate + ' ' + ttime, #"2019-07-06 02:15",
                            pt_rule = keywords,
                            )
    
    # result stream
    
    rs = ResultStream(rule_payload = rule,
                      max_results = 10,
                      **premium_search_args)
    

    # save file 
    """
    with open('C:\\Users\\Samuktha\\Documents\\USC\\twitter\\proj\\data.json','a',encoding = 'utf-8') as f:
        for tweet in rs.stream():
            #print('{0}: {1}'.format(str(n), tweet['created_at']))
            json.dump(tweet, f)
            f.write('\n')

    print('done')
    
    """
    
    return rs