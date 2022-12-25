Firebase Setup Notes by me - https://descriptive-agate-1d5.notion.site/Firebase-Notifications-02df71eb7a8c4f669c79bbf79178cf12

Steps to use this project:
1. Create virtual environment
   `python3 -m venv my-project-env`
2. Install packages: `pip3 install -r requirements.txt`
3. Point the mongo uri with a database name in `.env`
4. Run the FASTAPI application: `uvicorn app.main:app --port 5000`
5. Run: test.html using a http server: `python -m SimpleHTTPServer`
6. Navigate to `/firebase_toy/app/server/firebase/admin_sdk/test.html` in two browsers to simulate the sender and receiver.
7. Obtain device tokens for the two browsers in the console of test.html
8. End points flow to send and recieve a test message:
    - /create_user
    - /subscribe
    - /test_notification

