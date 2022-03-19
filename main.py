from flask import Flask, render_template
import requests, json
app = Flask('app')


@app.route('/')
def home():
  return render_template("index.html")


@app.route('/page1')
def page1():

  #making api call
  url = 'https://www.balldontlie.io/api/v1/games/1'

  #store API response in a json file
  r = requests.get(url).json()

  #dumping into a json File
  filename = 'data2.json'
  with open(filename, 'w') as fobj:
    json.dump(r, fobj, indent = 4)

  #loading a json File
  filename = 'data2.json'
  with open(filename) as fobj:
    all_data = json.load(fobj)

  #print(all_data)
  #extracting data from json file and appending to a list
  team_score = []
  #extract = ['Boston Celtics', 'Philadelphia 76ers']

  data = all_data['home_team_score']
  team_score.append(data)

  data = all_data['visitor_team_score']
  team_score.append(data)
    
  print(team_score)

  labels = ['Boston Celtics', 'Philadelphia 76ers']
  values = team_score

  #making second api call
  url2 = 'https://www.balldontlie.io/api/v1/season_averages?season=2018&player_ids[]=237&player_ids[]=115'

  #store API response in a json file
  r = requests.get(url2).json()

  #dumping into a json File
  filename = 'data.json'
  with open(filename, 'w') as fobj:
    json.dump(r, fobj, indent = 4)

  #loading a json File
  filename = 'data.json'
  with open(filename) as fobj:
    all_data = json.load(fobj)

  #print(all_data)
  #extracting data from json file and appending to a list
  lebron, steph = [], []
  extract = ['games_played', 'ftm', 'dreb', 'reb', 'ast', 'pts' ]

  for item in extract:
    data = all_data['data'][0][item]
    lebron.append(data)

  for item in extract:
    data = all_data['data'][1][item]
    steph.append(data)

  print(lebron)
  print(steph)


  #making third api call
  url3 = 'https://www.balldontlie.io/api/v1/games/2'

  #store API response in a json file
  r = requests.get(url3).json()

  #dumping into a json File
  filename = 'data3.json'
  with open(filename, 'w') as fobj:
    json.dump(r, fobj, indent = 4)

  #loading a json File
  filename = 'data3.json'
  with open(filename) as fobj:
    all_data = json.load(fobj)

  #print(all_data)
  #extracting data from json file and appending to a list
  team_score = []
  #extract = ['Boston Celtics', 'Philadelphia 76ers']

  data = all_data['home_team_score']
  team_score.append(data)

  data = all_data['visitor_team_score']
  team_score.append(data)
    
  print(team_score)

  labels2 = ['Golden State Warriors', 'Oklahoma City Thunder']
  values2 = team_score

  return render_template('page1.html', labels=labels, values=values, extract=extract, lebron=lebron, steph=steph, labels2=labels2, values2=values2)


@app.route('/page2')
def page2():

  #making fourth api call
  url4 = 'https://www.balldontlie.io/api/v1/season_averages?season=2019&player_ids[]=117&player_ids[]=145&player_ids[]=192'

  #store API response in a json file
  r = requests.get(url4).json()

  #dumping into a json File
  filename = 'data4.json'
  with open(filename, 'w') as fobj:
    json.dump(r, fobj, indent = 4)

  #loading a json File
  filename = 'data4.json'
  with open(filename) as fobj:
    all_data = json.load(fobj)

  #print(all_data)
  #extracting data from json file and appending to a list
  davis, embiid, harden = [], [], []
  extract2 = ['turnover', 'stl', 'fg3a', 'reb', 'fta', 'ftm' ]

  for item in extract2:
    data = all_data['data'][0][item]
    davis.append(data)

  for item in extract2:
    data = all_data['data'][1][item]
    embiid.append(data)

  for item in extract2:
    data = all_data['data'][2][item]
    harden.append(data)

  print(davis)
  print(embiid)
  print(harden)


  #making fifth api call
  url5 = 'https://www.balldontlie.io/api/v1/season_averages?season=2005&player_ids[]=237'

  #store API response in a json file
  r = requests.get(url5).json()

  #dumping into a json File
  filename = 'data5.json'
  with open(filename, 'w') as fobj:
    json.dump(r, fobj, indent = 4)

  #loading a json File
  filename = 'data5.json'
  with open(filename) as fobj:
    all_data = json.load(fobj)

  #print(all_data)
  #extracting data from json file and appending to a list
  lebron = []
  extract3 = ['fga', 'fgm', 'fg3a', 'oreb', 'ast', 'ftm' ]

  for item in extract3:
    data = all_data['data'][0][item]
    lebron.append(data)

  print(lebron)

  return render_template('page2.html', harden=harden, davis=davis, embiid=embiid, extract2=extract2, lebron=lebron, extract3=extract3)

app.run(host='0.0.0.0', port=8080, debug = True)
