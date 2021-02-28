# Warwick-Challenge

[![logo](/img/1.png)]()

# PROJECT GOALS

AI and machine learning have been used heavily in the past decade for commercial application and the development that has taken place has bled into the consumer world. For instance suggestions on streaming services like Netflix and Hulu. When starting our project we knew we wanted to make use of these tools to enhance the user experience without increasing the complexity of the system which seems like an impossible task at first glance. But as we found out during the creation of the project, it is easier that we thought.

While we could go with running the ml model locally through frameworks like CoreML we knew that would limit development and make certain features device specific so we opted to make use of API frameworks to integrate AI.

# PROJECT IDEA

When thinking of realistic implementations of our concept we wondered 'what If we integrated AI into a calculator'. You may ask yourself, why would you integrate AI into a calculator, we thought that too, but we made it anyways.

We ended up creating a calculator app that makes use of the wolfram API to perform complex calculations, this allowed us to create the most sophisticated calculator in the world and implement it in a way in which to the user it is just a simple calculator app.

This allows our calculator to answer all types of complex mathematical functions without having to have everything built on it. This name concept can be applied to IoT devices as well, using cloud services any device can run utilize ml and any application and integrate ML as we did with our project.

# API Implementation 

``` python
def apicall(nn):
  query = str(nn)
  app_id = "API-KEY"
  url = 'http://api.wolframalpha.com/v1/result?i=%s&appid=%s' %(query, app_id)
  req = requests.get(url)
    # Set debug flag to 1 to enable.
  debug = 1

  if debug == 1:
      print("----------------------")
      print("DEBUG INFORMATION")
      print("DEBUG (URL) : ", url)
      print("DEBUG: ", 'Requesting content')
      print("DEBUG (Status code) : ", req.status_code)
      print("----------------------")

  client = wolframalpha.Client(app_id)
  res = client.query(query)

  try:
    answer = next(res.results).text
  except:
    print("Unable to process query.")

  print("----------------------")
  print("Answer:")
  print(answer)
  print("----------------------")
  return answer
```

# Installation 

``` bash
python3 -m pip install pyforms-gui
python3 -m pip install wolframalpha
python3 -m pip install requests
```

# Debug Mode

Set flag in line 16 to 1. (It is set to on my default)
