# Knox/utils/messages.py

# =====================================================================================
# ====== ERROR MESSAGES ======
# =====================================================================================

# ------ General Errors ------
MSG_ERROR_GENERIC = "⚠️ **Oops!** Something unexpected happened. Please try again. If the issue persists, kindly contact our support team."
MSG_ERROR_USER_INFO = "❗ **User Not Found:** I couldn't find that user. Please double-check the ID or Username."

# ------ User Input & Validation Errors ------
MSG_INVALID_USER_ID = "❌ **Invalid User ID:** Please provide a valid numeric user ID."
MSG_ERROR_START_BOT = "⚠️ Please start the bot in our private chat first!\n👉 [Click here to start]({invite_link})"
MSG_ERROR_REPLY_FILE = "⚠️ Please use the `/link` command by replying directly to a file."
MSG_ERROR_NO_FILE = "⚠️ The message you replied to doesn't seem to contain a file."
MSG_ERROR_INVALID_NUMBER = "⚠️ **Invalid number specified.** Please check your input."
MSG_ERROR_NUMBER_RANGE = "⚠️ **Out of bounds:** Please specify a number between 1 and {max_files}."
MSG_ERROR_DM_FAILED = "⚠️ I couldn't send you a direct message. Please ensure you have started the bot in private first!"

# ------ File & Media Errors ------
MSG_ERROR_PROCESSING_MEDIA = "⚠️ **Processing Failed:** I encountered an error while processing your media. Please try sending it again."

# ------ Admin Action Errors (Ban, Auth, etc.) ------
MSG_AUTHORIZE_FAILED = (
    "❌ **Authorization Failed:**\n"
    "Could not grant access to user `{user_id}`."
)
MSG_DEAUTHORIZE_FAILED = (
    "❌ **Deauthorization Failed:**\n"
    "User `{user_id}` was not authorized or an error occurred."
)
MSG_TOKEN_FAILED = (
    "⚠️ **Token Activation Failed!**\n\n"
    "🔍 **Reason:** {reason}\n\n"
    "🔑 Please verify your token or contact support for assistance."
)
MSG_SHELL_ERROR = "❌ **Shell Command Error:**\n<pre>{error}</pre>"

# ------ System & Bot Errors ------
MSG_ERROR_NOT_ADMIN = "⚠️ **Admin Required:** I need to be an administrator in this chat to function properly."
MSG_DC_INVALID_USAGE = "🤔 **Invalid Usage:** Please reply to a user's message or a media file to fetch the DC info."
MSG_DC_ANON_ERROR = "😥 **Identification Failed:** Unable to identify you. This command may not work for anonymous admins."
MSG_DC_FILE_ERROR = "⚙️ **File Data Error:** Could not fetch data center details. The file might be inaccessible."
MSG_STATS_ERROR = "❌ **Stats Error:** Unable to retrieve system statistics at this moment."
MSG_STATUS_ERROR = "❌ **Status Error:** Unable to retrieve system status."
MSG_DB_ERROR = "❌ **Database Error:** Could not retrieve user statistics."
MSG_CRITICAL_ERROR = (
    "🚨 **Critical System Error Detected** 🚨\n\n"
    "⚠️ **Details:**\n```\n{error}\n```\n\n"
    "🛠 Please investigate immediately! (Error ID: {error_id})"
)

# =====================================================================================
# ====== ADMIN MESSAGES ======
# =====================================================================================

# ------ Ban/Unban ------
MSG_DECORATOR_BANNED = "⛔ **Access Denied!** You have been banned from using this bot.\n\n📝 **Reason:** {reason}\n🕒 **Date:** {ban_time}"
MSG_BAN_USAGE = "⚠️ **Usage:** `/ban [user_id] [reason]`"
MSG_CANNOT_BAN_OWNER = "❌ **Error:** You cannot ban an owner of the bot."
MSG_ADMIN_USER_BANNED = "✅ **Success:** User {user_id} has been permanently banned."
MSG_BAN_REASON_SUFFIX = "\n📝 **Reason:** {reason}"
MSG_ADMIN_NO_BAN_REASON = "No reason provided."
MSG_USER_BANNED_NOTIFICATION = "🚫 **Alert:** You have been banned from using this service."
MSG_UNBAN_USAGE = "⚠️ **Usage:** `/unban <user_id>`"
MSG_ADMIN_USER_UNBANNED = "✅ **Success:** User {user_id} has been unbanned."
MSG_USER_UNBANNED_NOTIFICATION = "🎉 **Good News!** Your ban has been lifted. You can now use the bot again."
MSG_USER_NOT_IN_BAN_LIST = "ℹ️ **Notice:** User {user_id} is not currently banned."
MSG_CHANNEL_BANNED = "✅ **Success:** Channel {channel_id} has been banned."
MSG_CHANNEL_BANNED_REASON_SUFFIX = "\n📝 **Reason:** {reason}"
MSG_CHANNEL_UNBANNED = "✅ **Success:** Channel {channel_id} has been unbanned."
MSG_CHANNEL_NOT_BANNED = "ℹ️ **Notice:** Channel {channel_id} is not currently banned."

# ------ Token & Authorization ------
MSG_AUTHORIZE_USAGE = "🔑 **Usage:** `/authorize <user_id>`"
MSG_DEAUTHORIZE_USAGE = "🔒 **Usage:** `/deauthorize <user_id>`"
MSG_AUTHORIZE_SUCCESS = (
    "✅ **User Successfully Authorized!**\n\n"
    "👤 **User ID:** `{user_id}`\n"
    "🔑 **Access Level:** Permanent"
)
MSG_DEAUTHORIZE_SUCCESS = (
    "✅ **User Deauthorized!**\n\n"
    "👤 **User ID:** `{user_id}`\n"
    "🔒 **Access Level:** Revoked"
)
MSG_TOKEN_ACTIVATED = "✅ **Token Activated Successfully!**\n\n⏳ Your premium access is now valid for {duration_hours} hours. Enjoy!"
MSG_TOKEN_INVALID = "🚫 **Token Expired or Invalid.**\n\nPlease click the button below to request a new access token."
MSG_NO_AUTH_USERS = "ℹ️ **Empty List:** There are currently no authorized users in the database."
MSG_AUTH_USER_INFO = """{i}. 👤 **ID:** `{user_id}`
   🛡️ **By:** `{authorized_by}`
   🕒 **Date:** `{auth_time}`\n\n"""
MSG_ADMIN_AUTH_LIST_HEADER = "🔐 **List of Authorized Users**\n\n"

# ------ Shell Commands ------
MSG_SHELL_USAGE = (
    "💻 **Terminal Usage:**\n"
    "`/shell <command>`\n\n"
    "💡 **Example:**\n"
    "`/shell ls -l`"
)
MSG_SHELL_EXECUTING = "⚙️ **Executing Command...**\n<pre>{command}</pre>"
MSG_SHELL_OUTPUT = "💻 **Command Output:**\n<pre>{output}</pre>"
MSG_SHELL_OUTPUT_STDOUT = "🟢 **[stdout]:**\n<pre>{output}</pre>"
MSG_SHELL_OUTPUT_STDERR = "🔴 **[stderr]:**\n<pre>{error}</pre>"
MSG_SHELL_NO_OUTPUT = "✅ **Executed Successfully:** (No output returned)"

# ------ Admin View & Control ------
MSG_WORKLOAD_ITEM = "   🖥️ {bot_name}: {load} active tasks\n"
MSG_ADMIN_RESTART_DONE = "✅ **System Restart Completed Successfully!**"
MSG_RESTARTING = "♻️ **System is Updating & Restarting...**\n\n⏳ Please hold on, this will only take a moment."
MSG_LOG_FILE_CAPTION = "📄 **System Log Export**"
MSG_LOG_FILE_EMPTY = "ℹ️ **Notice:** The system log is currently empty."
MSG_LOG_FILE_MISSING = "⚠️ **Error:** Could not locate the system log file."

# =====================================================================================
# ====== BUTTON TEXTS (User-facing) ======
# =====================================================================================

MSG_BUTTON_STREAM_NOW = "🖥️ Stream Now"
MSG_BUTTON_DOWNLOAD = "📥 Download"
MSG_BUTTON_GET_HELP = "📖 Help Menu"
MSG_BUTTON_CANCEL_BROADCAST = "🛑 Cancel Broadcast"
MSG_BUTTON_VIEW_PROFILE = "👤 My Profile"
MSG_BUTTON_ABOUT = "ℹ️ About Bot"
MSG_BUTTON_JOIN_CHANNEL = "📢 Join {channel_title}"
MSG_BUTTON_START_CHAT = "🚀 Start Bot"
MSG_BUTTON_CLOSE = "✖️ Close Menu"


# =====================================================================================
# ====== COMMAND RESPONSES (User-facing) ======
# =====================================================================================

MSG_WELCOME = (
    "🌟 **Welcome to File Stream!** 🌟\n\n"
    "Hello **{user_name}**, it's great to have you here! 👋\n\n"
    "I can help you instantly convert any Telegram file into a high-speed **Stream** and **Download** link.\n\n"
    "🎯 **How to use me:**\n"
    "🔹 **Private Chat:** Just send me any file directly.\n"
    "🔹 **Groups:** Reply to a file with the `/link` command.\n\n"
    "🚀 _Send a file now to get started!_"
)

MSG_HELP = (
    "📖 **Help & Instructions**\n\n"
    "**1️⃣ Using in Private Chat**\n"
    "Simply forward or send any media file to me, and I will instantly generate your personalized links.\n\n"
    "**2️⃣ Using in Groups**\n"
    "Reply to any file with `/link` (I must be an admin in the group).\n"
    "Need multiple links? Use batch mode: `/link 5` (processes up to {max_files} files at once).\n\n"
    "**🛠 Available Commands**\n"
    "🔸 `/start` - Launch the bot\n"
    "🔸 `/help` - Show this menu\n"
    "🔸 `/about` - Information about the bot\n"
    "🔸 `/ping` - Check server latency\n"
    "🔸 `/dc` - Get Data Center info\n\n"
    "💡 _Tip: Make sure you have started me in a private chat before using group commands!_"
)

MSG_ABOUT = (
    "ℹ️ **About File Stream Bot**\n\n"
    "A powerful, lightning-fast Telegram bot designed to bridge your files with the web.\n\n"
    "✨ **Core Features:**\n"
    "🚀 Instant Link Generation\n"
    "🖥️ In-browser HD Streaming\n"
    "📁 Supports all major file formats\n"
    "🔒 Secure and private routing\n"
    "⚡ Seamless batch processing\n\n"
    "👨‍💻 **Maintained by:** [@knoxprojects](https://t.me/knoxprojects)"
)

# ------ Ping ------
MSG_PING_START = "🛰️ **Pinging servers...**"
MSG_PING_RESPONSE = (
    "✅ **System is Online!**\n\n"
    "⚡ **Latency:** `{time_taken_ms:.2f} ms`\n"
    "🟢 **Status:** `Operational`"
)

# ------ DC Info ------
MSG_DC_USER_INFO = (
    "📍 **User Data Center Info**\n\n"
    "👤 **Name:** [{user_name}](tg://user?id={user_id})\n"
    "🆔 **User ID:** `{user_id}`\n"
    "🌍 **DC ID:** `{dc_id}`"
)

MSG_DC_FILE_INFO = (
    "🗂️ **File Data Center Info**\n\n"
    "📄 **Name:** `{file_name}`\n"
    "📊 **Size:** `{file_size}`\n"
    "📁 **Type:** `{file_type}`\n"
    "🌍 **Hosted on DC:** `{dc_id}`"
)

MSG_DC_UNKNOWN = "Unknown"

# ------ File Link Generation ------
MSG_DM_SINGLE_PREFIX = "📬 **Source:** {chat_title}\n\n"
MSG_LINKS = (
    "✨ **Links Generated Successfully!** ✨\n\n"
    "📁 **File:** `{file_name}`\n"
    "📊 **Size:** `{file_size}`\n\n"
    "🖥️ **Stream Online:**\n"
    "└ {stream_link}\n\n"
    "📥 **Direct Download:**\n"
    "└ {download_link}\n\n"
    "💡 _Click the buttons below to access your media!_"
)

# =====================================================================================
# ====== USER NOTIFICATIONS ======
# =====================================================================================

MSG_NEW_USER = (
    "👋 **New User Registration**\n\n"
    "👤 **User:** [{first_name}](tg://user?id={user_id})\n"
    "🆔 **ID:** `{user_id}`"
)
MSG_COMMUNITY_CHANNEL = "📢 **Notice:** Please join **{channel_title}** to continue using the bot."

# =====================================================================================
# ====== PROCESSING MESSAGES ======
# =====================================================================================

# ------ General File Processing ------
MSG_PROCESSING_REQUEST = "⏳ **Initializing request...**"
MSG_PROCESSING_FILE = "⏳ **Generating secure links...**"
MSG_NEW_FILE_REQUEST = (
    "🚀 **New File Processed!**\n\n"
    "👤 **User:** [{source_info}](tg://user?id={id_})\n"
    "🆔 **ID:** `{id_}`\n\n"
    "🖥️ **Stream:** `{stream_link}`\n"
    "📥 **Download:** `{online_link}`"
)

# ------ Batch Processing ------
MSG_PROCESSING_BATCH = "♻️ **Processing Batch {batch_number}/{total_batches}**\n> 📊 Total Files: {file_count}"
MSG_PROCESSING_STATUS = "📊 **Live Status:** {processed}/{total} completed | ❌ {failed} failed"
MSG_BATCH_LINKS_READY = "🔗 **Batch Processing Complete!**\nHere are your {count} links:"
MSG_DM_BATCH_PREFIX = "📬 **Batch Results from {chat_title}**\n\n"
MSG_PROCESSING_RESULT = "✅ **Task Finished:**\n> 🟢 {processed}/{total} processed successfully\n> 🔴 {failed} failed"

# =====================================================================================
# ====== BROADCAST MESSAGES ======
# =====================================================================================

MSG_BROADCAST_START = "📣 **Broadcast Initiated...**\n\n⏳ Sit tight, this might take a while depending on the user base."
MSG_BROADCAST_COMPLETE = (
    "📢 **Broadcast Completed!** 📢\n\n"
    "⏱️ **Time Taken:** `{elapsed_time}`\n"
    "👥 **Target Audience:** `{total_users}` users\n"
    "✅ **Delivered:** `{successes}`\n"
    "❌ **Failed:** `{failures}`\n"
    "🗑️ **Dead Accounts Removed:** `{deleted_accounts}`"
)
MSG_BROADCAST_CANCEL = "🛑 **Aborting Broadcast:** `{broadcast_id}`\n\n⏳ Halting operations..."
MSG_INVALID_BROADCAST_CMD = "⚠️ **Error:** Please reply directly to the message you wish to broadcast."
MSG_BROADCAST_USAGE = (
    "📣 **Broadcast Instructions:**\n\n"
    "🔸 `/broadcast` - Send to everyone\n"
    "🔸 `/broadcast authorized` - Send to premium/authorized users\n"
    "🔸 `/broadcast regular` - Send to standard users\n\n"
    "💡 _Remember to reply to the target message!_"
)

# =====================================================================================
# ====== PERMISSION MESSAGES ======
# =====================================================================================

MSG_ERROR_UNAUTHORIZED = "🔒 **Access Denied:** You do not have the required permissions to view this."
MSG_ERROR_BROADCAST_RESTART = "⚠️ Please use the `/broadcast` command to initiate a new broadcast."
MSG_ERROR_BROADCAST_INSTRUCTION = "⚠️ To broadcast, use the `/broadcast` command and reply to the message you want to send."
MSG_ERROR_CALLBACK_UNSUPPORTED = "⚠️ This interaction has expired or is no longer supported."

# =====================================================================================
# ====== RATE LIMITING MESSAGES ======
# =====================================================================================

MSG_RATE_LIMIT_QUEUE_PRIORITY = (
    "⚡ **Priority Queue Active!**\n\n"
    "⏳ **Estimated Wait:** `~{wait_estimate} minute(s)`\n"
    "🚀 **Status:** Processing soon..."
)

MSG_RATE_LIMIT_QUEUE_REGULAR = (
    "⏳ **Rate Limit Reached!**\n\n"
    "⌛ **Estimated Wait:** `~{wait_estimate} minute(s)`\n"
    "📊 **Limit:** `{max_requests} files per {time_window} minute(s)`\n"
    "🔄 **Status:** Added to queue"
)

MSG_RATE_LIMIT_QUEUE_FULL = (
    "⚠️ **Servers Overloaded!**\n\n"
    "The processing queue is currently at maximum capacity.\n"
    "🕒 **Try again in:** `~{wait_estimate} minute(s)`\n\n"
    "💡 _Thank you for your patience!_"
)


# =====================================================================================
# ====== FILE TYPE DESCRIPTIONS ======
# =====================================================================================
MSG_FILE_TYPE_DOCUMENT = "📄 Document"
MSG_FILE_TYPE_PHOTO = "🖼️ Image"
MSG_FILE_TYPE_VIDEO = "🎬 Video"
MSG_FILE_TYPE_AUDIO = "🎵 Audio Track"
MSG_FILE_TYPE_VOICE = "🎤 Voice Note"
MSG_FILE_TYPE_STICKER = "🎨 Sticker"
MSG_FILE_TYPE_ANIMATION = "🎞️ GIF/Animation"
MSG_FILE_TYPE_VIDEO_NOTE = "📹 Video Note"
MSG_FILE_TYPE_UNKNOWN = "❓ Unknown Format"

# =====================================================================================
# ====== SYSTEM & STATUS MESSAGES ======
# =====================================================================================

MSG_SYSTEM_STATUS = (
    "✅ **System Overview**\n\n"
    "🕒 **Uptime:** `{uptime}`\n"
    "🤖 **Active Bots:** `{active_bots}`\n"
    "📊 **Global Load:** `{total_workload}` tasks\n\n"
    "📜 **Node Distribution:**\n"
    "{workload_items}\n"
    "⚙️ **System Version:** `v{version}`"
)

# ------ Speedtest Messages ------
MSG_SPEEDTEST_INIT = "🚀 **Initiating Speed Test...**"
MSG_SPEEDTEST_ERROR = "❌ **Speed Test Failed:** The server could not complete the diagnostic check."
MSG_SPEEDTEST_RESULT = (
    "⚡ **Network Diagnostics Complete** ⚡\n\n"
    "🔻 **Download:** `{download_mbps} Mbps`\n"
    "🔺 **Upload:** `{upload_mbps} Mbps`\n"
    "🏓 **Latency (Ping):** `{ping} ms`\n\n"
    "🌍 **Server:** `{server_name}` (`{server_country}`)\n"
    "🏢 **Sponsor:** `{server_sponsor}`\n"
    "📡 **ISP:** `{client_isp}`"
)
MSG_SYSTEM_STATS = (
    "📊 **Hardware & Performance Stats**\n\n"
    "⏱️ **Uptime:**\n"
    "├ Server: `{sys_uptime}`\n"
    "└ Bot: `{bot_uptime}`\n\n"
    "🧠 **CPU:**\n"
    "├ Usage: `{cpu_percent}%`\n"
    "├ Cores: `{cpu_cores}`\n"
    "└ Clock: `{cpu_freq} GHz`\n\n"
    "💾 **Memory (RAM):**\n"
    "├ Total: `{ram_total}`\n"
    "├ Used: `{ram_used}`\n"
    "└ Free: `{ram_free}`\n\n"
    "💽 **Storage:**\n"
    "├ Total: `{total}`\n"
    "├ Used: `{used}` (`{disk_percent}%`)\n"
    "└ Free: `{free}`\n\n"
    "📶 **Network IO:**\n"
    "├ 🔺 Uploaded: `{upload}`\n"
    "└ 🔻 Downloaded: `{download}`"
)

MSG_DB_STATS = "📊 **Database Overview**\n\n👥 **Total Registered Users:** `{total_users}`"
