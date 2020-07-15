from searchtweets import load_credentials
from searchtweets import gen_rule_payload
from searchtweets import ResultStream
import yaml
import json

def get_file(aname, cak, cask, etype, hashtag, keywords, fdate = '00-00-0000', tdate = '00-00-0000', ftime = '00:00', ttime = '00:00'):
    
    if etype == 'efa': # Full archive scraping (refer to limits on README)
        endp = 'https://api.twitter.com/1.1/tweets/search/fullarchive/' + aname + '.json'
    elif etype == 'tdays': # 30 days scraping (refer to limits on README)
        endp = 'https://api.twitter.com/1.1/tweets/search/30day/' + aname + '.json'
    else:
        endp = 'ERROR'
     
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
    
    if etype == 'efa':
        rule = gen_rule_payload(results_per_call = 100,
                                from_date = fdate + ' '+ ftime, #"2019-07-06 01:00",
                                to_date = tdate + ' ' + ttime, #"2019-07-06 02:15",
                                pt_rule = keywords,
                                )
    else:
        rule = gen_rule_payload(results_per_call = 100,
                               pt_rule = keywords)
            
    
    # result stream

    rs = ResultStream(rule_payload = rule,
                      max_results = 50,
                      **premium_search_args)
    

    
    
    return rs
