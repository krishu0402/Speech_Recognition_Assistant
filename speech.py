import speech_recognition as sr
import datetime
import pytz
import requests
import json
import time
import math

# Initialize recognizer
recognizer = sr.Recognizer()

def recognize_pre_recorded_audio():
    """Function to recognize speech from a pre-recorded audio file"""
    try:
        # Load audio file
        with sr.AudioFile('input.wav') as source:
            print("🔊 Processing pre-recorded audio...")
            audio = recognizer.record(source)
            
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("\nTranscription from pre-recorded audio:")
        print(text + "\n")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio.\n")
    except sr.RequestError as e:
        print(f"Could not request results; {e}\n")
    except FileNotFoundError:
        print("Error: input.wav file not found. Please ensure the file exists.\n")

def live_speech_recognition():
    """Function for live speech recognition like Siri/Google Assistant"""
    with sr.Microphone() as source:
        print("\n🎤 Speak now (say 'stop' to end live listening)...")
        recognizer.adjust_for_ambient_noise(source)  # Optional, for better accuracy
        
        try:
            while True:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
                try:
                    text = recognizer.recognize_google(audio).lower()
                    print("You said:", text)
                    
                    # Check for stop command
                    if 'stop' in text:
                        print("Ending live listening...\n")
                        break
                        
                    # Check for commands
                    process_voice_command(text)
                    
                except sr.UnknownValueError:
                    print("Could not understand audio. Try again.\n")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}\n")
                    
        except KeyboardInterrupt:
            print("\nLive listening stopped by user.\n")

def get_time_info():
    """Function to get current time in London and Nepal"""
    # Get timezones
    london_tz = pytz.timezone('Europe/London')
    nepal_tz = pytz.timezone('Asia/Kathmandu')
    
    # Get current time in UTC
    utc_now = datetime.datetime.now(pytz.utc)
    
    # Convert to London and Nepal time
    london_time = utc_now.astimezone(london_tz)
    nepal_time = utc_now.astimezone(nepal_tz)
    
    # Format the output
    print("\n⏰ Current Time:")
    print(f"London: {london_time.strftime('%Y-%m-%d %H:%M:%S')} ({london_tz.zone})")
    print(f"Nepal: {nepal_time.strftime('%Y-%m-%d %H:%M:%S')} ({nepal_tz.zone})\n")

def get_weather(city):
    """Function to get weather information for a city"""
    # Use OpenWeatherMap API (you need to sign up for a free API key)
    api_key = "9b603d7725918535607fc564667d2d80"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    try:
        complete_url = f"{base_url}appid={api_key}&q={city}"
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main_data = data["main"]
            temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
            pressure = main_data["pressure"]
            humidity = main_data["humidity"]
            weather_data = data["weather"][0]
            weather_desc = weather_data["description"]
            
            print(f"\n🌤 Weather in {city}:")
            print(f"Temperature: {temperature:.1f}°C")
            print(f"Atmospheric Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Weather Description: {weather_desc.capitalize()}\n")
        else:
            print(f"\nCity {city} not found. Please try another city.\n")
    except Exception as e:
        print(f"\nError fetching weather data: {e}\n")

def student_helpdesk():
    """Student Helpdesk with timer and calculator functionality"""
    print("\n📚 STUDENT HELPDESK")
    print("1. Timer")
    print("2. Calculator")
    print("3. Back to main menu")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        timer_feature()
    elif choice == "2":
        calculator_feature()
    elif choice == "3":
        print("Returning to main menu...\n")
    else:
        print("Invalid choice. Please try again.\n")

def timer_feature():
    """Timer feature for the student helpdesk"""
    try:
        duration = int(input("Enter timer duration in seconds: "))
        print(f"⏳ Timer started for {duration} seconds...")
        
        for remaining in range(duration, 0, -1):
            print(f"Time remaining: {remaining} seconds", end='\r')
            time.sleep(1)
            
        print("\n🔔 Timer completed!                                      ")
    except ValueError:
        print("Invalid input. Please enter a number.\n")

def calculator_feature():
    """Calculator feature for the student helpdesk"""
    print("\n🧮 Calculator")
    print("1. Basic Operations (+, -, *, /)")
    print("2. Scientific Operations (sin, cos, tan, log, sqrt)")
    print("3. Back to Helpdesk")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        basic_calculator()
    elif choice == "2":
        scientific_calculator()
    elif choice == "3":
        print("Returning to Helpdesk...\n")
    else:
        print("Invalid choice. Please try again.\n")

def basic_calculator():
    """Basic calculator operations"""
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.\n")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.\n")
            return
            
        print(f"Result: {result}\n")
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

def scientific_calculator():
    """Scientific calculator operations"""
    try:
        print("\nScientific Operations:")
        print("1. Sine (sin)")
        print("2. Cosine (cos)")
        print("3. Tangent (tan)")
        print("4. Logarithm (base 10)")
        print("5. Square Root (sqrt)")
        
        operation = input("Enter operation number (1-5): ")
        num = float(input("Enter number: "))
        
        if operation == '1':
            result = math.sin(math.radians(num))  # Using degrees for trig functions
            print(f"sin({num}°) = {result:.4f}\n")
        elif operation == '2':
            result = math.cos(math.radians(num))
            print(f"cos({num}°) = {result:.4f}\n")
        elif operation == '3':
            result = math.tan(math.radians(num))
            print(f"tan({num}°) = {result:.4f}\n")
        elif operation == '4':
            if num <= 0:
                print("Error: Logarithm is only defined for positive numbers.\n")
                return
            result = math.log10(num)
            print(f"log10({num}) = {result:.4f}\n")
        elif operation == '5':
            if num < 0:
                print("Error: Square root is not defined for negative numbers.\n")
                return
            result = math.sqrt(num)
            print(f"sqrt({num}) = {result:.4f}\n")
        else:
            print("Invalid operation. Please try again.\n")
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

def process_voice_command(text):
    """Process voice commands during live speech recognition"""
    if 'time' in text or 'date' in text:
        get_time_info()
    elif 'weather' in text:
        if 'london' in text:
            get_weather('London')
        elif 'nepal' in text or 'kathmandu' in text:
            get_weather('Kathmandu')
        else:
            print("Please specify a city for weather information (e.g., 'weather in London').\n")
    elif 'helpdesk' in text or 'student help' in text:
        student_helpdesk()
    elif 'exit' in text or 'quit' in text:
        print("Exiting voice command processing...\n")
        return True  # Signal to exit
    return False

def main_menu():
    """Main menu for the application"""
    while True:
        print("\n" + "="*50)
        print("MAIN MENU".center(50))
        print("="*50)
        print("1. Pre-recorded Sound Recognition")
        print("2. Live Speech Recognition (Like Siri/Google Assistant)")
        print("3. Get Current Time and Date (London & Nepal)")
        print("4. Get Weather Information")
        print("5. STUDENT HELPDESK (Timer & Calculator)")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            recognize_pre_recorded_audio()
        elif choice == "2":
            live_speech_recognition()
        elif choice == "3":
            get_time_info()
        elif choice == "4":
            city = input("Enter city name: ")
            get_weather(city)
        elif choice == "5":
            student_helpdesk()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("SPEECH RECOGNITION ASSISTANT".center(50))
    print("="*50)
    main_menu()
