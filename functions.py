import numpy as np

def extract_url_features(url):
    """Extracts various character counts from a URL.

    Args:
        url: The URL string to analyze.

    Returns:
        A dictionary containing the extracted features and their counts.
    """

    features = {
        "url_length": len(url),
        "n_dots": url.count("."),
        "n_hypens": url.count("-"),
        "n_underline": url.count("_"),
        "n_slash": url.count("/"),
        "n_questionmark": url.count("?"),
        "n_equal": url.count("="),
        "n_at": url.count("@"),
        "n_and": url.count("&"),
        "n_exclamation": url.count("!"),
        "n_space": url.count(" "),
        "n_tilde": url.count("~"),
        "n_comma": url.count(","),
        "n_plus": url.count("+"),
        "n_asterisk": url.count("*"),
        "n_hastag": url.count("#"),
        "n_dollar": url.count("$"),
        "n_percent": url.count("%"),
    }
    return features


 

def r_inputs(spchar,q2):
    total_spchar=[]
    sum=0
    for i in spchar:
        total_spchar.append(spchar[i])
    for i in range(1,len(total_spchar)):
        sum=sum+total_spchar[i]
    total_spchar.append(int(q2)) 
    total_spchar.append(sum)
    total_spchar.append(round(sum/spchar['url_length'],2)*10)
    inputs=np.array(total_spchar)
    inputs=np.expand_dims(inputs,axis=0)
    return inputs