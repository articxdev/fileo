# Knox/utils/messages.py

# =====================================================================================
# ====== ERROR MESSAGES ======
# =====================================================================================

# ------ General Errors ------
MSG_ERROR_GENERIC = "⚠️ **Oops!** Something went wrong. Please try again. If the issue persists, contact support."
MSG_ERROR_USER_INFO = "❗ **User Not Found:** Couldn't find user. Please check the ID or Username."

# ------ User Input & Validation Errors ------
MSG_INVALID_USER_ID = "❌ **Invalid User ID:** Please provide a numeric user ID."
MSG_ERROR_START_BOT = "⚠️ You need to start Knox in private first to use this command.\n👉 [Click here]({invite_link}) to start a private chat."
MSG_ERROR_REPLY_FILE = "⚠️ Please use the /link command in reply to a file."
MSG_ERROR_NO_FILE = "⚠️ The message you're replying to does not contain any file."
MSG_ERROR_INVALID_NUMBER = "⚠️ **Invalid number specified.**"
MSG_ERROR_NUMBER_RANGE = "⚠️ **Please specify a number between 1 and {max_files}.**"
MSG_ERROR_DM_FAILED = "⚠️ I couldn't send you a Direct Message. Please start Knox first."

# ------ File & Media Errors ------
MSG_ERROR_PROCESSING_MEDIA = "⚠️ **Oops!** Something went wrong while processing your media. Please try again. If the issue persists, contact support."

# ------ Admin Action Errors (Ban, Auth, etc.) ------
MSG_AUTHORIZE_FAILED = (
    "❌ **Authorization Failed:** "
    "Could not authorize user `{user_id}`."
)
MSG_DEAUTHORIZE_FAILED = (
    "❌ **Deauthorization Failed:** "
    "User `{user_id}` was not authorized or an error occurred."
)
MSG_TOKEN_FAILED = (
    "⚠️ **Token Activation Failed!**\n\n"
    "> ❗ Reason: {reason}\n\n"
    "🔑 Please check your token or contact support."
)
MSG_SHELL_ERROR = """**❌ Shell Command Error ❌**
<pre>{error}</pre>"""

# ------ System & Bot Errors ------
MSG_ERROR_NOT_ADMIN = "⚠️ **Admin Required:** I need admin privileges to work here."
MSG_DC_INVALID_USAGE = "🤔 **Invalid Usage:** Please reply to a user's message or a media file to get DC info."
MSG_DC_ANON_ERROR = "😥 **Cannot Get Your DC Info:** Unable to identify you. This command might not work for anonymous users."
MSG_DC_FILE_ERROR = "⚙️ **Error Getting File DC Info:** Could not fetch details. File might be inaccessible."
MSG_STATS_ERROR = "❌ **Stats Error:** Could not retrieve system statistics."
MSG_STATUS_ERROR = "❌ **Status Error:** Could not retrieve system status."
MSG_DB_ERROR = "❌ **Database Error:** Could not retrieve user count."
MSG_CRITICAL_ERROR = (
    "🚨 **Critical Media Processing Error** 🚨\n\n"
    "> ⚠️ Details:\n```\n{error}\n```\n\n"
    "Please investigate immediately! (ID: {error_id})"
)

# =====================================================================================
# ====== ADMIN MESSAGES ======
# =====================================================================================

# ------ Ban/Unban ------
MSG_DECORATOR_BANNED = "You are currently banned and cannot use Knox.\nReason: {reason}\nBanned on: {ban_time}"
MSG_BAN_USAGE = "⚠️ **Usage:** /ban [user_id] [reason]"
MSG_CANNOT_BAN_OWNER = "❌ **Cannot ban an owner.**"
MSG_ADMIN_USER_BANNED = "✅ **User {user_id} has been banned."
MSG_BAN_REASON_SUFFIX = "\n📝 **Reason:** {reason}"
MSG_ADMIN_NO_BAN_REASON = "No reason provided"
MSG_USER_BANNED_NOTIFICATION = "🚫 **You have been banned from using Knox.**"
MSG_UNBAN_USAGE = "⚠️ **Usage:** /unban <user_id>"
MSG_ADMIN_USER_UNBANNED = "✅ **User {user_id} has been unbanned."
MSG_USER_UNBANNED_NOTIFICATION = "🎉 **You have been unbanned from using Knox.**"
MSG_USER_NOT_IN_BAN_LIST = "ℹ️ **User {user_id} was not found in the ban list."
MSG_CHANNEL_BANNED = "✅ **Channel {channel_id} has been banned.**"
MSG_CHANNEL_BANNED_REASON_SUFFIX = "\n📝 **Reason:** {reason}"
MSG_CHANNEL_UNBANNED = "✅ **Channel {channel_id} has been unbanned.**"
MSG_CHANNEL_NOT_BANNED = "ℹ️ **Channel {channel_id} was not found in the ban list.**"

# ------ Token & Authorization ------
MSG_AUTHORIZE_USAGE = "🔑 **Usage:** `/authorize <user_id>`"
MSG_DEAUTHORIZE_USAGE = "🔒 **Usage:** `/deauthorize <user_id>`"
MSG_AUTHORIZE_SUCCESS = (
    "✅ **User Authorized!**\n\n"
    "> 👤 User ID: `{user_id}`\n"
    "> 🔑 Access: Permanent"
)
MSG_DEAUTHORIZE_SUCCESS = (
    "✅ **User Deauthorized!**\n\n"
    "> 👤 User ID: `{user_id}`\n"
    "> 🔒 Access: Revoked"
)
MSG_TOKEN_ACTIVATED = "✅ Token successfully activated!\n\n⏳ This token is valid for {duration_hours} hours."
MSG_TOKEN_INVALID = "🚫 **Expired or Invalid Token.** Please click the button below to activate your access token."
MSG_NO_AUTH_USERS = "ℹ️ **No Authorized Users Found:** The list is currently empty."
MSG_AUTH_USER_INFO = """{i}. 👤 User ID: `{user_id}`
   • Authorized by: `{authorized_by}`
   • Date: `{auth_time}`\n\n"""
MSG_ADMIN_AUTH_LIST_HEADER = "🔐 **Authorized Users List**\n\n"

# ------ Shell Commands ------
MSG_SHELL_USAGE = (
    "<b>Usage:</b>\n"
    "/shell <command>\n\n"
    "<b>Example:</b>\n"
    "/shell ls -l"
)
MSG_SHELL_EXECUTING = "Executing Command... ⚙️\n<pre>{command}</pre>"
MSG_SHELL_OUTPUT = """**Shell Command Output:**
<pre>{output}</pre>"""
MSG_SHELL_OUTPUT_STDOUT = "<b>[stdout]:</b>\n<pre>{output}</pre>"
MSG_SHELL_OUTPUT_STDERR = "<b>[stderr]:</b>\n<pre>{error}</pre>"
MSG_SHELL_NO_OUTPUT = "✅ <b>Command Executed:</b> No output."

# ------ Admin View & Control ------

MSG_WORKLOAD_ITEM = "   {bot_name}: {load}\n"
MSG_ADMIN_RESTART_DONE = "✅ **Restart Successful!**"
MSG_RESTARTING = "♻️ **Updating and Restarting Knox...**\n\n> ⏳ Please wait a moment."
MSG_LOG_FILE_CAPTION = "📄 **System Logs**"

MSG_LOG_FILE_EMPTY = "ℹ️ **Log File Empty:** No data found in the log file."
MSG_LOG_FILE_MISSING = "⚠️ **Log File Missing:** Could not find the log file."

# =====================================================================================
# ====== BUTTON TEXTS (User-facing) ======
# =====================================================================================

MSG_BUTTON_STREAM_NOW = "▶️ Stream"
MSG_BUTTON_DOWNLOAD = "⬇️ Download"
MSG_BUTTON_GET_HELP = "📖 Help"
MSG_BUTTON_CANCEL_BROADCAST = "🛑 Cancel"
MSG_BUTTON_VIEW_PROFILE = "👤 Profile"
MSG_BUTTON_ABOUT = "ℹ️ About"
MSG_BUTTON_JOIN_CHANNEL = "📢 Join {channel_title}"
MSG_BUTTON_START_CHAT = "💬 Open Knox"
MSG_BUTTON_CLOSE = "✖️ Close"


# =====================================================================================
# ====== COMMAND RESPONSES (User-facing) ======
# =====================================================================================

MSG_WELCOME = (
    "━━━━━━━━━━━━━━━━━━\n"
    "⚡ **Knox** · File to Link\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "Hey **{user_name}** 👋\n\n"
    "Send any file and get **instant** stream + download links.\n\n"
    "┌ **Quick start**\n"
    "├ 📩 Private → send a file\n"
    "├ 👥 Group → reply `/link` to a file\n"
    "└ 📖 `/help` for full guide\n\n"
    "Ready when you are 🚀"
)

MSG_HELP = (
    "━━━━━━━━━━━━━━━━━━\n"
    "📖 **Knox Help**\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "**Private chat**\n"
    "• Send any media → get links instantly\n\n"
    "**Groups**\n"
    "• Reply `/link` on a file\n"
    "• Batch: `/link 5` (max {max_files})\n"
    "• Knox must be **admin** in the group\n\n"
    "**Channels**\n"
    "• Add Knox as admin to auto-link new media\n\n"
    "**Commands**\n"
    "`/start` · `/help` · `/about` · `/ping` · `/dc`\n"
    "`/link` · `/link <n>` (groups)\n\n"
    "💡 Start Knox in DM before using `/link` in groups."
)

MSG_ABOUT = (
    "━━━━━━━━━━━━━━━━━━\n"
    "ℹ️ **About Knox**\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "Knox turns Telegram files into **direct stream & download links**.\n\n"
    "✓ Fast link generation\n"
    "✓ Online streaming player\n"
    "✓ All file types supported\n"
    "✓ Groups, channels & private chat\n"
    "✓ Batch `/link <n>` in groups\n\n"
    "Built for speed. Share Knox with friends ⚡"
)

# ------ Ping ------
MSG_PING_START = "🛰️ **Pinging...** Please wait."
MSG_PING_RESPONSE = (
    "☁️ **PONG! Knox is Online!** ⚡\n\n"
    "> ⏱️ **Ping:** {time_taken_ms:.2f} ms\n"
    "> 🤖 **Status:** `Active`"
)

# ------ DC Info ------
MSG_DC_USER_INFO = (
    "📍 **Information**\n"
    "> 👤 **User:** [{user_name}](tg://user?id={user_id})\n"
    "> 🆔 **User ID:** `{user_id}`\n"
    "> 🌍 **DC ID:** `{dc_id}`"
)

MSG_DC_FILE_INFO = (
    "🗂️ **File Information**\n"
    ">`{file_name}`\n"
    "💾 **File Size:** `{file_size}`\n"
    "📁 **File Type:** `{file_type}`\n"
    "🌍 **DC ID:** `{dc_id}`"
)

MSG_DC_UNKNOWN = "Unknown"

# ------ File Link Generation ------
MSG_DM_SINGLE_PREFIX = "📬 **From {chat_title}**\n"
MSG_LINKS = (
    "━━━━━━━━━━━━━━━━━━\n"
    "✅ **Links Ready**\n"
    "━━━━━━━━━━━━━━━━━━\n\n"
    "📄 `{file_name}`\n"
    "💾 `{file_size}`\n\n"
    "▶️ **Stream**\n`{stream_link}`\n\n"
    "⬇️ **Download**\n`{download_link}`\n\n"
    "_Tap the buttons below or copy the links._"
)

# =====================================================================================
# ====== USER NOTIFICATIONS ======
# =====================================================================================

MSG_NEW_USER = (
    "✨ **New User Alert!** ✨\n"
    "> 👤 **Name:** [{first_name}](tg://user?id={user_id})\n"
    "> 🆔 **User ID:** `{user_id}`\n\n"
)
MSG_COMMUNITY_CHANNEL = "📢 **{channel_title}:** 🔒 Join this channel to use Knox."

# =====================================================================================
# ====== PROCESSING MESSAGES ======
# =====================================================================================

# ------ General File Processing ------
MSG_PROCESSING_REQUEST = "⚡ **Knox** is preparing your links..."
MSG_PROCESSING_FILE = "⚡ **Knox** is preparing your links..."
MSG_NEW_FILE_REQUEST = (
    "> 👤 **Source:** [{source_info}](tg://user?id={id_})\n"
    "> 🆔 **ID:** `{id_}`\n\n"
    "🚀 **Download:** `{online_link}`\n\n"
    "🖥️ **Stream:** `{stream_link}`"
)

# ------ Batch Processing ------
MSG_PROCESSING_BATCH = "♻️ **Processing Batch {batch_number}/{total_batches}** ({file_count} files)"
MSG_PROCESSING_STATUS = "📊 **Processing Files:** {processed}/{total} complete, {failed} failed"
MSG_BATCH_LINKS_READY = "🔗 Here are your {count} download links:"
MSG_DM_BATCH_PREFIX = "📬 **Batch Links from {chat_title}**\n"
MSG_PROCESSING_RESULT = "✅ **Process Complete:** {processed}/{total} files processed successfully, {failed} failed"

# =====================================================================================
# ====== BROADCAST MESSAGES ======
# =====================================================================================

MSG_BROADCAST_START = "📣 **Starting Broadcast...**\n\n> ⏳ Please wait for completion."
MSG_BROADCAST_COMPLETE = (
    "📢 **Broadcast Completed Successfully!** 📢\n\n"
    "⏱️ **Duration:** `{elapsed_time}`\n"
    "👥 **Total Users:** `{total_users}`\n"
    "✅ **Successful Deliveries:** `{successes}`\n"
    "❌ **Failed Deliveries:** `{failures}`\n"
    "🗑️ **Accounts Removed (Blocked/Deactivated):** `{deleted_accounts}`\n"
)
MSG_BROADCAST_CANCEL = "🛑 **Cancelling Broadcast:** `{broadcast_id}`\n\n> ⏳ Stopping operations..."
MSG_INVALID_BROADCAST_CMD = "Please reply to the message you want to broadcast."
MSG_BROADCAST_USAGE = (
    "📣 **Broadcast Command Usage:**\n\n"
    "`/broadcast` - Broadcast to all users\n"
    "`/broadcast authorized` - Broadcast to authorized users only\n"
    "`/broadcast regular` - Broadcast to regular (non-authorized) users only\n\n"
    "**Note:** Reply to the message you want to broadcast."
)

# =====================================================================================
# ====== PERMISSION MESSAGES ======
# =====================================================================================

MSG_ERROR_UNAUTHORIZED = "You are not authorized to view this information."
MSG_ERROR_BROADCAST_RESTART = "Please use the /broadcast command to start a new broadcast."
MSG_ERROR_BROADCAST_INSTRUCTION = "To start a new broadcast, use the /broadcast command and reply to the message you want to broadcast."
MSG_ERROR_CALLBACK_UNSUPPORTED = "This button is not active or no longer supported."

# =====================================================================================
# ====== RATE LIMITING MESSAGES ======
# =====================================================================================

MSG_RATE_LIMIT_QUEUE_PRIORITY = (
    "⚡ You're in the **Priority Queue!**\n\n"
    "> ⏳ **Estimated Wait:** `~{wait_estimate} minute{s}`\n"
    "> 🚀 **Status:** In Queue"
)

MSG_RATE_LIMIT_QUEUE_REGULAR = (
    "⏳ **Rate Limit Reached!**\n\n"
    "> ⌛ **Estimated Wait:** `~{wait_estimate} minute{s1}`\n"
    "> 📊 **Limit:** `{max_requests} files per {time_window} minute{s2}`\n"
    "> 🔄 **Status:** In Queue"
)

MSG_RATE_LIMIT_QUEUE_FULL = (
    "⚠️ **Service Busy!** The processing queue is currently full.\n\n"
    "> 🕒 **Please try again in:** `~{wait_estimate} minute{s}`\n"
    "> 💡 **Tip:** Try again later when system load decreases"
)


# =====================================================================================
# ====== FILE TYPE DESCRIPTIONS ======
# =====================================================================================
MSG_FILE_TYPE_DOCUMENT = "📄 Document"
MSG_FILE_TYPE_PHOTO = "🖼️ Photo"
MSG_FILE_TYPE_VIDEO = "🎬 Video"
MSG_FILE_TYPE_AUDIO = "🎵 Audio"
MSG_FILE_TYPE_VOICE = "🎤 Voice Message"
MSG_FILE_TYPE_STICKER = "🎨 Sticker"
MSG_FILE_TYPE_ANIMATION = "🎞️ Animation (GIF)"
MSG_FILE_TYPE_VIDEO_NOTE = "📹 Video Note"
MSG_FILE_TYPE_UNKNOWN = "❓ Unknown File Type"

# =====================================================================================
# ====== SYSTEM & STATUS MESSAGES ======
# =====================================================================================

MSG_SYSTEM_STATUS = (
    "✅ **System Status:** Operational\n\n"
    "> 🕒 **Uptime:** `{uptime}`\n"
    "> 🤖 **Bot Instances:** `{active_bots}`\n"
    "> 📊 **Total Workload:** `{total_workload}`\n\n"
    "📜 **Workload Distribution:**\n\n"
    "{workload_items}\n"
    "> ♻️ **Version:** `{version}`"
)

# ------ Speedtest Messages ------
MSG_SPEEDTEST_INIT = "🚀 **Running Speed Test...**"
MSG_SPEEDTEST_ERROR = "❌ **Speed Test Failed!**\n\n> Unable to complete the speed test. Please try again later."
MSG_SPEEDTEST_RESULT = (
    "⚡ **Speed Test Results**\n\n"
    "**SPEEDTEST INFO:**\n"
    "> **Download:** `{download_mbps} Mbps` (`{download_bps}/s`)\n"
    "> **Upload:** `{upload_mbps} Mbps` (`{upload_bps}/s`)\n"
    "> **Ping:** `{ping} ms`\n"
    "> **Timestamp:** `{timestamp}`\n"
    "> **Data Sent:** `{bytes_sent}`\n"
    "> **Data Received:** `{bytes_received}`\n\n"
    "**SERVER INFO:**\n"
    "> **Name:** `{server_name}`\n"
    "> **Country:** `{server_country}`\n"
    "> **Sponsor:** `{server_sponsor}`\n"
    "> **Latency:** `{server_latency} ms`\n"
    "> **Coordinates:** `{server_lat}, {server_lon}`\n\n"
    "**CLIENT DETAILS:**\n"
    "> **IP:** `{client_ip}`\n"
    "> **Coordinates:** `{client_lat}, {client_lon}`\n"
    "> **ISP:** `{client_isp}`\n"
    "> **ISP Rating:** `{client_isprating}`\n"
    "> **Country:** `{client_country}`"
)
MSG_SYSTEM_STATS = (
    "📊 **System Statistics**\n\n"
    "> System Uptime: {sys_uptime}\n"
    "> Bot Uptime: {bot_uptime}\n\n"
    "⚙️ **Performance:**\n"
    "> CPU: {cpu_percent}%\n"
    "> CPU Core: {cpu_cores}\n"
    "> Frequency: {cpu_freq} GHz\n\n"
    "💾 **RAM**\n"
    "> Total: {ram_total}\n"
    "> Used: {ram_used}\n"
    "> Free: {ram_free}\n\n"
    "💽 **Storage:**\n"
    "> Disk: `{disk_percent}%`\n"
    "> Total: `{total}`\n"
    "> Used: `{used}`\n"
    "> Free: `{free}`\n\n"
    "📶 **Network:**\n"
    "> 🔺 Upload: `{upload}`\n"
    "> 🔻 Download: `{download}`\n"
)

MSG_DB_STATS = "📊 **Database Statistics**\n\n> 👥 **Total Users:** `{total_users}`"
