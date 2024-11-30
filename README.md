# [TG] BaSiC Bot

This project features a simplified Python repository that serves as a solid foundation for both beginners and experienced developers interested in creating their own Telegram bots.

---

## Getting Started

### Required Credentials

To begin, you will need the following credentials:

- **`API_ID`**: Obtain your API ID from [my.telegram.org](https://my.telegram.org).
- **`API_HASH`**: Obtain your API Hash from [my.telegram.org](https://my.telegram.org).
- **`BOT_TOKEN`**: Get your Bot's API Token from [@BotFather](https://t.me/BotFather).
- **`OWNER_ID`**: Retrieve your Telegram account's UserID from [@tgBaSiCBot](https://t.me/tgBaSiCBot).

> **Note**: For more information about these credentials, please refer to `@tgBaSiCBot` on Telegram.

---

### Deployment

We recommend deploying your bot on **[Render](https://render.com/)**, which offers application to be hosted for free. Follow these steps to deploy your bot:

1. **Fork the Repository**: Start by forking this repository to your own GitHub account. You can do this by clicking the "Fork" button at the top right of the repository page on GitHub.

2. **Create a Render Account**: Go to [Render](https://render.com/) and sign up for a free account if you don’t have one already.

3. **Connect Your GitHub Account**: After logging in to Render, navigate to the "Dashboard" and click on "New" > "Web Service". You will be prompted to connect your GitHub account. Follow the instructions to authorize Render to access your GitHub repositories.

4. **Select Your Forked Repository**: Once your GitHub account is connected, you will see a list of your repositories. Select the forked repository of the BaSiC Bot.

5. **Configure Your Service**:
   - **Name**: Give your service a name.
   - **Region**: Choose a region that is closest to your users.
   - **Branch**: Select the branch you want to deploy (`main`).
   - **Build Command**: Enter the command to install dependencies, `pip install -r requirements.txt`.
   - **Start Command**: Enter the command to run your bot, typically `python3 main.py`.

6. **Set Environment Variables**: In the "Environment" section, add the following environment variables with your actual values:
   - `API_ID`: Place your Telegram API ID.
   - `API_HASH`: Place your Telegram API Hash.
   - `BOT_TOKEN`: Place your Bot's API Token.
   - `OWNER_ID`: Place your Telegram account's UserID.

7. **Deploy Your Bot**: Click the "Create Web Service" button to start the deployment process. Render will build and deploy your bot automatically.

8. **Check Your Bot**: Once the deployment is complete, you can test your bot by sending the `/start` command in Telegram. If you receive a reply, your deployment was successful. If not, check the application logs for errors.

### Add a Monitor in UptimeRobot

To keep the Render application alive, follow these steps to add a monitor in UptimeRobot:

1. **Sign Up or Log In**
   - Visit [UptimeRobot.com](https://uptimerobot.com) and create an account or log in to your existing account.

2. **Navigate to the Dashboard**
   - After logging in, you will be directed to your dashboard where you can manage your monitors.

3. **Add a New Monitor**
   - Click on the **"+ Add New Monitor"** button located on the left side of the dashboard.
   - Choose the type of monitor you want to create (e.g., HTTP(s), Keyword, Ping, etc.).

4. **Configure Monitor Settings**
   - **Friendly Name**: Enter a name for your monitor that helps you identify it.
   - **URL or IP Address**: Input the URL or IP address of the service you want to monitor (Your Render application link).
   - **Monitoring Interval**: Set how often you want UptimeRobot to check the status (minimum interval is 5 minutes for free accounts).
   - **Alert Contacts**: Select the alert contacts that should be notified if the monitor goes down.

5. **Advanced Settings (Optional)**
   - For Keyword monitors, specify the keyword to check for and the condition (e.g., "Keyword Exists" or "Keyword Not Exists").
   - Configure any additional settings as needed.

6. **Save the Monitor**
   - After filling in all the necessary information, click on the **"Create Monitor"** button to save your settings.

7. **Monitor Status**
   - Your new monitor will now appear in the dashboard, and you can view its status and performance metrics.

8. **Testing the Monitor**
   - Use the **Test Notification** feature to ensure alerts are working correctly.
---

By following these steps, you can easily host your Telegram bot on Render and get it up and running quickly!

---

## Are You a Beginner?

If you're new to Telegram bot development, follow these steps after the successful deployment:

1. **Test your Bot**: Test your bot by sending the `/start` command in Telegram. If you receive a reply, your deployment was successful. If not, check the application log for errors and feel free to ask for help in our support group.
2. **Request Verification**: If your deployment is successful, you can request verification for your bot.
3. **Verify Your Bot**: Use [@tgBaSiCBot](https://t.me/tgBaSiCBot) to verify your bot once deployment is confirmed.
4. **Join the Private Group**: After verification, you will be invited to a private group for bot builders.
5. **Get Ready to Build**: If you receive the group link, you are set to start building Telegram bots.
6. **Receive Support**: Our team is here to assist you in modifying or enhancing your BaSiC bot to an advanced version based on your ideas.

---

## Usage

To run your bot, execute the following command in your terminal:

`python3 main.py`

## For queries 

You can ask your doubts in our Support Chat : [@BaSiCBotChat](https://t.me/BaSiCBotChat)

## Happy Deploying...

**We hope this project will help those interested in building Telegram bots but don't know where to start. We're here to guide you. Let's build it together 🎉**

