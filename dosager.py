import tkinter as tk
import webbrowser
import requests

def open_website():
    url = entry.get()
    if url:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        webbrowser.open(url)

def send_get_request():
    url = entry.get()
    try:
        num_requests = int(request_count_entry.get())
    except ValueError:
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, "Error: Please enter a valid number of requests.")
        return

    if url:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        try:
            response_text.delete(1.0, tk.END)  # Clear previous content
            for i in range(num_requests):
                response = requests.get(url)
                response_text.insert(tk.END, f"Request {i + 1} - Status Code: {response.status_code}\n")
            response_text.insert(tk.END, "All requests completed successfully.")
        except Exception as e:
            response_text.delete(1.0, tk.END)
            response_text.insert(tk.END, f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Dosager v1.0")

# Create and place the input field for URL
label = tk.Label(root, text="Enter Website URL:")
label.pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create and place the input field for number of requests
request_count_label = tk.Label(root, text="Enter Number of Requests:")
request_count_label.pack(pady=5)

request_count_entry = tk.Entry(root, width=10)
request_count_entry.pack(pady=5)

# Create and place the buttons
open_button = tk.Button(root, text="Open Website", command=open_website)
open_button.pack(pady=5)

get_request_button = tk.Button(root, text="Send GET Requests", command=send_get_request)
get_request_button.pack(pady=5)

# Create a text box to display the GET request responses
response_text = tk.Text(root, height=15, width=60)
response_text.pack(pady=10)

# Run the application
root.mainloop()