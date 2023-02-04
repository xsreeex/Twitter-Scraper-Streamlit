# Twitter-Scraper-Streamlit
A Twitter Scraper made with Google Colab and Streamlit


![Screenshot (454)](https://user-images.githubusercontent.com/120957359/216751468-b5d51b7a-28e3-4c07-a3db-dac6c880f85a.png)


Today, data is scattered everywhere in the world. Especially in social media, there may be a big quantity of data on Facebook, Instagram, Youtube, Twitter, etc. 
This consists of pictures and films on Youtube and Instagram as compared to Facebook and Twitter. 
To get the real facts on Twitter, you need to scrape the data from Twitter. 


If you are a data enthusiast, you'll likely agree that one of the richest sources of real-world data is social media. Sites like Twitter are full of data.

You can use the data you can get from social media in a number of ways, like sentiment analysis (analyzing people's thoughts) on a specific issue or field of interest.


![image](https://user-images.githubusercontent.com/120957359/216751511-3a43cbcd-db50-40d6-8418-d68988b1bbd1.png)

I've done my project directly using google colab instead of vs-code or anaconda env other applications which are usually used,
i've made it using a local tunnel kind of method where in an application called ngrok would act like my local host 

Ngrok is a simplified API-first ingress-as-a-service that adds connectivity,
security, and observability to your apps with no code changes

!streamlit run app1.py & npx localtunnel --port 8501  <--- this is the code i used to connect my google colab project with ngrok

!./ngrok authtokens 2Kpi06bDZ67r1BCvCkS2i7KP77V_5svQUVT87qr3xSk4bAskC <-- connection from ngrok to google colab has been made using these authentication token

![image](https://user-images.githubusercontent.com/120957359/216751811-d5be7dbf-e90a-41e3-8916-9908b282fbb8.png)

this is how the local tunnel would look like

finally this is how the GUI looks like where you can search, save to database and also download the dataset in csv format .
![image](https://user-images.githubusercontent.com/120957359/216751914-dea35a59-9ca0-4af3-98f8-6f670c4762ef.png)

Happy Coding!😊

