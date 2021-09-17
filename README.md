# domain-exploration

These are the notebooks I used to look for patterns in harvard.edu domain names that may indicate if a url was valid (i.e. an actual website). 

To get the data I started with the list of 25K harvard.edu URLs (data/LF_Survey.csv) and engineered some features (e.g. parsed the URL into sub domains, got response status codes, assigned "KEEP/REMOVE/CHECK" values) to get the dataframe for exploring associations and domain names. This is the LF_DomainList_FeatureEngineering.ipynb notebook.

Run the [LF_DomainList_FeatureEngineering.ipynb notebook](https://mybinder.org/v2/gh/derekjackson-das/domain-exploration/main?filepath=LF_DomainList_FeatureEngineering.ipynb) in binder. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/derekjackson-das/domain-exploration/main?filepath=LF_DomainList_FeatureEngineering.ipynb)

Using the dataframe from that notebook I looked at domain names and any correlation to the "REMOVE" value. This is the domain_name_exploration.ipynb notebook.

Run the [domain_name_exploration.ipynb notebook](https://mybinder.org/v2/gh/derekjackson-das/domain-exploration/main?filepath=domain_name_exploration.ipynb) in binder. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/derekjackson-das/domain-exploration/main?filepath=domain_name_exploration.ipynb)

Anf finally I used the apriori method to look at associations between sub-domains and the "REMOVE" value to see if there were patterns with multiple subdomains. This is the Apriori-association-exploration.ipynb notebook.

Run the [Apriori-association-exploration.ipynb notebook](https://mybinder.org/v2/gh/derekjackson-das/domain-exploration/main?filepath=Apriori-association-exploration.ipynb) in binder. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/derekjackson-das/domain-exploration/main?filepath=Apriori-association-exploration.ipynb)

In the end the aprori association rules was interesting but did not turn up any information that just looking at single domain names found. In the end the list of sub-domains used to exclude a site is in the exclusion_list.csv file
