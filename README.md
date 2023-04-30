# the-kitchen-sink
Literally everything but the kitchen sink! GPT4 API + Llama + GPT-NEO 125m Intercom AI
working intercom!

![image](https://user-images.githubusercontent.com/34530588/235335021-40db1616-f9a5-4bcc-b2b0-00f9e794d3b9.png)


 Python script that creates a graphical user interface (GUI) for an AI conversation application. The application allows users to enter text input and receive responses from three different AI models: Llama, GPT-Neo, and GPT-4 (ChatGPT plugin model). The responses from the three models are displayed in the GUI.

Here is a breakdown of the key components of the code:

Importing Libraries: The script imports the necessary libraries and modules, including json, torch, openai, tkinter, and transformers. It also imports the Llama class from llama_cpp.

Llama Model: The script initializes the Llama model using a specified model path.

GPT-Neo Model: The script initializes the GPT-Neo model using the transformers library and loads the model onto the appropriate device (CPU or GPU).

GPT-4 (ChatGPT) Model: The script defines a function gpt4_generate that uses the OpenAI API to generate responses from the GPT-4 model. The user needs to replace "replacekey" with their actual API key.

Intercommunication Function: The intercommunication function takes user input and generates responses from all three models (Llama, GPT-Neo, and GPT-4). The responses are combined and returned as a single string.

GUI Setup: The script uses the tkinter library to create a GUI with an input field, a generate button, and an output text area. The user can type input into the input field and click the generate button to receive responses from the AI models. The responses are displayed in the output text area.

Event Binding: The script binds the Enter key to the generate button click event, allowing the user to generate responses by pressing Enter.

Main Loop: The script runs the main event loop for the GUI using root.mainloop().

Please note that the script assumes that the Llama model and the GPT-Neo model are available on the system, and that the user has a valid API key for accessing the GPT-4 model via the OpenAI API. Additionally, the script uses the llama_cpp module, which is not a standard Python module and may require custom installation or setup using `pip install llama-cpp-python. As well as pytorch requirements can be installed with the guide here. (i use anaconda) https://pytorch.org .


Love your enemies! 
