# Weather_bot
This is a Weather API chatbot, which will tell you about the current weather and it is built using the RASA framework.

I started this project to get familiar with developing chatbots, since the RASA Framework was open source i opted for it.



## Introduction to RASA 
Please refer to the blog where I have explained the basics of how to get started with the RASA Framework.

[How to build a conversational AI assistant with Rasa](https://medium.com/@karthikvegeta/how-to-build-a-conversational-ai-assistant-with-rasa-83caa1341ab9)

## Working of the bot
**Project Explanation: Weather API Chatbot using RASA Framework**
The Link for the demo is given in the DEMO section.

**1. Why Weather API Chatbot:**

   The Weather API chatbot serves as a convenient and user-friendly tool for retrieving real-time weather information. It leverages the RASA Framework to create a natural language interface, allowing users to inquire about weather conditions in a conversational manner. This project is particularly useful for individuals who want quick and accurate weather updates without needing to navigate complex interfaces.

**2. Developing NLU and Stories:**

   - **Natural Language Understanding (NLU):** The NLU component involves training the chatbot to understand user inputs. Using RASA's NLU capabilities, the model is trained on a dataset that includes examples of user queries related to weather conditions (e.g., "What's the weather like today?", "Tell me the temperature in New York"). This enables the bot to comprehend and extract relevant information from user messages.
   
   - **Stories:** Stories represent conversational flows or dialogues between users and the chatbot. In the context of a weather API chatbot, stories define the paths a conversation can take. These stories are created to cover various scenarios, ensuring the chatbot can handle diverse interactions.

Example:

User: Hi/Hello

Bot: The bot will greet the user with Good Morning/Good Afternoon/Good Evening based on the current time, followed by "Welcome I am a weather bot", and "How can I help you?"

User: 
what is the weather in location / what is the weather now?

           - there are 2 situations involved here.
           
           1. the user will directly ask for the weather along with the location mentioned.
           
           2. the user will ask only for the weather without mentioning the location.	

Bot:       

           1. the bot will collect the location from the text, hit the API, and fetch the weather for the location.

           2. if the location is not mentioned the bot will ask  for the location, hit the API, and fetch the weather for the location.
           
Bot:  Did that help you?

User: Yes/No.

Bot: 1. Yes - Thanks for the feedback. 

Bot: 2. No- Sorry to hear from you. This feedback is noted for improvement.

User: Bye

Bot: Bye, we can catch up after some time. 

The bot is also trained in a few more situations where,

If any gibberish words or questions are asked it will respond that: sorry couldn't understand you can you please come again

If any out-of-context questions are asked it will respond that: this is out of my scope of work.


**3. Getting API from OpenWeather:**
   - **OpenWeather API:** To provide accurate and up-to-date weather information, the chatbot integrates with the OpenWeather API.

   - **API Integration:** RASA's custom actions can be implemented to handle API calls. These actions trigger the communication with the OpenWeather API, retrieve the weather data, and format it for user-friendly responses. The API key is securely stored and utilized to authenticate each request, ensuring the chatbot has access to the necessary weather information.

**4. Uses of the Chatbot:**

   - **Weather Updates:** Users can inquire about current weather conditions, forecasts, and other relevant details for specific locations.
     
   - **Conversational Interaction:** The chatbot provides a conversational interface, allowing users to interact with the weather service naturally.
     
   - **User Engagement:** Enhances user engagement by providing information quickly and interactively.
     
   - **Accessibility:** Enables users to access weather information without complex navigation in weather applications.

**5. Conclusion:**

   The Weather API chatbot using the RASA Framework offers a seamless and user-friendly experience for obtaining weather information. By integrating with the OpenWeather API, the chatbot ensures accurate and timely responses. The project showcases the potential of natural language processing in creating practical and accessible solutions. It serves as a foundation for expanding conversational AI applications into various domains, making information retrieval more intuitive and engaging for users.



## Acknowledgement
[RASA](https://rasa.com/docs/rasa/)

[BotFront](https://github.com/botfront/botfront)
## Authors

- [@Karthik](https://www.linkedin.com/in/l-karthik/)


## Demo

https://www.linkedin.com/in/l-karthik/


## Documentation

[RASA](https://rasa.com/docs/rasa/)

[BotFront](https://github.com/botfront/botfront)


## Installation

To get started:

```bash
  !pip install rasa
  rasa init 
  rasa run actions 
  rasa shell 
  rasa vizaualize
```
    

## FlowChart

The Flow of the the chatbot is included in the file named graph.
## 🚀 About Me
Self-driven and Aspiring Engineer with a keen focus on Artificial Intelligence. Demonstrated dedication and enthusiasm toward applying data-driven decision-making techniques to solve real-world industry challenges. Equipped with the knowledge and skills to add substantial value through the development and implementation of innovative solutions. Committed to contributing to the advancement of the field and making a meaningful impact on the industry.

I am a driven and optimistic individual eagerly seeking a dynamic and demanding platform to demonstrate my skill set while gaining fresh insights. I look at every task with diligence, making sure that the set objectives are completed. My strong organizational and time management abilities empower me to excel across diverse settings.

My expertise lies within the domain of Python, Artificial Intelligence, Data Analysis, and Machine Learning.

Technical Proficiencies:

Python 3
Statistics
MySQL
Data Analytics
Machine Learning
GenerativeAI
PowerBI

Completed my graduation in Engineering in the stream of Electronics and communication with [7.97 CGPA].

My path to Artificial Intelligence started in 2020 when I was attracted to the way it functions. Since then my interest in AI has never been down and wanted to contribute and provide solutions in this domain. For sure in the near future, I will be on my way to contributing, and currently working on becoming an Artificial Intelligence Engineer.Seeking to use my skills and knowledge to make a positive impact as a data scientist.

I'm a quick learner and enthusiastic about participating in extracurricular activities, with my talent I'm looking for an opportunity to take the next step in my career.

🔭 I’m currently working on to improve myself

🌱 I’m currently learning Python3

💬 Soon in the near future ask me about Artificial
 Intelligence stuff

📫 How to reach me:
 PORTFOLIO : https://karthik-56.github.io/Karthik_Portfolio/

 BLOG : https://sites.google.com/view/karthikaiblogs/home

 PERSONAL INSTAGRAM : https://www.instagram.com/prince_6_karthik/

 INSTAGRAM : https://www.instagram.com/_.pythonista._/

 MEDIUM : https://karthikvegeta.medium.com/

 GMAIL : karthiksurya611@gmail.com

⚡ Fun fact: I got inspired by Tony Stark ✌️ and Motivated by 💪 Prince Vegeta ♕


