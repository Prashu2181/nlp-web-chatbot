console.log("JS LOADED"); 

const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendBtn = document.getElementById("send-btn");
const langSelect = document.getElementById("language");

const micBtn = document.getElementById("mic-btn");

let recognition;
if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.continuous = false;
    recognition.interimResults = false;
}


function addMessage(sender, text) {
    const div = document.createElement("div");
    div.classList.add("message", sender);

    const msgText = document.createElement("div");
    msgText.textContent = text;

    const time = document.createElement("div");
    time.className = "time";
    time.textContent = new Date().toLocaleTimeString();

    div.appendChild(msgText);
    div.appendChild(time);

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}


function sendMessage() {
    const message = input.value.trim();
    if (message === "") return;

    addMessage("user", message);
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
    message: message,
    language: langSelect.value
})

    })
    .then(res => res.json())
    .then(data => {
        addMessage("bot", data.bot_reply);
    })
    .catch(err => {
        console.error(err);
        addMessage("bot", "Server error");
    });
}


sendBtn.addEventListener("click", sendMessage);


input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        e.preventDefault();
        sendMessage();
    }
});

micBtn.addEventListener("click", function () {
    if (!recognition) {
        alert("Voice recognition not supported in this browser");
        return;
    }

    recognition.start();

    recognition.onresult = function (event) {
        const voiceText = event.results[0][0].transcript;
        input.value = voiceText;
        sendMessage();
    };

    recognition.onerror = function () {
        alert("Voice input error");
    };
});
