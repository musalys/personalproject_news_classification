# Prediction of Naver, Daum News classification

### Why ?
  
  - Can machine classify the news as the human do by reading the content of news?
  - Suppose on-job-situation that other team asked me to extract the keywords in each news category.
    1. Limitations : We only have news title and contents(no clue for news class)
    2. How about using machine-learning for these tasks? Once we make classificaiton model, then We can SAVE TIME!  

### Project's Goal

  - Train existing news from naver.com and automatically predicts new article's topics and fields from daum.net
  - News content(text) are the inputs, and output is the class of news (Politics, Economy, Society, Global, IT/Tech, Culture)
  
### How?

#### Data Collection

  - Crawl the news from(http://news.naver.com/), use them as Traing Data. And Predict Daum News class(http://media.daum.net/)
  - Source Code of Crawler : see https://github.com/musalys/navernewscrawl
  - Use only news contents as X-feature, output(y-target) is class of news.
  
  - 6 topics:
  
  navernews_politics.csv, navernews_economy.csv, navernews_global.csv,
  
  navernews_it.csv, navernews_culture.csv, navernews_society.csv
  
  - Training Data: navernews_category.csv
  - Final Test Data: daumnews_test.csv

#### Methods of Analysis

  - Supervised Learining : TfidfVectorizer, CountVectorizer ==> Support Vector Machine Classifier('linear' kernel)
  - Vectorize text through TfidfVectorizer, CountVectorizer in Scikit-Learn packages.
  - Preprocessing target value y through LabelEncoder in Scikit-Learn packages.
  - Training already classifed 10831 naver news, then predict unlabled(but we know the answer) Daum news


### Results

- Traing 10831 Naver news, model performance scored 0.91
    - preprocessing by TF-idf, SVC model

- Final Test with Daum News(90 articles)
    - 15 articles per each topics(6 topics, 90 articles)
    - Model scored 81% point of performance.

### Conclusion 

- Analysis
    - Crawled between end of November and middle of December(relatively recent), some keywords concentrated 
    - Politics : 최순실, 대통령, 탄핵, 새누리당, 박근혜  ⇒ Mainly related by impeachment of korean president
     - economy : 삼성, 회장, 기업, 금리, 금융 ⇒ Corresponds to Mrs.Choi's Case, presidents and ceo of big company
     - society : 대통령, 퇴진, 집회, 교과서, 촛불집회 ⇒ Keywords that closely related to Candle Rally
     - global  : 트럼프, 미국, 중국, 러시아, 대만 ⇒ Mainly about Donald Trump's actions and comments
     - culture : 서울, 기온 ⇒ Frequently weather news
      -  IT    : 삼성, 애플, 스마트폰, 구글, 아이폰, 갤럭시 ⇒ Mainly about smartphone, samsung, apple, iphone

- Problems
     - Its performance for other times news which have diffent main keywords is somewhat low
          - e.g) news about 'Thaad' in 2016 Jan. ==> predict global category
     - Society category performance are 50% ⇒ Difficulty with extraction of keywords that can tell from other news
     - There are various keywords in accordance with trend and issue, so we need huge amount of data.

- Future plans
    - Proceed Analysis with whole news data in 2016
    - Analyze with similarities(cosine similarity) among other news
    - Using topic modeling in Python genism
       - LDA(Latent Dirichlet Allocation) model use
