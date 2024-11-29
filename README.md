# [TG] BaSiC Bot

**[@tgBaSiCBot](https://github.com/AbOutMeDK/tgBaSiCbOt)** is an initiative by the **Exam Vault** team, designed to provide a comprehensive and user-friendly guide for anyone looking to start their journey in Telegram Bot development.

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

---

By following these steps, you can easily host your Telegram bot on Render and get it up and running quickly!

---

## Are You a Beginner?

If you're new to Telegram bot development, follow these steps after the successful deployment:

1. **Check Your Bot**: Test the bot you created using @BotFather.
2. **Test the `/start` Command**: If you receive a reply, your deployment was successful. If not, check the application log for errors and feel free to ask for help in our support group.
3. **Request Verification**: If your deployment is successful, you can request verification for your bot.
4. **Verify Your Bot**: Use [@tgBaSiCBot](https://t.me/tgBaSiCBot) to verify your bot once deployment is confirmed.
5. **Join the Private Group**: After verification, you will be invited to a private group for bot builders.
6. **Get Ready to Build**: If you receive the group link, you are set to start building Telegram bots.
7. **Receive Support**: Our team is here to assist you in modifying or enhancing your BaSiC bot to an advanced version based on your ideas.

---

## Usage

To run your bot, execute the following command in your terminal:

`python3 main.py`

## For queries 

You can ask your doubts in our Support Chat : [@BaSiCBotChat](https://t.me/BaSiCBotChat)

## Happy Deploying...

**We hope this project will help those interested in building Telegram bots but don't know where to start. We're here to guide you. Let's build it together 🎉**

